#!/bin/bash
# Simple deployment checker for BrandFactory landing page

URL="https://open-webui-multi-agent.onrender.com"

echo "╔══════════════════════════════════════════════════════════╗"
echo "║  🔍 BrandFactory Deployment Checker                     ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""
echo "🌐 URL: $URL"
echo "⏰ Time: $(date '+%H:%M:%S %Z')"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Check if landing page is live
if curl -s "$URL" | grep -q "AI-Powered Multi-Agent Workspace"; then
    echo "✅ SUCCESS! BrandFactory landing page is LIVE!"
    echo ""
    echo "Landing page features detected:"
    curl -s "$URL" | grep -o "<h1>.*</h1>" | sed 's/<[^>]*>//g'
    echo ""
    echo "Footer check:"
    curl -s "$URL" | grep -o "BrandFactory LLC"
    echo ""
    echo "🎉 Deployment complete!"
else
    echo "⏳ Still deploying... (showing Open WebUI currently)"
    echo ""
    echo "Current status:"
    curl -sI "$URL" | grep -E "(HTTP|date|x-render)" | head -3
    echo ""
    echo "💡 Check Render dashboard: https://dashboard.render.com"
    echo "   Look for 'brandfactory' or 'open-webui-multi-agent' service"
    echo ""
    echo "Expected deployment time: 7-10 minutes from git push"
fi

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
