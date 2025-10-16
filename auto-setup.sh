#!/bin/bash

echo "=================================================="
echo "🤖 AUTOMATIC SETUP FOR LAZY PEOPLE 😎"
echo "=================================================="
echo ""

# Configuration
API_URL="http://localhost:8080"
ADMIN_EMAIL="admin@yourdomain.com"
ADMIN_PASSWORD="changeme123"
ADMIN_NAME="Admin"

echo "Step 1: Creating admin account..."

# Create admin account
SIGNUP_RESPONSE=$(curl -s -X POST "${API_URL}/api/v1/auths/signup" \
  -H "Content-Type: application/json" \
  -d "{
    \"email\": \"${ADMIN_EMAIL}\",
    \"password\": \"${ADMIN_PASSWORD}\",
    \"name\": \"${ADMIN_NAME}\"
  }")

echo "$SIGNUP_RESPONSE"

# Extract token
TOKEN=$(echo "$SIGNUP_RESPONSE" | grep -o '"token":"[^"]*' | cut -d'"' -f4)

if [ -z "$TOKEN" ]; then
    echo "⚠️  Could not create account automatically."
    echo "You'll need to sign up manually at http://localhost:8080"
    echo ""
    echo "Use these credentials:"
    echo "  Email: ${ADMIN_EMAIL}"
    echo "  Password: ${ADMIN_PASSWORD}"
    echo ""
    exit 1
fi

echo "✓ Admin account created!"
echo "  Email: ${ADMIN_EMAIL}"
echo "  Password: ${ADMIN_PASSWORD}"
echo ""

echo "Step 2: Adding n8n webhook functions..."

# Read the function file
FUNCTION_CODE=$(cat functions/n8n_integration.py)

# Add function
FUNCTION_RESPONSE=$(curl -s -X POST "${API_URL}/api/v1/functions/create" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${TOKEN}" \
  -d "{
    \"name\": \"n8n_integration\",
    \"description\": \"n8n webhook integration for automated workflows\",
    \"content\": $(echo "$FUNCTION_CODE" | jq -Rs .)
  }")

echo "✓ Functions added!"
echo ""

echo "Step 3: Creating AI personas..."

# Array of personas
declare -a PERSONAS=(
  "Content Strategist:0.7:You are an expert content strategist for a digital media company. Your expertise: content planning, editorial calendars, SEO optimization, audience targeting, content performance analysis, cross-platform strategy. Provide actionable recommendations, data-driven insights, clear strategic rationale, and platform-specific considerations. You can trigger n8n workflows."
  "Creative Director:0.8:You are a creative director specializing in digital media. Your expertise: visual storytelling, brand identity, design principles, creative campaign development, cross-media execution. Provide innovative creative concepts, brand-aligned recommendations, visual direction guidance, and production feasibility assessments. You can trigger media processing workflows."
  "Social Media Manager:0.75:You are a social media manager for a digital media company. Your expertise: platform-specific strategies (Instagram, Twitter, LinkedIn, TikTok, Facebook), community engagement, trending topics, analytics reporting, influencer collaboration. Provide platform-optimized content, engagement strategies, posting schedules, and performance insights. You can schedule posts and fetch analytics using n8n."
  "Video Producer:0.7:You are a video producer specializing in digital content. Your expertise: video scripting, storyboarding, production planning, editing workflows, platform optimization (YouTube, TikTok, Reels), video SEO. Provide detailed production timelines, resource requirements, platform-specific recommendations, and technical specifications. You can trigger media processing workflows."
  "Data Analyst:0.6:You are a data analyst for a digital media company. Your expertise: performance metrics analysis, audience insights, trend analysis, A/B testing, ROI calculation, reporting. Provide clear actionable insights, data visualizations, trend interpretations, and optimization recommendations. You can fetch analytics data from n8n workflows."
)

for persona in "${PERSONAS[@]}"; do
    IFS=':' read -r name temp prompt <<< "$persona"

    echo "Creating: $name..."

    MODELFILE="FROM gpt-4\n\nSYSTEM \"\"\"${prompt}\"\"\"\n\nPARAMETER temperature ${temp}"

    curl -s -X POST "${API_URL}/api/v1/models/create" \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer ${TOKEN}" \
      -d "{
        \"name\": \"${name}\",
        \"meta\": {
          \"description\": \"${name} for digital media company\"
        },
        \"params\": {},
        \"modelfile\": \"${MODELFILE}\"
      }" > /dev/null

    echo "✓ $name created!"
done

echo ""
echo "=================================================="
echo "🎉 SETUP COMPLETE!"
echo "=================================================="
echo ""
echo "Your credentials:"
echo "  URL: http://localhost:8080"
echo "  Email: ${ADMIN_EMAIL}"
echo "  Password: ${ADMIN_PASSWORD}"
echo ""
echo "Your AI Team:"
echo "  👔 Content Strategist"
echo "  🎨 Creative Director"
echo "  📱 Social Media Manager"
echo "  🎬 Video Producer"
echo "  📊 Data Analyst"
echo ""
echo "✨ Just open http://localhost:8080 and login!"
echo ""
