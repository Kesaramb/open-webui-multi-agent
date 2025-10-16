#!/bin/bash

echo "Checking installation status..."
echo ""

if pip show open-webui &>/dev/null; then
    echo "✅ Open WebUI is INSTALLED!"
    echo ""
    echo "Version: $(pip show open-webui | grep Version | awk '{print $2}')"
    echo ""
    echo "🚀 Ready to start! Run:"
    echo "   ./run.sh"
    echo ""
    echo "Or manually:"
    echo "   cd /Users/mac/Projects/open-webui-multi-agent"
    echo "   open-webui serve --host 0.0.0.0 --port 8080"
else
    echo "⏳ Installation still in progress..."
    echo ""

    # Check if pip process is running
    if ps aux | grep -v grep | grep "pip install.*open-webui" > /dev/null; then
        echo "✓ Background installation is active"
        echo ""
        echo "This typically takes 5-10 minutes."
        echo "Check again in a few minutes by running: ./check-status.sh"
    else
        echo "⚠️  No installation process detected"
        echo ""
        echo "Start installation with:"
        echo "   pip install open-webui"
        echo ""
        echo "Or use the installer:"
        echo "   ./INSTALL.sh"
    fi
fi

echo ""
