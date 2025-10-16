# Open WebUI Multi-Agent Workspace
## Digital Media Company Setup

This is a fully configured multi-agent workspace using Open WebUI for digital media operations.

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

## Installation

### 1. Install Open WebUI

```bash
pip install open-webui
```

### 2. Configure Environment

```bash
cp .env.template .env
# Edit .env with your actual API keys and configuration
```

### 3. Start Open WebUI

```bash
cd /Users/mac/Projects/open-webui-multi-agent
open-webui serve --host 0.0.0.0 --port 8080
```

Or with custom config:

```bash
OPEN_WEBUI_CONFIG=config.yaml open-webui serve
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

Create new Python files in the `functions/` directory. Functions will be automatically detected by Open WebUI.

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
- Restart Open WebUI after adding new functions

## Support

For issues and questions:
- Open WebUI Docs: https://docs.openwebui.com
- Open WebUI GitHub: https://github.com/open-webui/open-webui
- n8n Documentation: https://docs.n8n.io

## License

This configuration is provided as-is for use with Open WebUI.
