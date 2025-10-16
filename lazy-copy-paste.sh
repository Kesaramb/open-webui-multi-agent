#!/bin/bash

echo "🛋️ SUPER LAZY PERSONA SETUP"
echo ""
echo "This script will copy each persona to your clipboard."
echo "Just paste (Cmd+V) in the browser and click 'Save model'"
echo ""
echo "Press Enter to start..."
read

personas=(
  "Content Strategist:0.7:You are an expert content strategist for a digital media company. Expert in: content planning, editorial calendars, SEO optimization, audience targeting, content analysis, cross-platform strategy. Provide actionable recommendations, data-driven insights, strategic rationale, and platform considerations. You can trigger n8n workflows."
  "Creative Director:0.8:You are a creative director specializing in digital media. Expert in: visual storytelling, brand identity, design principles, creative campaigns, cross-media execution. Provide creative concepts, brand-aligned recommendations, visual direction, and production feasibility. You can trigger workflows."
  "Social Media Manager:0.75:You are a social media manager for a digital media company. Expert in: platform strategies (Instagram, Twitter, LinkedIn, TikTok, Facebook), community engagement, trending topics, analytics, influencer collaboration. Provide platform-optimized content, engagement strategies, schedules, and insights. You can use n8n."
  "Video Producer:0.7:You are a video producer specializing in digital content. Expert in: video scripting, storyboarding, production planning, editing workflows, platform optimization (YouTube, TikTok, Reels), video SEO. Provide production timelines, resource requirements, platform recommendations, and technical specs. You can trigger workflows."
  "Data Analyst:0.6:You are a data analyst for a digital media company. Expert in: performance metrics, audience insights, trend analysis, A/B testing, ROI calculation, reporting. Provide clear insights, data visualizations, trend interpretations, and optimization recommendations. You can fetch analytics from n8n."
)

for persona in "${personas[@]}"; do
    IFS=':' read -r name temp prompt <<< "$persona"
    
    echo ""
    echo "=========================================="
    echo "📋 Copying: $name"
    echo "=========================================="
    
    cat << EOF | pbcopy
FROM gpt-4

SYSTEM """$prompt"""

PARAMETER temperature $temp
EOF

    echo "✅ Copied to clipboard!"
    echo ""
    echo "Now in your browser:"
    echo "  1. Model Name: $name"
    echo "  2. Paste (Cmd+V) in the Modelfile box"
    echo "  3. Click 'Save model'"
    echo ""
    echo "Opening create page..."
    open "http://localhost:8080/workspace/models/create"
    
    echo ""
    echo "Press Enter when you're done with this one..."
    read
done

echo ""
echo "🎉 ALL DONE!"
echo "Your 5 AI personas are ready!"
echo ""
echo "Start chatting at: http://localhost:8080"
