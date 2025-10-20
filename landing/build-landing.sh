#!/bin/bash
# Build React landing page for production

set -e

echo "🔨 Building BrandFactory Landing Page..."
cd /app/landing/react-landing

# Install dependencies
echo "📦 Installing dependencies..."
npm ci --silent

# Build for production
echo "⚡ Building production bundle..."
npm run build

echo "✅ Landing page built successfully!"
echo "📂 Output: /app/landing/dist"
