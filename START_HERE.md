# 🚀 Quick Start - BrandFactory Multi-Agent Workspace

Your AI workspace is ready to deploy! Let's get started.

## ✅ What's Ready

- ✓ API configuration ready
- ✓ 5 AI personas (Content Strategist, Creative Director, Social Media Manager, Video Producer, Data Analyst)
- ✓ n8n webhook integration functions
- ✓ Full configuration files
- ✓ Docker deployment ready

## 🎯 Recommended: Start with Docker

Since pip installation is timing out, Docker is the fastest way to get started:

### Step 1: Install Docker Desktop (if not installed)

Download from: https://www.docker.com/products/docker-desktop

### Step 2: Start Everything

```bash
cd /Users/mac/Projects/open-webui-multi-agent

# Start all services (Open WebUI + n8n + Ollama)
docker-compose up -d

# Check if everything is running
docker-compose ps
```

This will start:
- **BrandFactory** on http://localhost:8080
- **n8n** on http://localhost:5678 (username: admin, password: changeme123)
- **Ollama** for local models on http://localhost:11434

### Step 3: Access Your AI Team

1. Open http://localhost:8080 in your browser
2. Create your admin account
3. Start chatting with your AI personas!

### Step 4: View Logs (if needed)

```bash
# View all logs
docker-compose logs -f

# View only BrandFactory logs
docker-compose logs -f brandfactory

# View n8n logs
docker-compose logs -f n8n
```

### Stop Services

```bash
docker-compose down
```

---

## 🔧 Alternative: Deploy to Render

The easiest way to deploy BrandFactory:

1. Fork this repository to your GitHub account
2. Connect to Render.com
3. Deploy using the included `render.yaml` configuration
4. Add your API keys in Render environment variables
5. Access your live BrandFactory instance!

---

## 📋 Your AI Personas

Once logged in, you can chat with:

1. **👔 Content Strategist** - Content planning, SEO, strategy
   - Ask about: Content calendars, audience targeting, SEO optimization

2. **🎨 Creative Director** - Visual storytelling, branding
   - Ask about: Creative campaigns, brand guidelines, visual direction

3. **📱 Social Media Manager** - Social strategy, engagement
   - Ask about: Social posts, hashtag strategies, platform optimization

4. **🎬 Video Producer** - Video production, scripting
   - Ask about: Video scripts, production planning, editing workflows

5. **📊 Data Analyst** - Analytics, insights, reporting
   - Ask about: Performance metrics, trend analysis, ROI

## 🔗 Connect to n8n Workflows

Once n8n is running at http://localhost:5678:

1. Login with: admin / changeme123
2. Import workflow templates from `workflows/n8n-examples.json`
3. Configure your social media credentials
4. Use the webhook functions from your AI personas!

Example:
```
trigger_content_generation(
    topic="Summer Campaign",
    content_type="social",
    target_audience="millennials",
    tone="exciting"
)
```

## 📚 Documentation

- **QUICKSTART.md** - Detailed getting started guide
- **README.md** - Complete documentation
- **workflows/n8n-examples.json** - n8n workflow templates
- **config.yaml** - System configuration

## 🆘 Troubleshooting

### Docker Issues
- Make sure Docker Desktop is running
- Check available disk space
- Try: `docker-compose down && docker-compose up -d`

### Connection Issues
- Wait 30-60 seconds after starting for services to initialize
- Check logs: `docker-compose logs -f`
- Verify ports 8080, 5678, 11434 are not in use

### API Key Issues
- Your OpenAI key is configured in `.env`
- Restart services after changing `.env`: `docker-compose restart`

## 🎉 Next Steps

1. **Set up n8n workflows** - Create automations for your content workflows
2. **Add brand knowledge** - Upload brand guidelines to the RAG system
3. **Customize personas** - Edit persona files in `data/personas/`
4. **Create templates** - Save common prompts for quick access
5. **Invite team** - Add team members to collaborate

---

**Need help?** Check QUICKSTART.md for detailed instructions!
