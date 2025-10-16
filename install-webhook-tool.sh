#!/bin/bash

echo "🔗 WEBHOOK TOOL INSTALLER FOR OPEN WEBUI"
echo "========================================"
echo ""

# Copy webhook manager to clipboard
echo "Copying webhook_manager.py to clipboard..."
cat /Users/mac/Projects/open-webui-multi-agent/functions/webhook_manager.py | pbcopy

echo "✅ Webhook manager copied to clipboard!"
echo ""
echo "📋 Now follow these steps:"
echo ""
echo "1. Open http://localhost:8080 in your browser"
echo "2. Click profile icon → Settings → Admin Panel → Functions"
echo "3. Click the '+' button"
echo "4. Paste (Cmd+V) the code"
echo "5. Click 'Save'"
echo ""
echo "Opening Open WebUI Admin Panel..."
open "http://localhost:8080/admin/functions"

echo ""
echo "Press Enter when you're done adding the function..."
read

echo ""
echo "✅ Great! Now let's set up n8n (optional)"
echo ""
echo "Would you like to install n8n? (y/n)"
read -r install_n8n

if [[ "$install_n8n" == "y" || "$install_n8n" == "Y" ]]; then
    echo ""
    echo "Installing n8n..."
    echo ""
    echo "Running: npx n8n"
    echo ""
    echo "n8n will start at: http://localhost:5678"
    echo ""
    echo "To import example workflows:"
    echo "  1. Open http://localhost:5678"
    echo "  2. Go to Workflows → Import from File"
    echo "  3. Select: /Users/mac/Projects/open-webui-multi-agent/workflows/n8n-complete-workflows.json"
    echo ""
    echo "Starting n8n in 3 seconds..."
    sleep 3
    npx n8n
else
    echo ""
    echo "Skipping n8n installation."
    echo ""
    echo "You can install it later with: npx n8n"
fi

echo ""
echo "=========================================="
echo "✅ SETUP COMPLETE!"
echo "=========================================="
echo ""
echo "Your AI personas can now use webhooks!"
echo ""
echo "Try asking your Content Strategist:"
echo '  "Create a blog post about AI trends"'
echo ""
echo "📖 Full guide: WEBHOOK_GUIDE.md"
echo ""
