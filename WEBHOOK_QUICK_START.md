# 🚀 Webhook Tool - Quick Start

## 30 Second Installation

```bash
cd /Users/mac/Projects/open-webui-multi-agent
./install-webhook-tool.sh
```

This will:
1. Copy webhook code to clipboard
2. Open Open WebUI admin panel
3. You paste and save
4. Done!

---

## Test It Immediately

### 1. Ask Content Strategist:
```
"Create a blog post about sustainable fashion for millennials"
```

### 2. Ask Social Media Manager:
```
"Schedule this to Instagram tomorrow at 2pm:
Check out our eco-friendly collection! 🌱"
```

### 3. Ask Data Analyst:
```
"Show me our top performing posts from last week"
```

---

## Available Functions

| Function | What It Does |
|----------|--------------|
| `trigger_content_generation()` | Generate blog posts, articles, scripts |
| `schedule_social_media_post()` | Schedule posts to any platform |
| `fetch_analytics_report()` | Get performance metrics |
| `process_media_file()` | Resize, compress, convert media |
| `trigger_campaign_workflow()` | Launch multi-channel campaigns |
| `send_custom_webhook()` | Connect to any service |
| `list_available_webhooks()` | See all webhooks |
| `get_webhook_logs()` | View activity logs |

---

## Connect to n8n (Optional)

```bash
# Install n8n
npx n8n

# Opens at: http://localhost:5678
```

Then import workflows from:
```
workflows/n8n-complete-workflows.json
```

---

## Connect to Other Services

### Zapier
```python
send_custom_webhook(
    url="https://hooks.zapier.com/hooks/catch/YOUR_ID",
    payload={"action": "do_something"}
)
```

### Discord
```python
send_custom_webhook(
    url="https://discord.com/api/webhooks/YOUR_WEBHOOK",
    payload={"content": "Message from AI!"}
)
```

### Slack
```python
send_custom_webhook(
    url="https://hooks.slack.com/services/YOUR_WEBHOOK",
    payload={"text": "Hello from OpenWebUI!"}
)
```

---

## Example Conversations

### Content Creation
```
You: Create 5 blog post ideas about AI in healthcare
Content Strategist: [Generates ideas and offers to trigger content generation]
You: Yes, create the first one
Content Strategist: [Calls trigger_content_generation()]
✅ Content generation workflow started!
```

### Social Scheduling
```
You: Post this to all our social channels tomorrow at 10am:
     "New product launch! Limited time offer 🚀"
Social Media Manager: [Calls schedule_social_media_post() for each platform]
✅ Scheduled to Instagram, Twitter, LinkedIn, Facebook
```

### Analytics
```
You: How did we perform last month?
Data Analyst: [Calls fetch_analytics_report()]
📊 Analytics Report:
   - Total Views: 125K
   - Engagement: 8.5K
   - Top Post: "AI Marketing Trends" (15K views)
```

---

## Troubleshooting

### Webhook fails?
1. Check n8n is running: http://localhost:5678
2. View logs: Ask AI "show webhook logs"
3. Test manually: https://webhook.site

### n8n not receiving?
1. Verify webhook path in n8n
2. Activate the workflow
3. Check n8n execution log

---

## File Locations

- **Webhook Code:** `functions/webhook_manager.py`
- **Full Guide:** `WEBHOOK_GUIDE.md`
- **n8n Workflows:** `workflows/n8n-complete-workflows.json`
- **Install Script:** `install-webhook-tool.sh`

---

## Quick Commands

```bash
# Copy webhook code
cat functions/webhook_manager.py | pbcopy

# Run n8n
npx n8n

# Test webhook
curl -X POST http://localhost:5678/webhook/content-generation \
  -H "Content-Type: application/json" \
  -d '{"topic": "AI Trends", "content_type": "blog"}'
```

---

**🎉 Your AI personas can now automate everything!**

Full documentation: `WEBHOOK_GUIDE.md`
