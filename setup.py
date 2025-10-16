"""
Setup script for Open WebUI Multi-Agent Workspace
Digital Media Company Configuration
"""

import os
import sys
import json
from pathlib import Path


def create_directory_structure():
    """Create necessary directories"""
    directories = [
        "data/personas",
        "data/uploads",
        "data/rag_documents",
        "functions",
        "workflows",
        "logs"
    ]

    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✓ Created directory: {directory}")


def create_persona_files():
    """Create persona definition files"""
    personas = [
        {
            "name": "Content Strategist",
            "role": "content_strategy",
            "avatar": "👔",
            "description": "Expert in content planning, SEO, and audience engagement",
            "system_prompt": """You are an expert content strategist for a digital media company.

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

When asked, you can trigger n8n workflows using the available functions.""",
            "model": "gpt-4",
            "temperature": 0.7,
            "capabilities": [
                "content_planning",
                "seo_optimization",
                "audience_analysis",
                "workflow_automation"
            ]
        },
        {
            "name": "Creative Director",
            "role": "creative_direction",
            "avatar": "🎨",
            "description": "Visual storytelling expert and brand consistency guardian",
            "system_prompt": """You are a creative director specializing in digital media.

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

You can coordinate with other agents and trigger media processing workflows.""",
            "model": "gpt-4",
            "temperature": 0.8,
            "capabilities": [
                "creative_concepts",
                "brand_development",
                "visual_direction",
                "campaign_planning"
            ]
        },
        {
            "name": "Social Media Manager",
            "role": "social_media",
            "avatar": "📱",
            "description": "Social media expert and community engagement specialist",
            "system_prompt": """You are a social media manager for a digital media company.

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

You can schedule posts and fetch analytics using n8n workflows.""",
            "model": "gpt-4",
            "temperature": 0.75,
            "capabilities": [
                "social_media_strategy",
                "community_management",
                "content_scheduling",
                "analytics_reporting"
            ]
        },
        {
            "name": "Video Producer",
            "role": "video_production",
            "avatar": "🎬",
            "description": "Video content expert and production coordinator",
            "system_prompt": """You are a video producer specializing in digital content.

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

You can trigger media processing workflows for video optimization.""",
            "model": "gpt-4",
            "temperature": 0.7,
            "capabilities": [
                "video_production",
                "script_writing",
                "post_production",
                "platform_optimization"
            ]
        },
        {
            "name": "Data Analyst",
            "role": "analytics",
            "avatar": "📊",
            "description": "Analytics expert and insights generator",
            "system_prompt": """You are a data analyst for a digital media company.

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

You can fetch analytics data from n8n workflows and generate comprehensive reports.""",
            "model": "gpt-4",
            "temperature": 0.6,
            "capabilities": [
                "data_analysis",
                "reporting",
                "trend_forecasting",
                "performance_optimization"
            ]
        }
    ]

    for persona in personas:
        filename = f"data/personas/{persona['role']}.json"
        with open(filename, 'w') as f:
            json.dump(persona, f, indent=2)
        print(f"✓ Created persona: {persona['name']}")


def create_env_template():
    """Create .env template file"""
    env_content = """# Open WebUI Multi-Agent Configuration
# Copy this file to .env and fill in your actual values

# n8n Configuration
N8N_BASE_URL=http://localhost:5678
N8N_API_KEY=your_n8n_api_key_here

# LLM Provider API Keys
OPENAI_API_KEY=your_openai_key_here
ANTHROPIC_API_KEY=your_anthropic_key_here

# Optional: For local models
OLLAMA_BASE_URL=http://localhost:11434

# Database Configuration (for production)
# DATABASE_URL=postgresql://user:password@localhost:5432/openwebui

# Storage Configuration
# STORAGE_TYPE=local  # or s3, azure, gcp
# STORAGE_PATH=./data/uploads

# Security
JWT_SECRET=your_secret_key_here_change_in_production

# Features
ENABLE_RAG=true
ENABLE_WEB_SEARCH=true
ENABLE_IMAGE_GENERATION=true
ENABLE_VOICE=true

# Voice Services
STT_ENGINE=whisper
TTS_ENGINE=openai  # or elevenlabs

# Optional: ElevenLabs API Key
# ELEVENLABS_API_KEY=your_elevenlabs_key_here

# Server Configuration
HOST=0.0.0.0
PORT=8080
"""

    with open('.env.template', 'w') as f:
        f.write(env_content)
    print("✓ Created .env.template file")


def create_readme():
    """Create comprehensive README"""
    readme_content = """# Open WebUI Multi-Agent Workspace
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
curl http://localhost:8080/v1/chat/completions \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer YOUR_API_KEY" \\
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
"""

    with open('README.md', 'w') as f:
        f.write(readme_content)
    print("✓ Created README.md")


def create_startup_script():
    """Create startup script"""
    script_content = """#!/bin/bash

# Open WebUI Multi-Agent Startup Script

echo "Starting Open WebUI Multi-Agent Workspace..."

# Load environment variables
if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
    echo "✓ Environment variables loaded"
else
    echo "⚠ Warning: .env file not found. Using defaults."
fi

# Check if Open WebUI is installed
if ! command -v open-webui &> /dev/null; then
    echo "✗ Open WebUI is not installed. Please run: pip install open-webui"
    exit 1
fi

# Start Open WebUI
echo "🚀 Starting Open WebUI on http://$HOST:$PORT"
echo ""
echo "Available personas:"
echo "  - Content Strategist"
echo "  - Creative Director"
echo "  - Social Media Manager"
echo "  - Video Producer"
echo "  - Data Analyst"
echo ""
echo "Press Ctrl+C to stop"
echo ""

open-webui serve --host ${HOST:-0.0.0.0} --port ${PORT:-8080}
"""

    with open('start.sh', 'w') as f:
        f.write(script_content)

    os.chmod('start.sh', 0o755)
    print("✓ Created start.sh script")


def main():
    """Main setup function"""
    print("="*60)
    print("Open WebUI Multi-Agent Workspace Setup")
    print("Digital Media Company Configuration")
    print("="*60)
    print()

    try:
        create_directory_structure()
        print()

        create_persona_files()
        print()

        create_env_template()
        create_readme()
        create_startup_script()

        print()
        print("="*60)
        print("✓ Setup completed successfully!")
        print("="*60)
        print()
        print("Next steps:")
        print("1. Copy .env.template to .env and configure your API keys")
        print("2. Review and customize config.yaml")
        print("3. Set up your n8n workflows")
        print("4. Run ./start.sh to start the system")
        print()
        print("For detailed instructions, see README.md")
        print()

    except Exception as e:
        print(f"\n✗ Setup failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
