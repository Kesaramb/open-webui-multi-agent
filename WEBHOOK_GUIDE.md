# 🔗 Webhook Integration Guide

Complete guide for connecting webhooks with your Open WebUI multi-agent workspace.

---

## 📋 What This Does

The webhook tool enables your AI personas to:
- ✅ **Send data** to n8n workflows
- ✅ **Trigger automated processes** (content generation, posting, analytics)
- ✅ **Process media files** through external services
- ✅ **Launch campaigns** across multiple channels
- ✅ **Connect to custom webhooks** (Zapier, Make.com, etc.)
- ✅ **Track webhook activity** with built-in logging

---

## 🚀 Quick Setup (2 minutes)

### Step 1: Add the Webhook Manager to Open WebUI

1. Open http://localhost:8080
2. Go to: **Settings** → **Admin Panel** → **Functions**
3. Click **"+"** to add a new function
4. Copy the webhook manager code:

```bash
cat /Users/mac/Projects/open-webui-multi-agent/functions/webhook_manager.py | pbcopy
```

5. Paste in the code editor
6. Click **"Save"**

✅ **Done!** All your AI personas can now use webhooks!

---

## 🎯 Available Functions

Your AI personas can now call these functions in conversations:

### 1️⃣ Content Generation
```python
trigger_content_generation(
    topic="10 AI Marketing Trends for 2024",
    content_type="blog",  # blog, article, social_post, email, video_script
    target_audience="marketing professionals",
    tone="professional",  # professional, casual, friendly, authoritative
    word_count=1500,
    seo_keywords=["AI marketing", "digital trends", "automation"],
    additional_context="Focus on practical applications"
)
```

**Example Chat:**
```
You: Hey Content Strategist, create a blog post about AI in marketing

AI: I'll trigger the content generation workflow for you!
[Calls trigger_content_generation function]
✅ Content generation workflow started!
📝 Topic: AI in Marketing
📋 Type: blog
🎯 Audience: marketing professionals
```

---

### 2️⃣ Social Media Posting
```python
schedule_social_media_post(
    platform="instagram",  # instagram, twitter, linkedin, facebook, tiktok
    content="Check out our latest blog post on AI trends! 🚀",
    schedule_time="2024-01-15T10:00:00Z",  # or "now"
    media_urls=["https://example.com/image.jpg"],
    hashtags=["AI", "Marketing", "Tech"],
    caption="AI is transforming marketing"
)
```

**Example Chat:**
```
You: Schedule this post to Instagram tomorrow at 10am: "New product launch! 🎉"

AI: I'll schedule that for you!
[Calls schedule_social_media_post function]
✅ Social media post scheduled!
📱 Platform: Instagram
⏰ Scheduled: 2024-01-15T10:00:00Z
```

---

### 3️⃣ Analytics Reports
```python
fetch_analytics_report(
    date_range="last_30_days",  # last_7_days, last_30_days, this_month
    metrics=["views", "engagement", "reach", "conversions"],
    platforms=["instagram", "facebook", "website"],
    report_format="detailed"  # summary, detailed, csv
)
```

**Example Chat:**
```
You: Data Analyst, show me our Instagram performance for the last month

AI: Fetching analytics for you...
[Calls fetch_analytics_report function]
📊 Analytics Report Generated
📅 Period: Last 30 Days
📈 Metrics: views, engagement, reach
```

---

### 4️⃣ Media Processing
```python
process_media_file(
    media_url="https://example.com/video.mp4",
    operations=["resize", "compress", "thumbnail"],
    output_format="mp4",
    quality="high"  # low, medium, high
)
```

**Example Chat:**
```
You: Process this video and create a thumbnail: https://example.com/promo.mp4

AI: Starting media processing...
[Calls process_media_file function]
✅ Media processing started!
🖼️ Source: https://example.com/promo.mp4
⚙️ Operations: resize, compress, thumbnail
```

---

### 5️⃣ Campaign Launch
```python
trigger_campaign_workflow(
    campaign_name="Summer Sale 2024",
    campaign_type="seasonal",  # product_launch, seasonal, awareness, conversion
    channels=["email", "social", "paid_ads"],
    target_audience={
        "age": "25-45",
        "interests": ["technology", "innovation"],
        "location": "US"
    },
    budget=5000.0,
    duration_days=14
)
```

**Example Chat:**
```
You: Launch our summer campaign across email and social media

AI: Setting up your campaign workflow...
[Calls trigger_campaign_workflow function]
🚀 Campaign workflow initiated!
📢 Campaign: Summer Sale 2024
🎯 Type: seasonal
📱 Channels: email, social
```

---

### 6️⃣ Custom Webhooks
```python
send_custom_webhook(
    url="https://hooks.zapier.com/hooks/catch/12345/abcde",
    payload={
        "message": "New lead generated",
        "lead_email": "john@example.com",
        "source": "website"
    },
    method="POST",
    headers={"Authorization": "Bearer token123"}
)
```

---

### 7️⃣ List Webhooks
```python
list_available_webhooks()
```

**Example Chat:**
```
You: What webhooks are available?

AI: [Calls list_available_webhooks function]
📋 Available Webhook Integrations
• Content Generation (n8n_content_gen)
• Social Media Post (n8n_social_post)
• Fetch Analytics (n8n_analytics)
...
```

---

### 8️⃣ View Logs
```python
get_webhook_logs(limit=20)
```

---

## 🔧 Connecting to n8n

### Option 1: Run n8n Locally (Recommended)

```bash
# Install and run n8n
npx n8n

# n8n will start at: http://localhost:5678
```

### Option 2: Use n8n Cloud

1. Sign up at https://n8n.io
2. Update your .env file:
```bash
N8N_BASE_URL=https://your-n8n-instance.app.n8n.cloud
```

---

## 📝 Creating n8n Workflows

### Example: Content Generation Workflow

1. Open n8n at http://localhost:5678
2. Create new workflow
3. Add **Webhook** trigger node:
   - Method: POST
   - Path: `content-generation`
4. Add **OpenAI** node:
   - Model: GPT-4
   - Prompt: Use `{{ $json.topic }}` and other parameters
5. Add **HTTP Response** node to send back results
6. Activate the workflow

**Your webhook URL will be:**
```
http://localhost:5678/webhook/content-generation
```

---

## 🎨 Using with AI Personas

### Natural Language Examples

**With Content Strategist:**
```
"Create a blog post about sustainable fashion trends for millennials"
→ Triggers content generation workflow
```

**With Social Media Manager:**
```
"Post this to Instagram at 3pm: Check out our new eco-friendly collection 🌱"
→ Triggers social posting workflow
```

**With Data Analyst:**
```
"Show me our top performing posts from last week"
→ Triggers analytics workflow
```

**With Video Producer:**
```
"Process this video and create thumbnails: https://drive.com/video.mp4"
→ Triggers media processing workflow
```

**With Creative Director:**
```
"Launch our spring campaign across all social channels"
→ Triggers campaign workflow
```

---

## 🔐 Security Features

### HMAC Signatures
Webhooks can include HMAC signatures for security:

```python
webhook_manager.webhooks["my_webhook"].secret = "your_secret_key"
```

The tool automatically adds `X-Webhook-Signature` header.

### Verify in n8n:
```javascript
// In n8n Function node
const crypto = require('crypto');
const signature = $node["Webhook"].json.headers['x-webhook-signature'];
const secret = 'your_secret_key';
const payload = JSON.stringify($node["Webhook"].json.body);
const expectedSignature = crypto
  .createHmac('sha256', secret)
  .update(payload)
  .digest('hex');

if (signature !== expectedSignature) {
  throw new Error('Invalid signature');
}
```

---

## 📊 Webhook Logging

All webhook activity is automatically logged:

```
✅ 📤 Content Generation
  Time: 2024-01-15T10:30:00Z
  Status: success

❌ 📤 Social Media Post
  Time: 2024-01-15T10:35:00Z
  Status: error
```

View logs anytime: `get_webhook_logs(limit=50)`

---

## 🔗 Connect to Other Services

### Zapier
```python
send_custom_webhook(
    url="https://hooks.zapier.com/hooks/catch/YOUR_ZAPIER_WEBHOOK",
    payload={"action": "create_task", "title": "Follow up with client"}
)
```

### Make.com (Integromat)
```python
send_custom_webhook(
    url="https://hook.us1.make.com/YOUR_MAKE_WEBHOOK",
    payload={"trigger": "new_lead", "data": {...}}
)
```

### Discord
```python
send_custom_webhook(
    url="https://discord.com/api/webhooks/YOUR_DISCORD_WEBHOOK",
    payload={"content": "New blog post published!"}
)
```

### Slack
```python
send_custom_webhook(
    url="https://hooks.slack.com/services/YOUR_SLACK_WEBHOOK",
    payload={"text": "Campaign launched successfully! 🚀"}
)
```

---

## 🧪 Testing Webhooks

### Test with webhook.site:
1. Go to https://webhook.site
2. Copy your unique URL
3. Send test webhook:

```python
send_custom_webhook(
    url="https://webhook.site/your-unique-id",
    payload={"test": "Hello from Open WebUI!"}
)
```

4. View the request in webhook.site dashboard

---

## 🛠️ Troubleshooting

### "Webhook failed" error
- ✅ Check n8n is running: `http://localhost:5678`
- ✅ Verify webhook URLs in `.env` file
- ✅ Ensure workflows are activated in n8n
- ✅ Check webhook logs: `get_webhook_logs()`

### Timeout errors
- Increase timeout in webhook config:
```python
webhook_manager.webhooks["n8n_content_gen"].timeout = 60
```

### n8n not receiving data
- Verify webhook path matches: `/webhook/content-generation`
- Check n8n execution log
- Test with Postman or curl first

---

## 📚 Advanced Configuration

### Add Custom Webhook

```python
from functions.webhook_manager import webhook_manager, WebhookConfig

webhook_manager.webhooks["my_custom"] = WebhookConfig(
    name="My Custom Webhook",
    url="https://api.myservice.com/webhook",
    method="POST",
    headers={"Authorization": "Bearer YOUR_TOKEN"},
    secret="your_secret_key",
    timeout=45
)
```

### Environment Variables

In `.env` file:
```bash
N8N_BASE_URL=http://localhost:5678
N8N_API_KEY=your_api_key_here

# For cloud n8n
# N8N_BASE_URL=https://your-instance.app.n8n.cloud
```

---

## 🎓 Real-World Examples

### 1. Automated Content Pipeline
```
User → Content Strategist: "Create 5 blog posts about AI"
→ Triggers content generation workflow
→ n8n generates content with GPT-4
→ Saves to Google Docs
→ Sends to editor for review
→ Schedules social media posts
```

### 2. Social Media Campaign
```
User → Social Media Manager: "Launch our product launch campaign"
→ Triggers campaign workflow
→ n8n creates posts for all platforms
→ Schedules posts over 7 days
→ Sets up monitoring
→ Sends daily performance reports
```

### 3. Analytics Dashboard
```
User → Data Analyst: "Show me this week's performance"
→ Triggers analytics workflow
→ n8n fetches data from all platforms
→ Generates charts and insights
→ Compiles into PDF report
→ Sends to stakeholders
```

---

## ✅ Next Steps

1. ✅ Add webhook_manager.py to Open WebUI functions
2. ✅ Install and run n8n: `npx n8n`
3. ✅ Create your first workflow in n8n
4. ✅ Test with your AI personas
5. ✅ Connect to your favorite services

---

## 📖 Resources

- **n8n Documentation:** https://docs.n8n.io
- **Open WebUI Functions:** https://docs.openwebui.com
- **Webhook Testing:** https://webhook.site
- **This Project:** `/Users/mac/Projects/open-webui-multi-agent/`

---

**Your AI team can now automate everything with webhooks!** 🚀
