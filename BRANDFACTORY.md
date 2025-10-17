# 🏭 BrandFactory - AI-Powered Multi-Agent Workspace

**BrandFactory** is your enterprise AI workspace designed specifically for digital media companies.

---

## 🎨 Branding

- **Name:** BrandFactory
- **Logo:** `static/brandfactory-logo.png`
- **Tagline:** AI-Powered Multi-Agent Workspace for Digital Media

---

## ✨ Features

### 5 Specialized AI Agents:
- 👔 **Content Strategist** - Content planning & SEO optimization
- 🎨 **Creative Director** - Visual storytelling & brand identity
- 📱 **Social Media Manager** - Multi-platform social media strategy
- 🎬 **Video Producer** - Video production & platform optimization
- 📊 **Data Analyst** - Performance metrics & insights

### Integrations:
- ✅ OpenAI (GPT-4, GPT-3.5 Turbo)
- ✅ Anthropic (Claude 3.5, Claude 3 Opus)
- ✅ N8N Workflow Automation
- ✅ Custom Webhook Functions

---

## 🚀 Deployment

### Live URL:
```
https://brandfactory.onrender.com
```

### Repository:
```
https://github.com/Kesaramb/open-webui-multi-agent
```

---

## 🎨 Customizing Branding

### Update Logo:
Replace `static/brandfactory-logo.png` with your custom logo (recommended: 512x512px PNG)

### Update Name:
In `render.yaml` or Render dashboard environment variables:
```yaml
WEBUI_NAME: "BrandFactory"
```

### Update Colors (via Admin Panel):
1. Login as admin
2. Go to Settings → Admin Panel → Interface
3. Customize colors, themes, and appearance

---

## 📊 Dashboard Access

### First Login:
1. Go to https://brandfactory.onrender.com
2. Click "Sign up"
3. First user automatically becomes **admin**

### Admin Panel:
- Settings → Admin Panel
- Manage users, functions, models, and configurations

---

## 🔑 API Configuration

### Add API Keys:
1. Settings → Connections
2. Add OpenAI API key
3. Add Anthropic API key

### Configure N8N:
1. Settings → Admin Panel → Functions
2. Find "N8N Streaming Agent"
3. Set webhook URL and credentials

---

## 👥 Team Setup

### Add Team Members:
1. Admin Panel → Users
2. Invite via email
3. Assign roles (user, admin)

### Permissions:
- **Admin:** Full access to all settings
- **User:** Access to chat and personas

---

## 🛠️ Technical Details

### Stack:
- **Frontend:** SvelteKit
- **Backend:** FastAPI (Python)
- **Database:** SQLite (persistent on Render)
- **Vector DB:** ChromaDB
- **Deployment:** Render (Docker)

### Resources:
- **RAM:** 2GB (Standard plan)
- **Storage:** 10GB persistent disk
- **Cost:** ~$27.50/month

---

## 📚 Using Your AI Agents

### Select a Persona:
1. Start new chat
2. Click model dropdown
3. Select one of the 5 personas

### Example Prompts:

**Content Strategist:**
```
"Create a 30-day content calendar for a tech startup"
```

**Creative Director:**
```
"Design a visual campaign for our product launch"
```

**Social Media Manager:**
```
"Create a week's worth of Instagram posts for our brand"
```

**Video Producer:**
```
"Plan a YouTube series about AI in business"
```

**Data Analyst:**
```
"Analyze our content performance and suggest improvements"
```

---

## 🔗 N8N Automation

### Available Workflows:
- Content generation
- Social media scheduling
- Analytics reporting
- Media processing
- Campaign management

### Trigger from Chat:
Just ask your AI agents to execute tasks:
```
"Generate a blog post and schedule social media promotion"
```

The agent will automatically trigger N8N workflows!

---

## 🎯 Roadmap

- [ ] Custom domain setup
- [ ] Additional AI model integrations
- [ ] Advanced RAG (document search)
- [ ] Team collaboration features
- [ ] Mobile app

---

## 📞 Support

- **GitHub Issues:** https://github.com/Kesaramb/open-webui-multi-agent/issues
- **N8N Docs:** https://docs.n8n.io

---

**Built with ❤️ for Digital Media Teams**

*BrandFactory - Enterprise AI Platform*
