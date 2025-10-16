"""
n8n Webhook Integration Functions for Open WebUI
Enables seamless integration with n8n workflows
"""

import httpx
import json
from typing import Optional, Dict, Any
import os


class N8NIntegration:
    """Integration class for n8n workflows"""

    def __init__(self, base_url: str = None):
        self.base_url = base_url or os.getenv("N8N_BASE_URL", "http://localhost:5678")
        self.timeout = 30.0

    async def trigger_workflow(
        self,
        webhook_path: str,
        data: Dict[str, Any],
        method: str = "POST"
    ) -> Dict[str, Any]:
        """
        Trigger an n8n workflow via webhook

        Args:
            webhook_path: The webhook endpoint path (e.g., "/webhook/content-gen")
            data: The data to send to the webhook
            method: HTTP method (POST, GET, etc.)

        Returns:
            Dictionary with response data or error information
        """
        url = f"{self.base_url}{webhook_path}"

        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                if method.upper() == "POST":
                    response = await client.post(url, json=data)
                elif method.upper() == "GET":
                    response = await client.get(url, params=data)
                else:
                    return {"error": f"Unsupported HTTP method: {method}"}

                response.raise_for_status()

                return {
                    "success": True,
                    "status_code": response.status_code,
                    "data": response.json() if response.text else None,
                    "execution_id": response.headers.get("x-n8n-execution-id")
                }

        except httpx.HTTPError as e:
            return {
                "success": False,
                "error": str(e),
                "error_type": type(e).__name__
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "error_type": "UnexpectedError"
            }

    async def get_execution_status(self, execution_id: str) -> Dict[str, Any]:
        """
        Get the status of an n8n workflow execution

        Args:
            execution_id: The execution ID returned from trigger_workflow

        Returns:
            Dictionary with execution status information
        """
        url = f"{self.base_url}/api/v1/executions/{execution_id}"

        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(url)
                response.raise_for_status()

                return {
                    "success": True,
                    "data": response.json()
                }

        except httpx.HTTPError as e:
            return {
                "success": False,
                "error": str(e)
            }


# Open WebUI Function Definitions
# These functions will be automatically detected by Open WebUI

n8n = N8NIntegration()


async def trigger_content_generation(
    topic: str,
    content_type: str = "blog",
    target_audience: str = "general",
    tone: str = "professional",
    additional_context: Optional[str] = None
) -> str:
    """
    Trigger content generation workflow in n8n

    Args:
        topic: The topic for content generation
        content_type: Type of content (blog, social, video, etc.)
        target_audience: Target audience description
        tone: Tone of the content (professional, casual, friendly, etc.)
        additional_context: Any additional context or requirements
    """
    data = {
        "topic": topic,
        "content_type": content_type,
        "target_audience": target_audience,
        "tone": tone,
        "additional_context": additional_context
    }

    result = await n8n.trigger_workflow("/webhook/content-gen", data)

    if result.get("success"):
        return f"✓ Content generation workflow triggered successfully!\n" \
               f"Execution ID: {result.get('execution_id', 'N/A')}\n" \
               f"Status: {result.get('status_code')}"
    else:
        return f"✗ Failed to trigger workflow: {result.get('error')}"


async def schedule_social_media_post(
    platform: str,
    content: str,
    schedule_time: Optional[str] = None,
    media_urls: Optional[list] = None,
    hashtags: Optional[list] = None
) -> str:
    """
    Schedule a social media post via n8n

    Args:
        platform: Social media platform (twitter, linkedin, instagram, facebook)
        content: The post content
        schedule_time: When to publish (ISO format or "now")
        media_urls: List of media URLs to attach
        hashtags: List of hashtags to include
    """
    data = {
        "platform": platform,
        "content": content,
        "schedule_time": schedule_time or "now",
        "media_urls": media_urls or [],
        "hashtags": hashtags or []
    }

    result = await n8n.trigger_workflow("/webhook/social-scheduler", data)

    if result.get("success"):
        return f"✓ Social media post scheduled successfully on {platform}!\n" \
               f"Execution ID: {result.get('execution_id', 'N/A')}"
    else:
        return f"✗ Failed to schedule post: {result.get('error')}"


async def fetch_analytics_report(
    date_range: str = "last_7_days",
    metrics: Optional[list] = None,
    platforms: Optional[list] = None
) -> str:
    """
    Fetch analytics report from n8n

    Args:
        date_range: Date range for analytics (last_7_days, last_30_days, custom)
        metrics: List of metrics to include (engagement, reach, clicks, etc.)
        platforms: List of platforms to analyze
    """
    data = {
        "date_range": date_range,
        "metrics": metrics or ["engagement", "reach", "impressions"],
        "platforms": platforms or ["all"]
    }

    result = await n8n.trigger_workflow("/webhook/analytics", data)

    if result.get("success"):
        response_data = result.get("data", {})
        return f"✓ Analytics report generated!\n" \
               f"Data: {json.dumps(response_data, indent=2)}"
    else:
        return f"✗ Failed to fetch analytics: {result.get('error')}"


async def process_media_file(
    media_url: str,
    operations: list,
    output_format: Optional[str] = None
) -> str:
    """
    Process media files (images, videos) via n8n

    Args:
        media_url: URL of the media file to process
        operations: List of operations (resize, crop, compress, watermark, etc.)
        output_format: Desired output format
    """
    data = {
        "media_url": media_url,
        "operations": operations,
        "output_format": output_format
    }

    result = await n8n.trigger_workflow("/webhook/media-process", data)

    if result.get("success"):
        response_data = result.get("data", {})
        processed_url = response_data.get("processed_url", "N/A")
        return f"✓ Media processed successfully!\n" \
               f"Processed URL: {processed_url}"
    else:
        return f"✗ Failed to process media: {result.get('error')}"


async def trigger_campaign_workflow(
    campaign_name: str,
    campaign_type: str,
    target_audience: Dict[str, Any],
    budget: Optional[float] = None,
    duration_days: int = 7
) -> str:
    """
    Trigger a marketing campaign workflow

    Args:
        campaign_name: Name of the campaign
        campaign_type: Type of campaign (awareness, conversion, engagement)
        target_audience: Target audience parameters
        budget: Campaign budget
        duration_days: Campaign duration in days
    """
    data = {
        "campaign_name": campaign_name,
        "campaign_type": campaign_type,
        "target_audience": target_audience,
        "budget": budget,
        "duration_days": duration_days
    }

    result = await n8n.trigger_workflow("/webhook/campaign", data)

    if result.get("success"):
        return f"✓ Campaign '{campaign_name}' workflow triggered!\n" \
               f"Execution ID: {result.get('execution_id', 'N/A')}"
    else:
        return f"✗ Failed to trigger campaign: {result.get('error')}"
