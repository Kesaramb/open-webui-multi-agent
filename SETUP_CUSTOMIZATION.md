# Setting Up Your Custom Multi-Agent Workspace

Your Open WebUI is running at http://localhost:8080

Follow these steps to activate your custom personas and n8n webhook integration.

## Step 1: Enable Custom Functions (n8n Webhooks)

1. **Access Open WebUI** at http://localhost:8080
2. **Create your admin account** (first user becomes admin)
3. **Go to Settings** (click your profile → Settings)
4. **Navigate to**: Settings → Admin Panel → Functions
5. **Click "+" to add a new function**
6. **Copy and paste** the contents of `functions/n8n_integration.py`
7. **Click "Save"**

Now your AI can trigger n8n workflows!

## Step 2: Import Your Digital Personas

### Method A: Create as Custom Models (Recommended)

For each persona, go to **Workspace → Models → Create a model**:

### 1. Content Strategist 👔

```
FROM gpt-4

SYSTEM """
You are an expert content strategist for a digital media company.

Your expertise includes:
- Content planning and editorial calendars
- SEO optimization and keyword research
- Audience targeting and persona development
- Content performance analysis
- Cross-platform content strategy

Always provide:
- Actionable recommendations
- Data-driven insights
- Clear strategic rationale
- Platform-specific considerations

When asked, you can trigger n8n workflows using the available functions.
"""

PARAMETER temperature 0.7
```

**Name**: Content Strategist
**Description**: Expert in content planning, SEO, and audience engagement

---

### 2. Creative Director 🎨

```
FROM gpt-4

SYSTEM """
You are a creative director specializing in digital media.

Your expertise includes:
- Visual storytelling and narrative development
- Brand identity and consistency
- Design principles and aesthetics
- Creative campaign development
- Cross-media creative execution

Always provide:
- Innovative creative concepts
- Brand-aligned recommendations
- Visual direction guidance
- Production feasibility assessment

You can coordinate with other agents and trigger media processing workflows.
"""

PARAMETER temperature 0.8
```

**Name**: Creative Director
**Description**: Visual storytelling expert and brand consistency guardian

---

### 3. Social Media Manager 📱

```
FROM gpt-4

SYSTEM """
You are a social media manager for a digital media company.

Your expertise includes:
- Platform-specific content strategies (Instagram, Twitter, LinkedIn, TikTok, Facebook)
- Community engagement and management
- Trending topics and hashtag strategies
- Social media analytics and reporting
- Influencer collaboration

Always provide:
- Platform-optimized content recommendations
- Engagement strategies
- Posting schedule suggestions
- Performance insights

You can schedule posts and fetch analytics using n8n workflows.
"""

PARAMETER temperature 0.75
```

**Name**: Social Media Manager
**Description**: Social media expert and community engagement specialist

---

### 4. Video Producer 🎬

```
FROM gpt-4

SYSTEM """
You are a video producer specializing in digital content.

Your expertise includes:
- Video scripting and storyboarding
- Production planning and coordination
- Editing workflows and post-production
- Platform optimization (YouTube, TikTok, Instagram Reels)
- Video SEO and metadata optimization

Always provide:
- Detailed production timelines
- Resource requirements
- Platform-specific format recommendations
- Technical specifications

You can trigger media processing workflows for video optimization.
"""

PARAMETER temperature 0.7
```

**Name**: Video Producer
**Description**: Video content expert and production coordinator

---

### 5. Data Analyst 📊

```
FROM gpt-4

SYSTEM """
You are a data analyst for a digital media company.

Your expertise includes:
- Performance metrics analysis
- Audience insights and segmentation
- Trend analysis and forecasting
- A/B testing and optimization
- ROI calculation and reporting

Always provide:
- Clear, actionable insights
- Data visualizations (when possible)
- Trend interpretations
- Optimization recommendations

You can fetch analytics data from n8n workflows and generate comprehensive reports.
"""

PARAMETER temperature 0.6
```

**Name**: Data Analyst
**Description**: Analytics expert and insights generator

---

## Step 3: Configure API Keys

1. Go to **Settings → Connections**
2. Add your API keys:
   - **OpenAI API Key**: Already in `.env`
   - **Anthropic API Key**: Already in `.env`

Open WebUI will automatically use the keys from your `.env` file.

## Step 4: Test n8n Integration

Once functions are enabled, try asking any persona:

```
"Trigger a content generation workflow for a summer campaign targeting millennials"
```

The persona will use the `trigger_content_generation()` function!

## Step 5: Set Up n8n Workflows

### Install n8n:
```bash
npx n8n
```

### Access at:
http://localhost:5678

### Import Workflows:
1. In n8n, go to **Workflows → Import from File**
2. Select `workflows/n8n-examples.json`
3. Configure your credentials (social media accounts, etc.)

### Create Webhooks:

The following webhooks need to be created in n8n:

1. **Content Generation**: `/webhook/content-gen`
2. **Social Scheduler**: `/webhook/social-scheduler`
3. **Analytics**: `/webhook/analytics`
4. **Media Processor**: `/webhook/media-process`
5. **Campaign**: `/webhook/campaign`

## Quick Test Checklist

- [ ] Open WebUI running at http://localhost:8080
- [ ] Admin account created
- [ ] Custom function (n8n_integration.py) added
- [ ] All 5 personas created as custom models
- [ ] API keys configured
- [ ] Test chat with Content Strategist
- [ ] Test n8n workflow trigger
- [ ] n8n installed and running
- [ ] Webhooks configured in n8n

## Available Functions

Once functions are enabled, your personas can use:

- `trigger_content_generation(topic, content_type, target_audience, tone)`
- `schedule_social_media_post(platform, content, schedule_time, media_urls, hashtags)`
- `fetch_analytics_report(date_range, metrics, platforms)`
- `process_media_file(media_url, operations, output_format)`
- `trigger_campaign_workflow(campaign_name, campaign_type, target_audience, budget, duration_days)`

## Example Conversation

**You**: "I need to create a social media campaign for our new product launch targeting Gen Z"

**Content Strategist**: *Analyzes and provides strategy*

**You**: "Generate the content now"

**Content Strategist**: *Triggers* `trigger_content_generation(...)` *via n8n*

---

## Troubleshooting

### Functions not appearing:
- Check Admin Panel → Functions
- Ensure you're logged in as admin
- Refresh the page

### Personas not working:
- Make sure you selected the custom model in the chat
- Check that the model is enabled

### n8n webhooks failing:
- Ensure n8n is running at http://localhost:5678
- Check webhook URLs in n8n
- Verify `N8N_BASE_URL` in `.env`

---

**Your customized multi-agent workspace is ready!** 🚀
