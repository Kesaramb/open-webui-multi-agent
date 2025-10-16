#!/bin/bash

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
