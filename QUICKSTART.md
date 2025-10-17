# Quick Start Guide
## BrandFactory Multi-Agent Workspace for Digital Media Company

## Installation Options

### Option 1: Docker (Recommended)

This is the easiest way to get started with everything pre-configured.

```bash
cd /Users/mac/Projects/open-webui-multi-agent

# Copy and configure environment variables
cp .env.template .env
# Edit .env and add your API keys

# Start all services (BrandFactory + n8n + Ollama)
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f brandfactory
```

Access the applications:
- BrandFactory: http://localhost:8080
- n8n: http://localhost:5678 (username: admin, password: changeme)
- Ollama: http://localhost:11434

### Option 2: Manual Installation

If Docker isn't available, install manually:

```bash
cd /Users/mac/Projects/open-webui-multi-agent

# Copy environment variables
cp .env.template .env
# Edit .env with your API keys

# Build and run with Docker
docker build -t brandfactory .
docker run -p 8080:8080 brandfactory
```

For n8n (in a separate terminal):
```bash
npx n8n
# or if installed globally:
n8n start
```

## Initial Setup

### 1. Configure API Keys

Edit the `.env` file:

```bash
# Required for AI functionality
OPENAI_API_KEY=sk-your-key-here
ANTHROPIC_API_KEY=sk-ant-your-key-here

# n8n connection
N8N_BASE_URL=http://localhost:5678

# Security (change in production!)
JWT_SECRET=your-random-secret-key-here
```

### 2. Set Up n8n Workflows

Open n8n at http://localhost:5678 and create webhooks for:

#### A. Content Generation Webhook
- URL: `/webhook/content-gen`
- Method: POST
- Expected data:
  ```json
  {
    "topic": "string",
    "content_type": "string",
    "target_audience": "string",
    "tone": "string",
    "additional_context": "string"
  }
  ```

#### B. Social Media Scheduler
- URL: `/webhook/social-scheduler`
- Method: POST
- Expected data:
  ```json
  {
    "platform": "string",
    "content": "string",
    "schedule_time": "string",
    "media_urls": ["array"],
    "hashtags": ["array"]
  }
  ```

#### C. Analytics Reporter
- URL: `/webhook/analytics`
- Method: POST
- Expected data:
  ```json
  {
    "date_range": "string",
    "metrics": ["array"],
    "platforms": ["array"]
  }
  ```

#### D. Media Processor
- URL: `/webhook/media-process`
- Method: POST
- Expected data:
  ```json
  {
    "media_url": "string",
    "operations": ["array"],
    "output_format": "string"
  }
  ```

### 3. First Login

1. Open http://localhost:8080
2. Create an admin account
3. Go to Settings → Models
4. Add your LLM providers (OpenAI, Anthropic, etc.)

## Using Your Digital Personas

### Available Personas

Your workspace includes 5 specialized AI personas:

1. **Content Strategist** 👔
   - Content planning and SEO
   - Editorial calendars
   - Audience targeting
   - Use for: Strategy sessions, content planning

2. **Creative Director** 🎨
   - Visual storytelling
   - Brand consistency
   - Creative campaigns
   - Use for: Campaign development, creative direction

3. **Social Media Manager** 📱
   - Platform-specific strategies
   - Community engagement
   - Trending topics
   - Use for: Social posts, engagement strategies

4. **Video Producer** 🎬
   - Video production planning
   - Script writing
   - Platform optimization
   - Use for: Video projects, production planning

5. **Data Analyst** 📊
   - Performance analysis
   - Insights generation
   - ROI tracking
   - Use for: Reports, data analysis

### Example Workflows

#### Workflow 1: Create a Social Media Campaign

1. Start chat with **Content Strategist**:
   ```
   I need a social media campaign for our new product launch.
   Target audience: Gen Z tech enthusiasts
   Duration: 2 weeks
   ```

2. Switch to **Creative Director**:
   ```
   Based on the content strategy, develop creative concepts
   for our Gen Z tech product launch campaign.
   ```

3. Use **Social Media Manager**:
   ```
   Create platform-specific content for Instagram, TikTok,
   and Twitter based on the creative direction provided.
   ```

4. Trigger n8n workflow directly:
   ```
   trigger_content_generation(
       topic="Gen Z Tech Product Launch",
       content_type="social",
       target_audience="Gen Z tech enthusiasts",
       tone="casual and exciting"
   )
   ```

#### Workflow 2: Video Production Pipeline

1. **Video Producer** - Script and plan:
   ```
   Create a 2-minute explainer video script about our product features.
   Target: YouTube and Instagram Reels
   ```

2. **Creative Director** - Visual direction:
   ```
   Provide visual direction and shot list for the explainer video.
   ```

3. **Social Media Manager** - Distribution strategy:
   ```
   Create a distribution and promotion strategy for the video
   across our social channels.
   ```

#### Workflow 3: Performance Analysis

1. **Data Analyst** - Fetch data:
   ```
   fetch_analytics_report(
       date_range="last_30_days",
       metrics=["engagement", "reach", "conversions"],
       platforms=["instagram", "twitter", "youtube"]
   )
   ```

2. **Content Strategist** - Strategy adjustments:
   ```
   Based on the analytics, recommend content strategy adjustments
   for next month.
   ```

## Using n8n Webhook Functions

The system includes pre-built functions to trigger n8n workflows:

### 1. Content Generation
```
trigger_content_generation(
    topic="Summer Marketing Ideas",
    content_type="blog",
    target_audience="millennials",
    tone="professional"
)
```

### 2. Schedule Social Post
```
schedule_social_media_post(
    platform="instagram",
    content="Check out our latest project! 🚀",
    schedule_time="2024-03-20T15:00:00Z",
    hashtags=["marketing", "digitalcontent", "creative"]
)
```

### 3. Process Media
```
process_media_file(
    media_url="https://example.com/video.mp4",
    operations=["resize", "compress", "watermark"],
    output_format="mp4"
)
```

### 4. Fetch Analytics
```
fetch_analytics_report(
    date_range="last_7_days",
    platforms=["instagram", "twitter", "linkedin"]
)
```

## Multi-Agent Collaboration

### Sequential Workflow

Chat with multiple personas in sequence, each building on previous work:

1. Content Strategist → Strategy
2. Creative Director → Creative execution
3. Social Media Manager → Platform distribution
4. Data Analyst → Performance tracking

### Parallel Workflow

Use workspaces to have multiple personas working simultaneously:
- Workspace 1: Content Strategist (blog strategy)
- Workspace 2: Video Producer (video script)
- Workspace 3: Social Media Manager (social posts)

### Team Collaboration

Create a group chat with multiple personas:
1. Go to Settings → Workspace
2. Enable "Multi-Agent Mode"
3. Add multiple personas to a single chat
4. They can collaborate and build on each other's responses

## Tips & Best Practices

### For Content Creation
- Always start with Content Strategist for strategy
- Use Creative Director for brand consistency checks
- Let Social Media Manager adapt for each platform
- Track performance with Data Analyst

### For Campaigns
- Involve Data Analyst early for baseline metrics
- Use Creative Director for visual cohesion
- Let each persona contribute their expertise
- Document workflows in n8n for repeatability

### For Efficiency
- Create saved prompts for common tasks
- Build n8n workflows for repetitive processes
- Use RAG (knowledge base) for brand guidelines
- Set up scheduled reports with Data Analyst

## Troubleshooting

### Cannot connect to n8n
```bash
# Check if n8n is running
docker-compose ps
# or if manual install:
ps aux | grep n8n

# Check n8n logs
docker-compose logs n8n

# Verify webhook URLs in n8n interface
```

### Persona not responding correctly
- Check the persona JSON file in `data/personas/`
- Verify the system prompt is appropriate
- Try adjusting temperature in persona config
- Clear chat history and start fresh

### Functions not working
- Restart BrandFactory: `docker-compose restart brandfactory`
- Check function syntax in `functions/n8n_integration.py`
- Verify environment variables in `.env`
- Check BrandFactory logs: `docker-compose logs -f brandfactory`

### API key issues
- Verify keys in `.env` file
- Check key permissions and quotas
- Restart services after changing `.env`:
  ```bash
  docker-compose down
  docker-compose up -d
  ```

## Next Steps

1. **Customize Personas**: Edit JSON files in `data/personas/` to match your brand voice
2. **Build n8n Workflows**: Create automation workflows for your specific needs
3. **Add Knowledge Base**: Upload brand guidelines to RAG for consistent responses
4. **Create Templates**: Build reusable prompt templates for common tasks
5. **Set Up Analytics**: Configure regular reporting workflows
6. **Train Your Team**: Share this guide with your team members

## Support Resources

- BrandFactory GitHub: https://github.com/Kesaramb/open-webui-multi-agent
- n8n Documentation: https://docs.n8n.io

## Project Structure

```
open-webui-multi-agent/
├── config.yaml              # Main configuration
├── docker-compose.yml       # Docker setup (recommended)
├── .env                     # Environment variables (create from .env.template)
├── README.md               # Full documentation
├── QUICKSTART.md           # This file
├── setup.py                # Setup script
├── start.sh                # Startup script
├── functions/
│   └── n8n_integration.py # n8n webhook functions
├── data/
│   ├── personas/          # 5 AI persona definitions
│   ├── uploads/           # Media files
│   └── rag_documents/     # Knowledge base
└── workflows/             # Workflow templates
```

---

**Ready to start creating amazing content with your AI team!** 🚀
