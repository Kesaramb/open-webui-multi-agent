# 🔑 Connecting OpenAI & Claude Models

Your API keys are already in the `.env` file. Just add them to BrandFactory interface:

## Quick Setup (2 minutes)

### 1. Open Settings

Go to: http://localhost:8080

Click: **Profile Icon** (top right) → **Settings** → **Connections**

---

### 2. Add OpenAI

In the **OpenAI** section:

1. Click **"+"** or **"Add Connection"**
2. **API Key:** Paste your OpenAI API key
   ```
   sk-proj-YOUR_OPENAI_API_KEY_HERE
   ```
   (Get your key from: https://platform.openai.com/api-keys)
3. **Click "Save"**

✅ **OpenAI models are now connected!**

Available models:
- GPT-4 (if you have access)
- GPT-4 Turbo
- GPT-3.5 Turbo
- And all other OpenAI models

---

### 3. Add Anthropic (Claude) - Optional

In the **Anthropic** section:

1. Click **"+"** or **"Add Connection"**
2. **API Key:** Paste your Anthropic API key
   ```
   sk-ant-YOUR_ANTHROPIC_API_KEY_HERE
   ```
   (Get your key from: https://console.anthropic.com/settings/keys)
3. **Click "Save"**

✅ **Claude models are now connected!**

Available models:
- Claude 3.5 Sonnet
- Claude 3 Opus
- Claude 3 Haiku

---

## ✅ That's It!

Your personas are already configured to use **GPT-4**.

When you chat with any persona, it will automatically use OpenAI's models!

---

## 🎯 How to Use Different Models

### Option 1: Use Your Personas (Recommended)

Just select a persona from the model dropdown and start chatting!

The persona's personality + GPT-4's power = 🔥

---

### Option 2: Switch Between Models

In any chat:
1. Click the **model dropdown** (top of chat)
2. Select any model:
   - Your personas (Content Strategist, etc.)
   - GPT-4
   - GPT-3.5 Turbo
   - Claude 3.5 Sonnet
   - Any other connected model

---

### Option 3: Update Personas to Use Different Models

To change which model a persona uses:

1. Go to: **Workspace** → **Models**
2. Find your persona (e.g., "Content Strategist")
3. Click the **edit icon**
4. Change the first line from:
   ```
   FROM gpt-4
   ```
   To any model you want:
   ```
   FROM gpt-3.5-turbo
   FROM claude-3-5-sonnet-20241022
   FROM gpt-4-turbo
   ```
5. Click **"Save"**

---

## 🚀 Test It Out!

1. Go to http://localhost:8080
2. Start a new chat
3. Select "Content Strategist" from the model dropdown
4. Ask: "Help me create a content strategy"
5. Watch GPT-4 respond with your custom persona! 🎉

---

## 💡 Tips

- **GPT-4** - Best for complex tasks, creativity
- **GPT-3.5 Turbo** - Faster, cheaper, good for simple tasks
- **Claude 3.5 Sonnet** - Great for writing, analysis
- **Your Personas** - Pre-configured experts for specific tasks!

---

## 🔍 Verify It's Working

After adding your API keys:

1. Go to **Settings** → **Connections**
2. You should see:
   - ✅ OpenAI (Connected)
   - ✅ Anthropic (Connected)

3. Go to a new chat
4. Click the model dropdown
5. You should see all available models + your personas

---

**Your AI team is now powered by OpenAI and Claude!** 🚀
