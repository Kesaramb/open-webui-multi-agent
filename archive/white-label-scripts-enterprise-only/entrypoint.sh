#!/bin/bash
# Custom entrypoint for BrandFactory
# Applies white-labeling before starting Open WebUI

set -e

echo "🏭 BrandFactory Starting..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Run white-labeling script
if [ -f "/app/scripts/white-label.sh" ]; then
    echo "🎨 Applying white-label customizations..."
    bash /app/scripts/white-label.sh
else
    echo "⚠️  White-label script not found, skipping..."
fi

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🚀 Starting BrandFactory server..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Start Open WebUI with proper command
exec bash /app/backend/start.sh
