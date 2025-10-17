#!/bin/bash
# White-label script to remove all OpenWebUI branding
# This script runs after the container starts to replace branding in compiled frontend

set -e

echo "🏭 Applying BrandFactory white-labeling..."

# Frontend build directory
FRONTEND_DIR="/app/build"

if [ ! -d "$FRONTEND_DIR" ]; then
    echo "⚠️  Frontend directory not found, skipping white-labeling"
    exit 0
fi

# Replace all instances of "Open WebUI" with "BrandFactory"
echo "📝 Replacing 'Open WebUI' with 'BrandFactory'..."
find $FRONTEND_DIR -type f \( -name "*.js" -o -name "*.html" -o -name "*.css" \) -exec sed -i 's/Open WebUI/BrandFactory/g' {} + 2>/dev/null || true

# Replace instances with different casings
find $FRONTEND_DIR -type f \( -name "*.js" -o -name "*.html" -o -name "*.css" \) -exec sed -i 's/OpenWebUI/BrandFactory/g' {} + 2>/dev/null || true
find $FRONTEND_DIR -type f \( -name "*.js" -o -name "*.html" -o -name "*.css" \) -exec sed -i 's/open-webui/brandfactory/g' {} + 2>/dev/null || true
find $FRONTEND_DIR -type f \( -name "*.js" -o -name "*.html" -o -name "*.css" \) -exec sed -i 's/openwebui/brandfactory/g' {} + 2>/dev/null || true

# Remove "Powered by" footer text
echo "🔧 Removing 'Powered by' footer..."
find $FRONTEND_DIR -type f \( -name "*.js" -o -name "*.css" \) -exec sed -i 's/Powered by Open WebUI//g' {} + 2>/dev/null || true
find $FRONTEND_DIR -type f \( -name "*.js" -o -name "*.css" \) -exec sed -i 's/Powered by//g' {} + 2>/dev/null || true

# Replace OpenWebUI GitHub links
echo "🔗 Updating links..."
find $FRONTEND_DIR -type f -name "*.js" -exec sed -i 's|https://github.com/open-webui/open-webui|https://brandfactory.ai|g' {} + 2>/dev/null || true
find $FRONTEND_DIR -type f -name "*.js" -exec sed -i 's|https://openwebui.com|https://brandfactory.ai|g' {} + 2>/dev/null || true

# Update meta tags
echo "🏷️  Updating meta tags..."
find $FRONTEND_DIR -type f -name "*.html" -exec sed -i 's/<title>.*<\/title>/<title>BrandFactory - AI Multi-Agent Workspace<\/title>/g' {} + 2>/dev/null || true

echo "✅ White-labeling complete!"
