"""
title: Youtube Transcript Provider
author: ekatiyar
author_url: https://github.com/ekatiyar
git_url: https://github.com/ekatiyar/open-webui-tools
description: A tool that returns the full youtube transcript in English of a passed in youtube url.
requirements: langchain-yt-dlp, langchain-community, yt-dlp
version: 0.1.0
license: MIT
"""

from typing import Any, Callable
from langchain_community.document_loaders import YoutubeLoader
from langchain_yt_dlp.youtube_loader import YoutubeLoaderDL
from pydantic import BaseModel, Field


class EventEmitter:
    def __init__(self, event_emitter: Callable[[dict], Any] = None):
        self.event_emitter = event_emitter

    async def progress_update(self, description):
        await self.emit(description)

    async def error_update(self, description):
        await self.emit(description, "error", True)

    async def success_update(self, description):
        await self.emit(description, "success", True)

    async def emit(self, description="Unknown State", status="in_progress", done=False):
        if self.event_emitter:
            await self.event_emitter(
                {
                    "type": "status",
                    "data": {
                        "status": status,
                        "description": description,
                        "done": done,
                    },
                }
            )


class Tools:
    class Valves(BaseModel):
        CITATION: bool = Field(
            default=True, description="True or false for citation"
        )

    class UserValves(BaseModel):
        TRANSCRIPT_LANGUAGE: str = Field(
            default="en,en_auto",
            description="A comma-separated list of languages from highest priority to lowest.",
        )
        TRANSCRIPT_TRANSLATE: str = Field(
            default="en",
            description="The language you want the transcript to auto-translate to, if it does not already exist.",
        )
        GET_VIDEO_DETAILS: bool = Field(
            default=True, description="Grab video details, such as title and author"
        )

    def __init__(self):
        self.valves = self.Valves()
        self.citation = self.valves.CITATION

    async def get_youtube_transcript(
        self,
        url: str,
        __event_emitter__: Callable[[dict], Any] = None,
        __user__: dict = {},
    ) -> str:
        """
        Provides the title and full transcript of a YouTube video in English.
        Only use if the user supplied a valid YouTube URL.
        Examples of valid YouTube URLs: https://youtu.be/dQw4w9WgXcQ, https://www.youtube.com/watch?v=dQw4w9WgXcQ

        :param url: The URL of the youtube video that you want the transcript for.
        :return: The full transcript of the YouTube video in English, or an error message.
        """
        emitter = EventEmitter(__event_emitter__)
        if "valves" not in __user__:
            __user__["valves"] = self.UserValves()

        try:
            await emitter.progress_update(f"Validating URL: {url}")

            # Check if the URL is valid
            if not url or url == "":
                raise Exception(f"Invalid YouTube URL: {url}")
            # LLM's love passing in this url when the user doesn't provide one
            elif "dQw4w9WgXcQ" in url:
                raise Exception("Rick Roll URL provided... is that what you want?)")

            # Get video details if the user wants them
            title = ""
            author = ""
            if __user__["valves"].GET_VIDEO_DETAILS:
                await emitter.progress_update("Getting video details")
                details = await YoutubeLoaderDL.from_youtube_url(
                    url, add_video_info=True
                ).aload()

                if len(details) == 0:
                    raise Exception("Failed to get video details")

                title = details[0].metadata["title"]
                author = details[0].metadata["author"]
                await emitter.progress_update(
                    f"Grabbed details for {title} by {author}"
                )

            languages = [
                item.strip()
                for item in __user__["valves"].TRANSCRIPT_LANGUAGE.split(",")
            ]

            transcript = await YoutubeLoader.from_youtube_url(
                url,
                add_video_info=False,
                language=languages,
                translation=__user__["valves"].TRANSCRIPT_TRANSLATE,
            ).aload()

            if len(transcript) == 0:
                raise Exception(
                    f"Failed to find transcript for {title if title else url}"
                )

            transcript = "\n".join([document.page_content for document in transcript])

            if title and author:
                transcript = f"{title}\nby {author}\n\n{transcript}"

            await emitter.success_update(f"Transcript for video {title} retrieved!")
            return transcript

        except Exception as e:
            error_message = f"Error: {str(e)}"
            await emitter.error_update(error_message)
            return error_message
