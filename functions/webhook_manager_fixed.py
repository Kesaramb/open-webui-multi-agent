"""
title: Webhook Manager for Multi-Agent Workflows
author: Open WebUI
author_url: https://github.com/open-webui
version: 1.0.0
required_open_webui_version: 0.3.0
"""

import httpx
import json
import hashlib
import hmac
from typing import Optional, Dict, Any, List, Callable, Awaitable
from datetime import datetime
import os
from pydantic import BaseModel, Field


class Filter:
    class Valves(BaseModel):
        priority: int = Field(
            default=0, description="Priority level for the filter operations."
        )
        n8n_base_url: str = Field(
            default="http://localhost:5678",
            description="Base URL for n8n instance"
        )
        n8n_api_key: str = Field(
            default="",
            description="n8n API key (optional)"
        )

    class UserValves(BaseModel):
        pass

    def __init__(self):
        self.valves = self.Valves()
        self.logs: List[Dict[str, Any]] = []
        self.max_logs = 100

    def _generate_signature(self, payload: str, secret: str) -> str:
        """Generate HMAC signature for webhook security"""
        return hmac.new(
            secret.encode(),
            payload.encode(),
            hashlib.sha256
        ).hexdigest()

    def _log_webhook(self, log_entry: Dict[str, Any]):
        """Add webhook activity to log"""
        self.logs.append(log_entry)
        if len(self.logs) > self.max_logs:
            self.logs = self.logs[-self.max_logs:]

    async def send_webhook(
        self,
        webhook_path: str,
        payload: Dict[str, Any],
        method: str = "POST",
        custom_url: Optional[str] = None,
        custom_headers: Optional[Dict[str, str]] = None,
        secret: Optional[str] = None
    ) -> Dict[str, Any]:
        """Send data to a webhook endpoint"""

        url = custom_url if custom_url else f"{self.valves.n8n_base_url}{webhook_path}"

        headers = {
            "Content-Type": "application/json",
            "User-Agent": "OpenWebUI-Webhook/1.0",
            **(custom_headers or {})
        }

        if self.valves.n8n_api_key:
            headers["X-N8N-API-KEY"] = self.valves.n8n_api_key

        if secret:
            payload_str = json.dumps(payload)
            signature = self._generate_signature(payload_str, secret)
            headers["X-Webhook-Signature"] = signature

        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                if method.upper() == "POST":
                    response = await client.post(url, json=payload, headers=headers)
                elif method.upper() == "GET":
                    response = await client.get(url, params=payload, headers=headers)
                elif method.upper() == "PUT":
                    response = await client.put(url, json=payload, headers=headers)
                else:
                    return {"success": False, "error": f"Unsupported method: {method}"}

                response.raise_for_status()

                try:
                    response_data = response.json()
                except:
                    response_data = {"text": response.text}

                result = {
                    "success": True,
                    "status_code": response.status_code,
                    "data": response_data,
                    "execution_id": response.headers.get("x-n8n-execution-id")
                }

                self._log_webhook({
                    "timestamp": datetime.utcnow().isoformat(),
                    "webhook_path": webhook_path,
                    "direction": "outgoing",
                    "status": "success",
                    "payload": payload,
                    "response": result
                })

                return result

        except httpx.HTTPError as e:
            error_result = {
                "success": False,
                "error": str(e),
                "error_type": type(e).__name__
            }

            self._log_webhook({
                "timestamp": datetime.utcnow().isoformat(),
                "webhook_path": webhook_path,
                "direction": "outgoing",
                "status": "error",
                "payload": payload,
                "error": str(e)
            })

            return error_result


class Tools:
    def __init__(self):
        self.filter = Filter()

    async def trigger_content_generation(
        self,
        topic: str,
        content_type: str = "blog",
        target_audience: str = "general",
        tone: str = "professional",
        word_count: int = 1000,
        seo_keywords: Optional[str] = None,
        additional_context: Optional[str] = None,
        __user__: dict = {}
    ) -> str:
        """
        Trigger content generation workflow in n8n

        :param topic: Main topic or title for the content
        :param content_type: Type of content (blog, article, social_post, email, video_script)
        :param target_audience: Who the content is for
        :param tone: Writing tone (professional, casual, friendly, authoritative)
        :param word_count: Target word count
        :param seo_keywords: Comma-separated SEO keywords
        :param additional_context: Any additional context or requirements
        :return: Status message with workflow execution details
        """

        keywords_list = seo_keywords.split(",") if seo_keywords else []

        payload = {
            "topic": topic,
            "content_type": content_type,
            "target_audience": target_audience,
            "tone": tone,
            "word_count": word_count,
            "seo_keywords": [k.strip() for k in keywords_list],
            "additional_context": additional_context,
            "requested_by": __user__.get("name", "Anonymous"),
            "timestamp": datetime.utcnow().isoformat()
        }

        result = await self.filter.send_webhook("/webhook/content-generation", payload)

        if result.get("success"):
            return f"""✅ Content generation workflow started!

📝 Topic: {topic}
📋 Type: {content_type}
🎯 Audience: {target_audience}
📊 Status: {result.get('status_code')}
🆔 Execution ID: {result.get('execution_id', 'N/A')}

The workflow is processing your request."""
        else:
            return f"""❌ Failed to trigger content generation

Error: {result.get('error')}

Please check that n8n is running and the webhook is configured."""

    async def schedule_social_media_post(
        self,
        platform: str,
        content: str,
        schedule_time: Optional[str] = "now",
        media_urls: Optional[str] = None,
        hashtags: Optional[str] = None,
        caption: Optional[str] = None,
        __user__: dict = {}
    ) -> str:
        """
        Schedule a social media post via n8n

        :param platform: Social media platform (instagram, twitter, linkedin, facebook, tiktok)
        :param content: Post content/text
        :param schedule_time: When to post (ISO format or "now" for immediate)
        :param media_urls: Comma-separated URLs of images/videos
        :param hashtags: Comma-separated hashtags (without #)
        :param caption: Additional caption for media posts
        :return: Confirmation message
        """

        media_list = media_urls.split(",") if media_urls else []
        hashtag_list = hashtags.split(",") if hashtags else []

        payload = {
            "platform": platform.lower(),
            "content": content,
            "schedule_time": schedule_time or "now",
            "media_urls": [u.strip() for u in media_list],
            "hashtags": [h.strip() for h in hashtag_list],
            "caption": caption,
            "scheduled_by": __user__.get("name", "Anonymous"),
            "timestamp": datetime.utcnow().isoformat()
        }

        result = await self.filter.send_webhook("/webhook/social-post", payload)

        if result.get("success"):
            time_str = schedule_time if schedule_time != "now" else "immediately"
            return f"""✅ Social media post scheduled!

📱 Platform: {platform.capitalize()}
⏰ Scheduled: {time_str}
📝 Content: {content[:100]}{'...' if len(content) > 100 else ''}
🖼️ Media: {len(media_list)} file(s)
#️⃣ Hashtags: {len(hashtag_list)}
🆔 Execution ID: {result.get('execution_id', 'N/A')}"""
        else:
            return f"""❌ Failed to schedule post

Error: {result.get('error')}"""

    async def fetch_analytics_report(
        self,
        date_range: str = "last_7_days",
        metrics: Optional[str] = "views,engagement,reach",
        platforms: Optional[str] = "all",
        report_format: str = "summary",
        __user__: dict = {}
    ) -> str:
        """
        Fetch analytics report from n8n

        :param date_range: Time period (last_7_days, last_30_days, this_month, custom)
        :param metrics: Comma-separated metrics (views, engagement, reach, conversions)
        :param platforms: Comma-separated platforms (instagram, facebook, website, youtube)
        :param report_format: Output format (summary, detailed, csv)
        :return: Analytics data summary
        """

        metrics_list = metrics.split(",") if metrics else ["views", "engagement"]
        platforms_list = platforms.split(",") if platforms else ["all"]

        payload = {
            "date_range": date_range,
            "metrics": [m.strip() for m in metrics_list],
            "platforms": [p.strip() for p in platforms_list],
            "report_format": report_format,
            "requested_by": __user__.get("name", "Anonymous"),
            "timestamp": datetime.utcnow().isoformat()
        }

        result = await self.filter.send_webhook("/webhook/analytics", payload, method="GET")

        if result.get("success"):
            data = result.get("data", {})
            return f"""📊 Analytics Report Generated

📅 Period: {date_range.replace('_', ' ').title()}
📈 Metrics: {', '.join(metrics_list)}
🌐 Platforms: {', '.join(platforms_list)}
🆔 Execution ID: {result.get('execution_id', 'N/A')}

{json.dumps(data, indent=2) if data else 'Report is being generated...'}"""
        else:
            return f"""❌ Failed to fetch analytics

Error: {result.get('error')}"""

    async def process_media_file(
        self,
        media_url: str,
        operations: str,
        output_format: Optional[str] = None,
        quality: str = "high",
        __user__: dict = {}
    ) -> str:
        """
        Process media files (images, videos) via n8n

        :param media_url: URL of the media file to process
        :param operations: Comma-separated operations (resize, crop, compress, filter, convert, thumbnail)
        :param output_format: Desired output format (jpg, png, mp4, webm)
        :param quality: Quality setting (low, medium, high)
        :return: Processing status
        """

        operations_list = operations.split(",") if operations else []

        payload = {
            "media_url": media_url,
            "operations": [o.strip() for o in operations_list],
            "output_format": output_format,
            "quality": quality,
            "processed_by": __user__.get("name", "Anonymous"),
            "timestamp": datetime.utcnow().isoformat()
        }

        result = await self.filter.send_webhook("/webhook/media-process", payload)

        if result.get("success"):
            return f"""✅ Media processing started!

🖼️ Source: {media_url}
⚙️ Operations: {', '.join(operations_list)}
📦 Output: {output_format or 'same as source'}
⭐ Quality: {quality}
🆔 Execution ID: {result.get('execution_id', 'N/A')}"""
        else:
            return f"""❌ Failed to process media

Error: {result.get('error')}"""

    async def trigger_campaign_workflow(
        self,
        campaign_name: str,
        campaign_type: str,
        channels: str,
        target_audience_json: str,
        budget: Optional[float] = None,
        start_date: Optional[str] = "now",
        duration_days: int = 7,
        __user__: dict = {}
    ) -> str:
        """
        Trigger a marketing campaign workflow

        :param campaign_name: Name of the campaign
        :param campaign_type: Type (product_launch, seasonal, awareness, conversion)
        :param channels: Comma-separated channels (email, social, paid_ads, content)
        :param target_audience_json: JSON string with audience parameters
        :param budget: Campaign budget
        :param start_date: When to start (ISO format or "now")
        :param duration_days: Campaign duration in days
        :return: Campaign setup confirmation
        """

        channels_list = channels.split(",") if channels else []

        try:
            target_audience = json.loads(target_audience_json)
        except:
            target_audience = {"audience": target_audience_json}

        payload = {
            "campaign_name": campaign_name,
            "campaign_type": campaign_type,
            "channels": [c.strip() for c in channels_list],
            "target_audience": target_audience,
            "budget": budget,
            "start_date": start_date or "now",
            "duration_days": duration_days,
            "created_by": __user__.get("name", "Anonymous"),
            "timestamp": datetime.utcnow().isoformat()
        }

        result = await self.filter.send_webhook("/webhook/campaign", payload)

        if result.get("success"):
            return f"""🚀 Campaign workflow initiated!

📢 Campaign: {campaign_name}
🎯 Type: {campaign_type}
📱 Channels: {', '.join(channels_list)}
💰 Budget: ${budget or 'Not specified'}
📅 Start: {start_date}
⏱️ Duration: {duration_days} days
🆔 Execution ID: {result.get('execution_id', 'N/A')}"""
        else:
            return f"""❌ Failed to trigger campaign

Error: {result.get('error')}"""

    async def send_custom_webhook(
        self,
        url: str,
        payload_json: str,
        method: str = "POST",
        headers_json: Optional[str] = None,
        __user__: dict = {}
    ) -> str:
        """
        Send a custom webhook to any URL

        :param url: Target webhook URL
        :param payload_json: JSON string with data to send
        :param method: HTTP method (POST, GET, PUT)
        :param headers_json: Optional JSON string with custom headers
        :return: Response from the webhook
        """

        try:
            payload = json.loads(payload_json)
        except:
            return "❌ Invalid JSON in payload"

        headers = None
        if headers_json:
            try:
                headers = json.loads(headers_json)
            except:
                return "❌ Invalid JSON in headers"

        payload["_triggered_by"] = __user__.get("name", "Anonymous")
        payload["_timestamp"] = datetime.utcnow().isoformat()

        result = await self.filter.send_webhook(
            "",
            payload,
            method=method,
            custom_url=url,
            custom_headers=headers
        )

        if result.get("success"):
            return f"""✅ Custom webhook sent!

🔗 URL: {url}
📤 Method: {method}
📦 Status: {result.get('status_code')}

Response: {json.dumps(result.get('data'), indent=2)}"""
        else:
            return f"""❌ Custom webhook failed

Error: {result.get('error')}"""

    async def get_webhook_logs(
        self,
        limit: int = 10,
        __user__: dict = {}
    ) -> str:
        """
        Get recent webhook activity logs

        :param limit: Number of recent logs to retrieve (max 100)
        :return: Recent webhook logs
        """

        logs = self.filter.logs[-min(limit, 100):]

        if not logs:
            return "📝 No webhook activity yet."

        log_text = []
        for log in logs:
            status_emoji = "✅" if log['status'] == "success" else "❌"
            direction_emoji = "📤" if log['direction'] == "outgoing" else "📥"
            log_text.append(
                f"{status_emoji} {direction_emoji} {log['webhook_path']}\n"
                f"  Time: {log['timestamp']}\n"
                f"  Status: {log['status']}"
            )

        return f"""📊 Recent Webhook Activity (Last {len(logs)})

{chr(10).join(log_text)}"""
