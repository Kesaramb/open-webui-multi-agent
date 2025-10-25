"""
title: YouTube Transcript Extractor
author: BrandFactory
version: 1.0.0
description: Extract transcripts from YouTube videos using yt-dlp (cloud-friendly)
required_open_webui_version: 0.3.9
"""

import re
import json
from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field


class Filter:
    class Valves(BaseModel):
        priority: int = Field(
            default=0, description="Priority level for the filter operations."
        )
        use_proxy: bool = Field(
            default=False,
            description="Enable proxy for YouTube requests (if blocked by IP)"
        )
        proxy_url: str = Field(
            default="",
            description="Proxy URL (e.g., http://proxy:port or socks5://proxy:port)"
        )

    def __init__(self):
        self.valves = self.Valves()

    def extract_video_id(self, url: str) -> Optional[str]:
        """Extract YouTube video ID from URL"""
        patterns = [
            r'(?:youtube\.com\/watch\?v=|youtu\.be\/)([a-zA-Z0-9_-]{11})',
            r'youtube\.com\/embed\/([a-zA-Z0-9_-]{11})',
            r'youtube\.com\/v\/([a-zA-Z0-9_-]{11})',
        ]

        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        return None

    def get_transcript_ytdlp(self, video_url: str) -> Dict[str, Any]:
        """
        Get transcript using yt-dlp (works better with cloud IPs)
        """
        try:
            import yt_dlp

            ydl_opts = {
                'writesubtitles': True,
                'writeautomaticsub': True,
                'subtitleslangs': ['en', 'en-US', 'en-GB'],
                'skip_download': True,
                'quiet': True,
                'no_warnings': True,
            }

            # Add proxy if enabled
            if self.valves.use_proxy and self.valves.proxy_url:
                ydl_opts['proxy'] = self.valves.proxy_url

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(video_url, download=False)

                # Get automatic or manual subtitles
                subtitles = info.get('subtitles', {}) or info.get('automatic_captions', {})

                # Try to get English subtitles
                transcript_text = ""
                for lang in ['en', 'en-US', 'en-GB']:
                    if lang in subtitles:
                        # Get the first subtitle format (usually JSON or SRT)
                        sub_url = subtitles[lang][0]['url']

                        # Download and parse subtitles
                        import urllib.request
                        with urllib.request.urlopen(sub_url) as response:
                            subtitle_data = response.read().decode('utf-8')

                            # Parse JSON subtitle format
                            if 'json' in subtitles[lang][0].get('ext', ''):
                                sub_json = json.loads(subtitle_data)
                                events = sub_json.get('events', [])
                                transcript_text = ' '.join([
                                    seg.get('utf8', '')
                                    for event in events
                                    for seg in event.get('segs', [])
                                    if seg.get('utf8')
                                ])
                            else:
                                # For other formats, just use the raw text
                                # Remove timestamps and formatting
                                lines = subtitle_data.split('\n')
                                transcript_text = ' '.join([
                                    line for line in lines
                                    if line and not line.isdigit() and '-->' not in line
                                ])

                        if transcript_text.strip():
                            return {
                                'success': True,
                                'transcript': transcript_text.strip(),
                                'method': 'yt-dlp',
                                'language': lang,
                                'title': info.get('title', 'Unknown'),
                                'duration': info.get('duration', 0),
                                'channel': info.get('uploader', 'Unknown')
                            }

                return {
                    'success': False,
                    'error': 'No English subtitles found for this video',
                    'available_languages': list(subtitles.keys())
                }

        except Exception as e:
            return {
                'success': False,
                'error': f'yt-dlp error: {str(e)}',
                'method': 'yt-dlp'
            }

    def get_transcript_api(self, video_id: str) -> Dict[str, Any]:
        """
        Fallback: Get transcript using youtube-transcript-api
        (May not work from cloud IPs without proxy)
        """
        try:
            from youtube_transcript_api import YouTubeTranscriptApi
            from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

            # Get transcript list
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

            # Try to find English transcript
            try:
                transcript = transcript_list.find_transcript(['en', 'en-US', 'en-GB'])
                transcript_data = transcript.fetch()

                # Combine all text segments
                full_text = ' '.join([entry['text'] for entry in transcript_data])

                return {
                    'success': True,
                    'transcript': full_text,
                    'method': 'youtube-transcript-api',
                    'language': transcript.language_code
                }

            except NoTranscriptFound:
                # Try auto-generated transcript
                try:
                    transcript = transcript_list.find_generated_transcript(['en', 'en-US', 'en-GB'])
                    transcript_data = transcript.fetch()
                    full_text = ' '.join([entry['text'] for entry in transcript_data])

                    return {
                        'success': True,
                        'transcript': full_text,
                        'method': 'youtube-transcript-api (auto-generated)',
                        'language': transcript.language_code
                    }
                except Exception as e:
                    return {
                        'success': False,
                        'error': f'No transcript available: {str(e)}'
                    }

        except TranscriptsDisabled:
            return {
                'success': False,
                'error': 'Transcripts are disabled for this video'
            }
        except Exception as e:
            return {
                'success': False,
                'error': f'API error: {str(e)}'
            }

    async def inlet(self, body: dict, __user__: Optional[dict] = None) -> dict:
        """Process incoming messages to detect YouTube URLs"""
        messages = body.get("messages", [])

        if messages:
            user_message = messages[-1].get("content", "")

            # Check if message contains YouTube URL
            video_id = self.extract_video_id(user_message)

            if video_id:
                video_url = f"https://www.youtube.com/watch?v={video_id}"

                # Try yt-dlp first (better for cloud environments)
                result = self.get_transcript_ytdlp(video_url)

                # If yt-dlp fails, try the API method
                if not result.get('success'):
                    result = self.get_transcript_api(video_id)

                # Add transcript info to the message
                if result.get('success'):
                    transcript_info = (
                        f"\n\n📺 **YouTube Transcript Extracted**\n"
                        f"**Title:** {result.get('title', 'N/A')}\n"
                        f"**Channel:** {result.get('channel', 'N/A')}\n"
                        f"**Method:** {result.get('method')}\n"
                        f"**Language:** {result.get('language')}\n\n"
                        f"**Transcript:**\n{result['transcript'][:500]}...\n\n"
                        f"*Full transcript available for analysis*"
                    )

                    # Append to user message
                    messages[-1]["content"] = user_message + transcript_info
                else:
                    error_msg = (
                        f"\n\n⚠️ **Could not extract transcript**\n"
                        f"**Error:** {result.get('error')}\n\n"
                        f"**Troubleshooting:**\n"
                        f"1. Enable proxy in function settings if running from cloud\n"
                        f"2. Check if video has captions/subtitles enabled\n"
                        f"3. Try a different video\n"
                    )
                    messages[-1]["content"] = user_message + error_msg

        body["messages"] = messages
        return body
