#!/bin/bash

echo "=============================================="
echo "Open WebUI Multi-Agent Workspace Installer"
echo "=============================================="
echo ""

# Check if Docker is available
if command -v docker &> /dev/null; then
    echo "✓ Docker found!"
    echo ""
    read -p "Do you want to use Docker? (recommended) [Y/n]: " use_docker
    
    if [[ $use_docker =~ ^[Nn]$ ]]; then
        echo "Installing via pip..."
    else
        echo ""
        echo "Starting with Docker..."
        echo ""
        docker-compose up -d
        echo ""
        echo "✓ Services started!"
        echo ""
        echo "Access your workspace at:"
        echo "  - Open WebUI: http://localhost:8080"
        echo "  - n8n: http://localhost:5678 (admin/changeme123)"
        echo ""
        exit 0
    fi
else
    echo "Docker not found. Installing via pip..."
fi

# Install via pip
echo ""
echo "Installing Open WebUI (this may take 5-10 minutes)..."
echo ""

pip install --default-timeout=1000 --retries=5 open-webui

if [ $? -eq 0 ]; then
    echo ""
    echo "✓ Installation successful!"
    echo ""
    echo "To start:"
    echo "  ./start.sh"
    echo ""
    echo "Or manually:"
    echo "  open-webui serve --host 0.0.0.0 --port 8080"
    echo ""
else
    echo ""
    echo "✗ Installation failed"
    echo ""
    echo "Alternative options:"
    echo "1. Install Docker and use: docker-compose up -d"
    echo "2. Try: pip install open-webui (wait patiently)"
    echo "3. Install from source: git clone https://github.com/open-webui/open-webui.git"
    echo ""
fi
