"""
OpenWebUI Webhook Manager
Handles both incoming and outgoing webhooks for multi-agent workflows
"""

import httpx
import json
import hashlib
import hmac
from typing import Optional, Dict, Any, List
from datetime import datetime
import os
from pydantic import BaseModel, Field


class WebhookConfig(BaseModel):
    """Configuration for a webhook endpoint"""
    name: str = Field(description="Friendly name for the webhook")
    url: str = Field(description="Target URL for outgoing webhooks")
    method: str = Field(default="POST", description="HTTP method")
    headers: Optional[Dict[str, str]] = Field(default_factory=dict)
    secret: Optional[str] = Field(default=None, description="Secret for HMAC signature")
    timeout: int = Field(default=30, description="Request timeout in seconds")


class WebhookLog(BaseModel):
    """Log entry for webhook activity"""
    timestamp: str
    webhook_name: str
    direction: str  # "outgoing" or "incoming"
    status: str  # "success" or "error"
    payload: Dict[str, Any]
    response: Optional[Dict[str, Any]] = None
    error: Optional[str] = None


class WebhookManager:
    """
    Manages webhook integrations for Open WebUI
    Supports n8n, Zapier, Make.com, and custom webhooks
    """

    def __init__(self):
        self.base_url = os.getenv("N8N_BASE_URL", "http://localhost:5678")
        self.timeout = 30.0
        self.logs: List[WebhookLog] = []
        self.max_logs = 100

        # Predefined webhook configurations
        self.webhooks = {
            "n8n_content_gen": WebhookConfig(
                name="Content Generation",
                url=f"{self.base_url}/webhook/content-generation",
                method="POST"
            ),
            "n8n_social_post": WebhookConfig(
                name="Social Media Post",
                url=f"{self.base_url}/webhook/social-post",
                method="POST"
            ),
            "n8n_analytics": WebhookConfig(
                name="Fetch Analytics",
                url=f"{self.base_url}/webhook/analytics",
                method="GET"
            ),
            "n8n_media_process": WebhookConfig(
                name="Media Processing",
                url=f"{self.base_url}/webhook/media-process",
                method="POST"
            ),
            "n8n_campaign": WebhookConfig(
                name="Campaign Workflow",
                url=f"{self.base_url}/webhook/campaign",
                method="POST"
            ),
        }

    def _generate_signature(self, payload: str, secret: str) -> str:
        """Generate HMAC signature for webhook security"""
        return hmac.new(
            secret.encode(),
            payload.encode(),
            hashlib.sha256
        ).hexdigest()

    def _log_webhook(self, log_entry: WebhookLog):
        """Add webhook activity to log"""
        self.logs.append(log_entry)
        # Keep only recent logs
        if len(self.logs) > self.max_logs:
            self.logs = self.logs[-self.max_logs:]

    async def send_webhook(
        self,
        webhook_name: str,
        payload: Dict[str, Any],
        custom_url: Optional[str] = None,
        custom_headers: Optional[Dict[str, str]] = None
    ) -> Dict[str, Any]:
        """
        Send data to a webhook endpoint

        Args:
            webhook_name: Name of predefined webhook or custom name
            payload: Data to send
            custom_url: Override URL for custom webhooks
            custom_headers: Additional headers
        """
        # Get webhook config
        if webhook_name in self.webhooks:
            config = self.webhooks[webhook_name]
        elif custom_url:
            config = WebhookConfig(
                name=webhook_name,
                url=custom_url,
                method="POST"
            )
        else:
            return {
                "success": False,
                "error": f"Unknown webhook '{webhook_name}' and no custom_url provided"
            }

        # Prepare headers
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "OpenWebUI-Webhook/1.0",
            **(config.headers or {}),
            **(custom_headers or {})
        }

        # Add signature if secret is configured
        if config.secret:
            payload_str = json.dumps(payload)
            signature = self._generate_signature(payload_str, config.secret)
            headers["X-Webhook-Signature"] = signature

        try:
            async with httpx.AsyncClient(timeout=config.timeout) as client:
                # Send request
                if config.method.upper() == "POST":
                    response = await client.post(config.url, json=payload, headers=headers)
                elif config.method.upper() == "GET":
                    response = await client.get(config.url, params=payload, headers=headers)
                elif config.method.upper() == "PUT":
                    response = await client.put(config.url, json=payload, headers=headers)
                else:
                    return {"success": False, "error": f"Unsupported method: {config.method}"}

                response.raise_for_status()

                # Parse response
                try:
                    response_data = response.json()
                except:
                    response_data = {"text": response.text}

                result = {
                    "success": True,
                    "status_code": response.status_code,
                    "data": response_data,
                    "execution_id": response.headers.get("x-n8n-execution-id"),
                    "webhook": config.name
                }

                # Log success
                self._log_webhook(WebhookLog(
                    timestamp=datetime.utcnow().isoformat(),
                    webhook_name=config.name,
                    direction="outgoing",
                    status="success",
                    payload=payload,
                    response=result
                ))

                return result

        except httpx.HTTPError as e:
            error_result = {
                "success": False,
                "error": str(e),
                "error_type": type(e).__name__,
                "webhook": config.name
            }

            # Log error
            self._log_webhook(WebhookLog(
                timestamp=datetime.utcnow().isoformat(),
                webhook_name=config.name,
                direction="outgoing",
                status="error",
                payload=payload,
                error=str(e)
            ))

            return error_result

    def get_logs(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get recent webhook logs"""
        recent_logs = self.logs[-limit:]
        return [log.dict() for log in recent_logs]

    def list_webhooks(self) -> List[Dict[str, str]]:
        """List all configured webhooks"""
        return [
            {
                "name": name,
                "display_name": config.name,
                "url": config.url,
                "method": config.method
            }
            for name, config in self.webhooks.items()
        ]


# Global instance
webhook_manager = WebhookManager()


# ============================================================================
# Open WebUI Function Definitions
# These functions are callable by AI personas in conversations
# ============================================================================

async def trigger_content_generation(
    topic: str,
    content_type: str = "blog",
    target_audience: str = "general",
    tone: str = "professional",
    word_count: int = 1000,
    seo_keywords: Optional[List[str]] = None,
    additional_context: Optional[str] = None,
    __user__: dict = {}
) -> str:
    """
    Trigger content generation workflow in n8n

    Args:
        topic: Main topic or title for the content
        content_type: Type of content (blog, article, social_post, email, video_script)
        target_audience: Who the content is for
        tone: Writing tone (professional, casual, friendly, authoritative)
        word_count: Target word count
        seo_keywords: List of SEO keywords to include
        additional_context: Any additional context or requirements

    Returns:
        Status message with workflow execution details
    """
    payload = {
        "topic": topic,
        "content_type": content_type,
        "target_audience": target_audience,
        "tone": tone,
        "word_count": word_count,
        "seo_keywords": seo_keywords or [],
        "additional_context": additional_context,
        "requested_by": __user__.get("name", "Anonymous"),
        "timestamp": datetime.utcnow().isoformat()
    }

    result = await webhook_manager.send_webhook("n8n_content_gen", payload)

    if result.get("success"):
        return f"""✅ Content generation workflow started!

📝 Topic: {topic}
📋 Type: {content_type}
🎯 Audience: {target_audience}
📊 Status: {result.get('status_code')}
🆔 Execution ID: {result.get('execution_id', 'N/A')}

The workflow is processing your request. You'll receive the generated content shortly."""
    else:
        return f"""❌ Failed to trigger content generation workflow

Error: {result.get('error')}
Type: {result.get('error_type', 'Unknown')}

Please check that n8n is running and the webhook is properly configured."""


async def schedule_social_media_post(
    platform: str,
    content: str,
    schedule_time: Optional[str] = None,
    media_urls: Optional[List[str]] = None,
    hashtags: Optional[List[str]] = None,
    caption: Optional[str] = None,
    __user__: dict = {}
) -> str:
    """
    Schedule a social media post via n8n

    Args:
        platform: Social media platform (instagram, twitter, linkedin, facebook, tiktok)
        content: Post content/text
        schedule_time: When to post (ISO format or "now" for immediate)
        media_urls: URLs of images/videos to attach
        hashtags: List of hashtags (without #)
        caption: Additional caption for media posts

    Returns:
        Confirmation message with scheduling details
    """
    payload = {
        "platform": platform.lower(),
        "content": content,
        "schedule_time": schedule_time or "now",
        "media_urls": media_urls or [],
        "hashtags": hashtags or [],
        "caption": caption,
        "scheduled_by": __user__.get("name", "Anonymous"),
        "timestamp": datetime.utcnow().isoformat()
    }

    result = await webhook_manager.send_webhook("n8n_social_post", payload)

    if result.get("success"):
        time_str = schedule_time if schedule_time and schedule_time != "now" else "immediately"
        return f"""✅ Social media post scheduled!

📱 Platform: {platform.capitalize()}
⏰ Scheduled: {time_str}
📝 Content: {content[:100]}{'...' if len(content) > 100 else ''}
🖼️ Media: {len(media_urls or [])} file(s)
#️⃣ Hashtags: {len(hashtags or [])}
🆔 Execution ID: {result.get('execution_id', 'N/A')}

Your post will be published as scheduled!"""
    else:
        return f"""❌ Failed to schedule social media post

Error: {result.get('error')}

Please verify the webhook configuration and try again."""


async def fetch_analytics_report(
    date_range: str = "last_7_days",
    metrics: Optional[List[str]] = None,
    platforms: Optional[List[str]] = None,
    report_format: str = "summary",
    __user__: dict = {}
) -> str:
    """
    Fetch analytics report from n8n

    Args:
        date_range: Time period (last_7_days, last_30_days, this_month, custom)
        metrics: Specific metrics to fetch (views, engagement, reach, conversions)
        platforms: Platforms to include (instagram, facebook, website, youtube)
        report_format: Output format (summary, detailed, csv)

    Returns:
        Analytics data summary
    """
    payload = {
        "date_range": date_range,
        "metrics": metrics or ["views", "engagement", "reach"],
        "platforms": platforms or ["all"],
        "report_format": report_format,
        "requested_by": __user__.get("name", "Anonymous"),
        "timestamp": datetime.utcnow().isoformat()
    }

    result = await webhook_manager.send_webhook("n8n_analytics", payload)

    if result.get("success"):
        data = result.get("data", {})
        return f"""📊 Analytics Report Generated

📅 Period: {date_range.replace('_', ' ').title()}
📈 Metrics: {', '.join(metrics or ['views', 'engagement', 'reach'])}
🌐 Platforms: {', '.join(platforms or ['all'])}
📋 Format: {report_format}
🆔 Execution ID: {result.get('execution_id', 'N/A')}

{json.dumps(data, indent=2) if data else 'Report is being generated...'}

The complete report will be available in your dashboard shortly."""
    else:
        return f"""❌ Failed to fetch analytics report

Error: {result.get('error')}"""


async def process_media_file(
    media_url: str,
    operations: List[str],
    output_format: Optional[str] = None,
    quality: str = "high",
    __user__: dict = {}
) -> str:
    """
    Process media files (images, videos) via n8n

    Args:
        media_url: URL of the media file to process
        operations: List of operations (resize, crop, compress, filter, convert, thumbnail)
        output_format: Desired output format (jpg, png, mp4, webm)
        quality: Quality setting (low, medium, high)

    Returns:
        Processing status and output URL
    """
    payload = {
        "media_url": media_url,
        "operations": operations,
        "output_format": output_format,
        "quality": quality,
        "processed_by": __user__.get("name", "Anonymous"),
        "timestamp": datetime.utcnow().isoformat()
    }

    result = await webhook_manager.send_webhook("n8n_media_process", payload)

    if result.get("success"):
        return f"""✅ Media processing started!

🖼️ Source: {media_url}
⚙️ Operations: {', '.join(operations)}
📦 Output: {output_format or 'same as source'}
⭐ Quality: {quality}
🆔 Execution ID: {result.get('execution_id', 'N/A')}

Processing your media file. The output will be ready shortly."""
    else:
        return f"""❌ Failed to process media file

Error: {result.get('error')}"""


async def trigger_campaign_workflow(
    campaign_name: str,
    campaign_type: str,
    channels: List[str],
    target_audience: Dict[str, Any],
    content_assets: Optional[List[str]] = None,
    budget: Optional[float] = None,
    start_date: Optional[str] = None,
    duration_days: int = 7,
    __user__: dict = {}
) -> str:
    """
    Trigger a marketing campaign workflow

    Args:
        campaign_name: Name of the campaign
        campaign_type: Type (product_launch, seasonal, awareness, conversion)
        channels: Marketing channels (email, social, paid_ads, content)
        target_audience: Audience parameters (age, location, interests)
        content_assets: List of content asset URLs
        budget: Campaign budget
        start_date: When to start (ISO format or "now")
        duration_days: Campaign duration in days

    Returns:
        Campaign setup confirmation
    """
    payload = {
        "campaign_name": campaign_name,
        "campaign_type": campaign_type,
        "channels": channels,
        "target_audience": target_audience,
        "content_assets": content_assets or [],
        "budget": budget,
        "start_date": start_date or "now",
        "duration_days": duration_days,
        "created_by": __user__.get("name", "Anonymous"),
        "timestamp": datetime.utcnow().isoformat()
    }

    result = await webhook_manager.send_webhook("n8n_campaign", payload)

    if result.get("success"):
        return f"""🚀 Campaign workflow initiated!

📢 Campaign: {campaign_name}
🎯 Type: {campaign_type}
📱 Channels: {', '.join(channels)}
👥 Target: {json.dumps(target_audience)}
💰 Budget: ${budget or 'Not specified'}
📅 Start: {start_date or 'Immediately'}
⏱️ Duration: {duration_days} days
🆔 Execution ID: {result.get('execution_id', 'N/A')}

Your campaign is being set up across all selected channels!"""
    else:
        return f"""❌ Failed to trigger campaign workflow

Error: {result.get('error')}"""


async def send_custom_webhook(
    url: str,
    payload: Dict[str, Any],
    method: str = "POST",
    headers: Optional[Dict[str, str]] = None,
    __user__: dict = {}
) -> str:
    """
    Send a custom webhook to any URL

    Args:
        url: Target webhook URL
        payload: Data to send
        method: HTTP method (POST, GET, PUT)
        headers: Optional custom headers

    Returns:
        Response from the webhook
    """
    # Add user context
    payload["_triggered_by"] = __user__.get("name", "Anonymous")
    payload["_timestamp"] = datetime.utcnow().isoformat()

    result = await webhook_manager.send_webhook(
        "custom_webhook",
        payload,
        custom_url=url,
        custom_headers=headers
    )

    if result.get("success"):
        return f"""✅ Custom webhook sent successfully!

🔗 URL: {url}
📤 Method: {method}
📦 Status: {result.get('status_code')}

Response: {json.dumps(result.get('data'), indent=2)}"""
    else:
        return f"""❌ Custom webhook failed

Error: {result.get('error')}"""


async def list_available_webhooks(__user__: dict = {}) -> str:
    """
    List all configured webhooks

    Returns:
        List of available webhook integrations
    """
    webhooks = webhook_manager.list_webhooks()

    webhook_list = "\n".join([
        f"• {w['display_name']} ({w['name']})\n  URL: {w['url']}\n  Method: {w['method']}"
        for w in webhooks
    ])

    return f"""📋 Available Webhook Integrations

{webhook_list}

You can trigger these webhooks using the specialized functions like:
- trigger_content_generation()
- schedule_social_media_post()
- fetch_analytics_report()
- process_media_file()
- trigger_campaign_workflow()
- send_custom_webhook()"""


async def get_webhook_logs(limit: int = 10, __user__: dict = {}) -> str:
    """
    Get recent webhook activity logs

    Args:
        limit: Number of recent logs to retrieve (max 100)

    Returns:
        Recent webhook logs
    """
    logs = webhook_manager.get_logs(min(limit, 100))

    if not logs:
        return "📝 No webhook activity yet."

    log_text = []
    for log in logs:
        status_emoji = "✅" if log['status'] == "success" else "❌"
        direction_emoji = "📤" if log['direction'] == "outgoing" else "📥"
        log_text.append(
            f"{status_emoji} {direction_emoji} {log['webhook_name']}\n"
            f"  Time: {log['timestamp']}\n"
            f"  Status: {log['status']}"
        )

    return f"""📊 Recent Webhook Activity (Last {len(logs)})

{chr(10).join(log_text)}"""
