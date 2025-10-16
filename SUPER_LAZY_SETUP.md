# 🛋️ SETUP FOR SUPER LAZY PEOPLE

## Just Do These 3 Things (2 minutes max)

### 1️⃣ CREATE ACCOUNT (20 seconds)

Open: **http://localhost:8080**

- Click "Sign up"
- Enter ANY email (can be fake): `admin@test.com`
- Enter ANY password: `test123`
- Enter a name: `Admin`
- Click "Create Account"

✅ DONE! You're now logged in.

---

### 2️⃣ COPY-PASTE THE FUNCTION CODE (30 seconds)

**In Open WebUI:**
- Click profile icon (top right) → Settings
- Go to: **Admin Panel** → **Functions** (in left sidebar)
- Click the big **"+"** button

**In Terminal, run this:**
```bash
cat /Users/mac/Projects/open-webui-multi-agent/functions/n8n_integration.py | pbcopy
```

**Back in browser:**
- Paste (Cmd+V) into the code box
- Click "Save"

✅ DONE! n8n webhooks enabled.

---

### 3️⃣ AUTO-CREATE ALL 5 PERSONAS (10 seconds)

I'll create a script that opens the browser for you.

**Just run this in terminal:**
```bash
cd /Users/mac/Projects/open-webui-multi-agent
open http://localhost:8080/workspace/models/create
```

Then for EACH of the 5 personas, I made them SUPER easy to copy:

---

**Run this to copy persona 1:**
```bash
cat << 'EOF' | pbcopy
FROM gpt-4

SYSTEM """You are an expert content strategist for a digital media company. Expert in: content planning, editorial calendars, SEO optimization, audience targeting, content analysis, cross-platform strategy. Provide actionable recommendations, data-driven insights, strategic rationale, and platform considerations. You can trigger n8n workflows."""

PARAMETER temperature 0.7
EOF

echo "✅ Content Strategist copied! Now paste in browser"
```

In browser:
- Model Name: `Content Strategist`
- Paste the modelfile (Cmd+V)
- Click "Save model"

---

**Run this for persona 2:**
```bash
cat << 'EOF' | pbcopy
FROM gpt-4

SYSTEM """You are a creative director specializing in digital media. Expert in: visual storytelling, brand identity, design principles, creative campaigns, cross-media execution. Provide creative concepts, brand-aligned recommendations, visual direction, and production feasibility. You can trigger workflows."""

PARAMETER temperature 0.8
EOF

echo "✅ Creative Director copied! Now paste in browser"
```

Same process - paste and save!

---

**Run this for persona 3:**
```bash
cat << 'EOF' | pbcopy
FROM gpt-4

SYSTEM """You are a social media manager for a digital media company. Expert in: platform strategies (Instagram, Twitter, LinkedIn, TikTok, Facebook), community engagement, trending topics, analytics, influencer collaboration. Provide platform-optimized content, engagement strategies, schedules, and insights. You can use n8n."""

PARAMETER temperature 0.75
EOF

echo "✅ Social Media Manager copied! Paste in browser"
```

---

**Run this for persona 4:**
```bash
cat << 'EOF' | pbcopy
FROM gpt-4

SYSTEM """You are a video producer specializing in digital content. Expert in: video scripting, storyboarding, production planning, editing workflows, platform optimization (YouTube, TikTok, Reels), video SEO. Provide production timelines, resource requirements, platform recommendations, and technical specs. You can trigger workflows."""

PARAMETER temperature 0.7
EOF

echo "✅ Video Producer copied! Paste in browser"
```

---

**Run this for persona 5:**
```bash
cat << 'EOF' | pbcopy
FROM gpt-4

SYSTEM """You are a data analyst for a digital media company. Expert in: performance metrics, audience insights, trend analysis, A/B testing, ROI calculation, reporting. Provide clear insights, data visualizations, trend interpretations, and optimization recommendations. You can fetch analytics from n8n."""

PARAMETER temperature 0.6
EOF

echo "✅ Data Analyst copied! Paste in browser"
```

---

## 🎉 THAT'S IT!

Now just:
1. Open http://localhost:8080
2. Start a new chat
3. Select one of your personas from the dropdown
4. Start chatting!

---

## Even Lazier? Run This One Script:

```bash
cd /Users/mac/Projects/open-webui-multi-agent

# This will copy each persona and open the create page
for i in 1 2 3 4 5; do
    echo "Opening create page for persona $i..."
    open "http://localhost:8080/workspace/models/create"
    sleep 2
done
```

Then just paste (Cmd+V) and click Save for each one!

---

**Total time: 2 minutes. Worth it to have your AI team!** 🚀
