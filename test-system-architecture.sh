#!/bin/bash
# Comprehensive System Architecture Test
# Tests the complete BrandFactory deployment using first principles

URL="https://open-webui-multi-agent.onrender.com"

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║  🔍 BrandFactory System Architecture Test                   ║"
echo "║  Using First Principles & Systems Thinking                  ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# PRINCIPLE 1: Network Layer - Can we reach the server?
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "1️⃣  NETWORK LAYER TEST"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
if curl -s -o /dev/null -w "%{http_code}" "$URL" | grep -q "200"; then
    echo "✅ HTTP 200 OK - Server is reachable"
else
    echo "❌ Server not responding"
    exit 1
fi
echo ""

# PRINCIPLE 2: Reverse Proxy - Is nginx serving requests?
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "2️⃣  REVERSE PROXY LAYER (Nginx)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
SERVER=$(curl -sI "$URL" | grep "x-render-origin-server" | cut -d' ' -f2-)
if echo "$SERVER" | grep -q "nginx"; then
    echo "✅ Nginx is serving requests: $SERVER"
else
    echo "⚠️  Server header: $SERVER"
fi
echo ""

# PRINCIPLE 3: Static Content - Landing page files
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "3️⃣  STATIC CONTENT LAYER (Landing Page)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Test landing page HTML
if curl -s "$URL" | grep -q "BrandFactory"; then
    echo "✅ Landing page HTML loaded"
else
    echo "❌ Landing page HTML missing"
fi

# Test title
if curl -s "$URL" | grep -q "<title>BrandFactory"; then
    echo "✅ Page title: BrandFactory"
else
    echo "❌ Page title incorrect"
fi

# Test Launch Workspace button
if curl -s "$URL" | grep -q "Launch Workspace"; then
    echo "✅ 'Launch Workspace' button present"
else
    echo "❌ 'Launch Workspace' button missing"
fi

# Test footer
if curl -s "$URL" | grep -q "2025 BrandFactory LLC"; then
    echo "✅ Footer: © 2025 BrandFactory LLC"
else
    echo "⚠️  Footer text may be incorrect"
fi
echo ""

# PRINCIPLE 4: Routing - Nginx proxy configuration
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "4️⃣  ROUTING LAYER (Nginx Proxy Rules)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Test /workspace route
WORKSPACE_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$URL/workspace")
if [ "$WORKSPACE_CODE" = "200" ]; then
    echo "✅ /workspace route accessible (HTTP $WORKSPACE_CODE)"
else
    echo "⚠️  /workspace returned HTTP $WORKSPACE_CODE"
fi

# Test /api route (should proxy to Open WebUI)
API_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$URL/api/config")
echo "📍 /api/config returns HTTP $API_CODE"
echo ""

# PRINCIPLE 5: Application Layer - Open WebUI backend
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "5️⃣  APPLICATION LAYER (Open WebUI on port 3000)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Check if workspace shows Open WebUI
if curl -s "$URL/workspace" | grep -q "Open WebUI\|openwebui"; then
    echo "✅ Open WebUI application running"
else
    echo "⚠️  Could not confirm Open WebUI is running"
fi
echo ""

# PRINCIPLE 6: Asset Delivery - Static assets
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "6️⃣  ASSET DELIVERY (BrandFactory Logo)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

LOGO_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$URL/brandfactory/brandfactory-logo.png")
if [ "$LOGO_CODE" = "200" ]; then
    echo "✅ BrandFactory logo accessible (HTTP $LOGO_CODE)"
else
    echo "⚠️  Logo returned HTTP $LOGO_CODE"
fi
echo ""

# SUMMARY
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 SYSTEM ARCHITECTURE SUMMARY"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Architecture Flow:"
echo "  User → Render CDN → Nginx (port 8080) → Routes:"
echo "    ├─ / → Landing Page (static HTML)"
echo "    ├─ /workspace → Open WebUI (proxy to port 3000)"
echo "    ├─ /api → Open WebUI API"
echo "    └─ /brandfactory → Static assets"
echo ""
echo "Stack:"
echo "  🌐 CDN: Cloudflare"
echo "  🔀 Reverse Proxy: Nginx 1.22.1"
echo "  🎨 Landing Page: Custom HTML/CSS"
echo "  ⚙️  Backend: Open WebUI (Uvicorn/FastAPI)"
echo "  💾 Database: SQLite (persistent disk)"
echo "  🔧 Runtime: Docker on Render.com"
echo ""
echo "URLs:"
echo "  Landing: $URL"
echo "  Workspace: $URL/workspace"
echo "  Custom Domain: https://gobrandfactory.com (if DNS configured)"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
