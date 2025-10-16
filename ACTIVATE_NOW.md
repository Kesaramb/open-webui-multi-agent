# 🚀 ACTIVATE YOUR CUSTOM WORKSPACE - 5 MINUTES

Open WebUI is running at: **http://localhost:8080**

Follow these 3 simple steps to activate your custom digital media workspace.

---

## ✅ STEP 1: Create Your Account (30 seconds)

1. Open http://localhost:8080 in your browser
2. Click "Sign up"
3. Create your admin account
   - Name: Your name
   - Email: your@email.com
   - Password: (choose a password)
4. **You're now the admin!**

---

## ✅ STEP 2: Enable n8n Webhook Functions (2 minutes)

This enables your AI personas to trigger automated workflows.

1. **Click your profile icon** (top right) → **Settings**
2. Go to **Admin Panel** → **Functions**
3. Click the **"+"** button to add a new function
4. **Paste this entire code:**

```python
# Copy the entire contents of: functions/n8n_integration.py
# Or run: cat functions/n8n_integration.py
```

**Quick copy command:**
```bash
cat /Users/mac/Projects/open-webui-multi-agent/functions/n8n_integration.py
```

5. Click **"Save"**

✅ Functions enabled! Your AI can now trigger n8n workflows!

---

## ✅ STEP 3: Create Your 5 AI Personas (2 minutes)

Go to: **Workspace** (sidebar) → **Models** → Click **"+"** to create a model

### Create Each Persona:

For EACH persona below, click "Create a model" and paste the Modelfile:

---

### 👔 Persona 1: Content Strategist

**Name:** Content Strategist
**Base Model:** gpt-4 (or select from your available models)

**Modelfile:**
```
SYSTEM """You are an expert content strategist for a digital media company.

Your expertise: content planning, editorial calendars, SEO optimization, audience targeting, content performance analysis, cross-platform strategy.

Provide actionable recommendations, data-driven insights, clear strategic rationale, and platform-specific considerations.

You can trigger n8n workflows using available functions."""

PARAMETER temperature 0.7
```

**Click "Create"**

---

### 🎨 Persona 2: Creative Director

**Name:** Creative Director
**Base Model:** gpt-4

**Modelfile:**
```
SYSTEM """You are a creative director specializing in digital media.

Your expertise: visual storytelling, brand identity, design principles, creative campaign development, cross-media execution.

Provide innovative creative concepts, brand-aligned recommendations, visual direction guidance, and production feasibility assessments.

You can trigger media processing workflows."""

PARAMETER temperature 0.8
```

**Click "Create"**

---

### 📱 Persona 3: Social Media Manager

**Name:** Social Media Manager
**Base Model:** gpt-4

**Modelfile:**
```
SYSTEM """You are a social media manager for a digital media company.

Your expertise: platform-specific strategies (Instagram, Twitter, LinkedIn, TikTok, Facebook), community engagement, trending topics, analytics reporting, influencer collaboration.

Provide platform-optimized content recommendations, engagement strategies, posting schedules, and performance insights.

You can schedule posts and fetch analytics using n8n."""

PARAMETER temperature 0.75
```

**Click "Create"**

---

### 🎬 Persona 4: Video Producer

**Name:** Video Producer
**Base Model:** gpt-4

**Modelfile:**
```
SYSTEM """You are a video producer specializing in digital content.

Your expertise: video scripting, storyboarding, production planning, editing workflows, platform optimization (YouTube, TikTok, Reels), video SEO.

Provide detailed production timelines, resource requirements, platform-specific recommendations, and technical specifications.

You can trigger media processing workflows."""

PARAMETER temperature 0.7
```

**Click "Create"**

---

### 📊 Persona 5: Data Analyst

**Name:** Data Analyst
**Base Model:** gpt-4

**Modelfile:**
```
SYSTEM """You are a data analyst for a digital media company.

Your expertise: performance metrics analysis, audience insights, trend analysis, A/B testing, ROI calculation, reporting.

Provide clear actionable insights, data visualizations, trend interpretations, and optimization recommendations.

You can fetch analytics data from n8n workflows."""

PARAMETER temperature 0.6
```

**Click "Create"**

---

## 🎉 YOU'RE DONE!

### Test Your Setup:

1. **Start a new chat**
2. **Select "Content Strategist"** from the model dropdown
3. **Ask:** "Help me plan a 30-day content strategy for a tech startup"
4. **Watch your specialized AI persona respond!**

### Switch Between Personas:

- Click the model dropdown in any chat
- Select different personas for different tasks
- Content Strategist for planning
- Creative Director for creative work
- Social Media Manager for social posts
- Video Producer for video projects
- Data Analyst for analytics

### Trigger Automated Workflows:

Once n8n is set up, ask any persona:
- "Generate content for our summer campaign"
- "Schedule this post to Instagram"
- "Fetch our analytics from last month"

---

## 📚 Reference Files

All setup details in your project:

- `SETUP_CUSTOMIZATION.md` - Complete setup guide
- `personas_modelfiles.txt` - Copy-paste ready modelfiles
- `functions/n8n_integration.py` - Webhook integration code
- `workflows/n8n-examples.json` - n8n workflow templates

---

## 🔗 Next: Set Up n8n (Optional)

To enable automated workflows:

```bash
# Install n8n
npx n8n
```

Access at: http://localhost:5678
Import workflows from: `workflows/n8n-examples.json`

---

**Your customized multi-agent workspace is ready to use!** 🚀
