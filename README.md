# 🏭 BrandFactory - AI Multi-Agent Workspace
## Enterprise-Grade AI Platform for Digital Media

**BrandFactory** is your fully configured multi-agent AI workspace designed for digital media operations.

**Live at:** https://brandfactory.onrender.com

## Features

- **5 Pre-configured AI Personas**
  - Content Strategist
  - Creative Director
  - Social Media Manager
  - Video Producer
  - Data Analyst

- **n8n Integration**
  - Content generation workflows
  - Social media scheduling
  - Analytics reporting
  - Media processing

- **Multi-Agent Collaboration**
  - Sequential and parallel workflows
  - Agent-to-agent communication
  - Workflow orchestration

## Deployment

**BrandFactory is deployed and ready to use at:**
```
https://brandfactory.onrender.com
```

No installation required! Just visit the URL and start using your AI team.

### For Development/Self-Hosting:

```bash
# Clone the repository
git clone https://github.com/Kesaramb/open-webui-multi-agent.git
cd open-webui-multi-agent

# Configure environment
cp .env.template .env
# Edit .env with your API keys

# Deploy with Docker
docker build -t brandfactory .
docker run -p 8080:8080 brandfactory
```

## n8n Integration Setup

### 1. Install n8n (if not already installed)

```bash
npm install -g n8n
# or
npx n8n
```

### 2. Create Webhooks in n8n

Create the following webhook nodes in n8n:

- `/webhook/content-gen` - Content generation workflow
- `/webhook/social-scheduler` - Social media scheduling
- `/webhook/analytics` - Analytics processing
- `/webhook/media-process` - Media file processing
- `/webhook/campaign` - Campaign management

### 3. Configure Webhook URLs

Update the `N8N_BASE_URL` in your `.env` file to point to your n8n instance.

## Using the System

### 1. Access the Web Interface

Open your browser and navigate to:
```
http://localhost:8080
```

### 2. Select a Persona

Choose from the available personas based on your task:
- Content Strategist - for content planning
- Creative Director - for creative campaigns
- Social Media Manager - for social posts
- Video Producer - for video projects
- Data Analyst - for analytics and reports

### 3. Trigger Workflows

Use the available functions to trigger n8n workflows:

```python
# Example: Generate content
trigger_content_generation(
    topic="Summer Campaign Ideas",
    content_type="blog",
    target_audience="millennials",
    tone="friendly"
)

# Example: Schedule social post
schedule_social_media_post(
    platform="instagram",
    content="Check out our latest project!",
    schedule_time="2024-03-15T14:00:00Z",
    hashtags=["marketing", "digitalcontent"]
)

# Example: Fetch analytics
fetch_analytics_report(
    date_range="last_30_days",
    platforms=["instagram", "twitter"]
)
```

## Multi-Agent Workflows

### Content Production Pipeline

1. **Content Strategist** - Generates content strategy and ideas
2. **Creative Director** - Develops creative concepts
3. **Social Media Manager** - Creates platform-specific content
4. **Data Analyst** - Tracks and reports performance

### Campaign Development

1. **Content Strategist** - Campaign strategy and goals
2. **Creative Director** - Creative execution plan
3. **Data Analyst** - Budget allocation and KPIs

### Video Production Workflow

1. **Video Producer** - Script and production plan
2. **Creative Director** - Visual direction and branding
3. **Social Media Manager** - Distribution strategy

## Project Structure

```
open-webui-multi-agent/
├── config.yaml                 # Main configuration file
├── .env                        # Environment variables
├── functions/
│   └── n8n_integration.py     # n8n webhook functions
├── data/
│   ├── personas/              # Persona definitions
│   ├── uploads/               # Uploaded files
│   └── rag_documents/         # RAG knowledge base
├── workflows/                 # Workflow definitions
└── logs/                      # Application logs
```

## Configuration

### Adding Custom Personas

1. Create a new JSON file in `data/personas/`
2. Define the persona properties:
   - name
   - role
   - description
   - system_prompt
   - model
   - capabilities

### Adding Custom Workflows

Edit `config.yaml` and add new workflows under `multi_agent.workflows`.

### Adding Custom Functions

Create new Python files in the `functions/` directory. Functions will be automatically detected by BrandFactory.

## API Access

The system exposes an OpenAI-compatible API:

```bash
curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

## Troubleshooting

### n8n Connection Issues

- Verify n8n is running: `ps aux | grep n8n`
- Check webhook URLs in n8n interface
- Verify `N8N_BASE_URL` in `.env`

### Persona Not Loading

- Check persona JSON files in `data/personas/`
- Verify file format is valid JSON
- Check logs for errors: `tail -f logs/openwebui.log`

### Function Calling Issues

- Ensure functions are in `functions/` directory
- Check Python syntax
- Restart BrandFactory after adding new functions

## Support

For issues and questions:
- BrandFactory Issues: https://github.com/Kesaramb/open-webui-multi-agent/issues
- n8n Documentation: https://docs.n8n.io

## License

BrandFactory is provided under the MIT License.
