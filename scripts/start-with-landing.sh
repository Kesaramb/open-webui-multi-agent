#!/bin/bash
# Startup script for BrandFactory with custom landing page
# Starts both nginx (landing page + proxy) and Open WebUI

set -e

echo "🏭 BrandFactory Starting..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Set required environment variables for Open WebUI
export PORT=3000
export HOST=127.0.0.1

# Generate WEBUI_SECRET_KEY if not set (Render sets this via render.yaml)
if [ -z "$WEBUI_SECRET_KEY" ]; then
    echo "⚠️  WEBUI_SECRET_KEY not set, generating random key..."
    export WEBUI_SECRET_KEY=$(python3 -c "import secrets; print(secrets.token_hex(32))")
fi

# Set DATA_DIR (directory created in Dockerfile with correct permissions)
export DATA_DIR=${DATA_DIR:-/app/backend/data}
echo "📂 Using data directory: $DATA_DIR"

# Start Open WebUI on port 3000 in background
echo "🚀 Starting Open WebUI backend on port 3000..."
bash /app/backend/start.sh &
OPENWEBUI_PID=$!

# Wait for Open WebUI to be ready
echo "⏳ Waiting for Open WebUI to start..."
for i in {1..30}; do
    if curl -s http://127.0.0.1:3000/health > /dev/null 2>&1; then
        echo "✅ Open WebUI is ready!"
        break
    fi
    if [ $i -eq 30 ]; then
        echo "❌ Open WebUI failed to start"
        exit 1
    fi
    sleep 2
done

# Start nginx on port 8080
echo "🌐 Starting nginx reverse proxy on port 8080..."
nginx -g 'daemon off;' &
NGINX_PID=$!

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ BrandFactory is running!"
echo ""
echo "📍 Landing Page: http://localhost:8080"
echo "📍 Workspace: http://localhost:8080/workspace"
echo "📍 API: http://localhost:8080/api"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Function to handle shutdown
shutdown() {
    echo ""
    echo "🛑 Shutting down BrandFactory..."
    kill $NGINX_PID 2>/dev/null || true
    kill $OPENWEBUI_PID 2>/dev/null || true
    exit 0
}

# Trap SIGTERM and SIGINT
trap shutdown SIGTERM SIGINT

# Wait for either process to exit
wait -n

# If we get here, one process died - shut down the other
shutdown
