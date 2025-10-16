"""
title: n8n Webhook Trigger
author: Open WebUI
author_url: https://github.com/open-webui
version: 1.0.0
required_open_webui_version: 0.3.0
"""

import httpx
import json
from typing import Optional, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field


class Tools:
    class Valves(BaseModel):
        n8n_webhook_url: str = Field(
            default="https://n8n-zdpc.onrender.com/webhook-test/0448ad6e-5bea-43b3-8278-80c84d58c44a",
            description="Your n8n webhook URL"
        )
        request_timeout: int = Field(
            default=30,
            description="Request timeout in seconds"
        )

    def __init__(self):
        self.valves = self.Valves()

    async def trigger_n8n_workflow(
        self,
        message: str = "Hello from Open WebUI",
        data: Optional[str] = None,
        __user__: dict = {}
    ) -> str:
        """
        Trigger your n8n workflow with custom data

        :param message: Message to send to n8n workflow
        :param data: Optional JSON string with additional data
        :return: Response from n8n workflow
        """

        # Parse additional data if provided
        extra_data = {}
        if data:
            try:
                extra_data = json.loads(data)
            except:
                pass

        # Build query parameters for GET request
        params = {
            "message": message,
            "triggered_by": __user__.get("name", "Anonymous"),
            "timestamp": datetime.utcnow().isoformat(),
            **extra_data
        }

        try:
            async with httpx.AsyncClient(timeout=self.valves.request_timeout) as client:
                response = await client.get(
                    self.valves.n8n_webhook_url,
                    params=params
                )
                response.raise_for_status()

                # Try to parse JSON response
                try:
                    result = response.json()
                    result_text = json.dumps(result, indent=2)
                except:
                    result_text = response.text

                return f"""✅ n8n Workflow Triggered Successfully!

📤 Sent: {message}
📥 Response:
{result_text}

🆔 Status: {response.status_code}
⏰ Time: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC"""

        except httpx.HTTPError as e:
            return f"""❌ Failed to trigger n8n workflow

Error: {str(e)}
Error Type: {type(e).__name__}

Please check:
1. n8n workflow is active
2. Webhook URL is correct
3. n8n service is running"""

        except Exception as e:
            return f"""❌ Unexpected error

Error: {str(e)}

Please check your n8n configuration."""

    async def trigger_n8n_with_post(
        self,
        payload_json: str,
        __user__: dict = {}
    ) -> str:
        """
        Trigger n8n workflow with POST request (if needed)

        :param payload_json: JSON string with data to send
        :return: Response from n8n workflow
        """

        try:
            payload = json.loads(payload_json)
        except:
            return "❌ Invalid JSON payload. Please provide valid JSON string."

        # Add user context
        payload["triggered_by"] = __user__.get("name", "Anonymous")
        payload["timestamp"] = datetime.utcnow().isoformat()

        try:
            async with httpx.AsyncClient(timeout=self.valves.request_timeout) as client:
                response = await client.post(
                    self.valves.n8n_webhook_url,
                    json=payload
                )
                response.raise_for_status()

                try:
                    result = response.json()
                    result_text = json.dumps(result, indent=2)
                except:
                    result_text = response.text

                return f"""✅ n8n Workflow Triggered (POST)

📤 Payload: {json.dumps(payload, indent=2)}
📥 Response:
{result_text}

🆔 Status: {response.status_code}"""

        except httpx.HTTPError as e:
            return f"""❌ Failed to trigger workflow

Error: {str(e)}"""

    async def check_n8n_status(
        self,
        __user__: dict = {}
    ) -> str:
        """
        Check if n8n webhook is reachable

        :return: Status of n8n webhook
        """

        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(
                    self.valves.n8n_webhook_url,
                    params={"test": "connection"}
                )

                return f"""✅ n8n Webhook is Reachable!

🔗 URL: {self.valves.n8n_webhook_url}
📊 Status Code: {response.status_code}
⏱️ Response Time: Fast

Your workflow is ready to use!"""

        except httpx.HTTPError as e:
            return f"""⚠️ n8n Webhook Check Failed

🔗 URL: {self.valves.n8n_webhook_url}
❌ Error: {str(e)}

Possible issues:
1. n8n workflow is not active
2. Webhook URL might be incorrect
3. Network connectivity issues"""

        except Exception as e:
            return f"""❌ Connection Error

Error: {str(e)}

Please verify your n8n webhook URL."""
