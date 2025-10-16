#!/bin/bash

cd /Users/mac/Projects/open-webui-multi-agent

echo "=============================================="
echo "Open WebUI Multi-Agent Workspace"
echo "=============================================="
echo ""

# Check if Open WebUI is installed
if pip show open-webui &>/dev/null; then
    echo "✓ Open WebUI is installed"
    echo ""
    echo "Starting Open WebUI with your multi-agent configuration..."
    echo ""
    echo "🤖 Available AI Personas:"
    echo "   👔 Content Strategist"
    echo "   🎨 Creative Director"
    echo "   📱 Social Media Manager"
    echo "   🎬 Video Producer"
    echo "   📊 Data Analyst"
    echo ""
    echo "🔗 Access at: http://localhost:8080"
    echo "📚 n8n at: http://localhost:5678 (if running)"
    echo ""
    echo "Press Ctrl+C to stop"
    echo "=============================================="
    echo ""

    # Load environment variables
    export $(cat .env | grep -v '^#' | xargs)

    # Start Open WebUI
    open-webui serve --host 0.0.0.0 --port 8080
else
    echo "⏳ Open WebUI is still installing..."
    echo ""
    echo "The installation is running in the background."
    echo "This can take 5-10 minutes depending on your internet speed."
    echo ""
    echo "To check status:"
    echo "  pip show open-webui"
    echo ""
    echo "Once installed, run this script again:"
    echo "  ./run.sh"
    echo ""
    echo "Or manually start:"
    echo "  open-webui serve --host 0.0.0.0 --port 8080"
    echo ""
fi
