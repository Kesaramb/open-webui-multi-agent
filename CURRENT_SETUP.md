# 🎨 BrandFactory - Current Setup (Legal CSS Customization)

## ✅ What This Deployment Uses

**Approach:** Free, legal CSS customization
**License Required:** None - fully compliant with Open WebUI terms
**Cost:** Free forever

---

## 🖼️ What Users Will See

### Browser Tab:
```
BrandFactory (Open WebUI) - AI Multi-Agent Workspace
```

### Page Header/Title:
```
BrandFactory (Open WebUI)
```

### Branding:
- ✅ **BrandFactory theme** - Custom colors, fonts, styling
- ✅ **Your logo** - Displayed alongside Open WebUI branding
- ✅ **Custom experience** - Unique look and feel
- ℹ️ **"Open WebUI" attribution** - Remains visible (required by license)

### What This Means:
Users will see a **custom-branded experience** that clearly shows:
1. Your BrandFactory branding (primary)
2. Open WebUI attribution (as required)

This is **professional co-branding** - like "Powered by Stripe" or "Built with WordPress"

---

## 🎨 Customization Options

### Current Theme (`custom.css`)

**BrandFactory Colors:**
- Primary: `#2563eb` (Blue)
- Secondary: `#7c3aed` (Purple)
- Background: `#0f172a` (Dark)
- Accent: `#f59e0b` (Orange)

**Custom Features:**
- Gradient sidebar
- Custom button styling
- Themed chat interface
- BrandFactory footer addition

### How to Change Colors

Edit `custom.css`:

```css
:root {
  --primary-color: #YOUR_COLOR;
  --secondary-color: #YOUR_COLOR;
  --background-color: #YOUR_COLOR;
}
```

Commit and push:
```bash
git add custom.css
git commit -m "Update BrandFactory theme colors"
git push
```

Render auto-deploys in ~2 minutes.

---

## 📁 Current File Structure

```
brandfactory/
├── Dockerfile                          # Legal CSS-only approach (ACTIVE)
├── Dockerfile.white-label-enterprise-only  # Full white-label (requires license)
├── custom.css                          # Your BrandFactory theme
├── render.yaml                         # Deployment config
├── functions/                          # AI personas and n8n integration
├── static/brandfactory-logo.png       # Your logo
└── archive/
    └── white-label-scripts-enterprise-only/  # Available if you get license
```

---

## 🚀 What's Deployed

**Live URL:** https://brandfactory.onrender.com

**Features:**
- ✅ 5 AI Personas (Content Strategist, Creative Director, etc.)
- ✅ N8N workflow integration
- ✅ OpenAI & Anthropic API support
- ✅ Custom BrandFactory theme
- ✅ Your branding alongside Open WebUI
- ✅ Fully legal for commercial use

**No License Required** - This setup is 100% compliant!

---

## 🎯 Future Upgrade Path

### If You Want FULL White-Labeling Later:

**Step 1: Get Enterprise License**
```
Email: sales@openwebui.com
Subject: Enterprise White-Labeling License for BrandFactory
```

**Step 2: Switch to Full White-Label**
```bash
# Restore white-label Dockerfile
mv Dockerfile.white-label-enterprise-only Dockerfile

# Restore white-label scripts
mv archive/white-label-scripts-enterprise-only scripts

# Update and deploy
git add .
git commit -m "Switch to enterprise white-labeling"
git push
```

**Step 3: Deploy**
Render auto-deploys with complete white-labeling - zero "Open WebUI" branding!

**All scripts are ready** - just need the license!

---

## 🔧 How to Customize Further

### Add Custom Logo Placement

Edit `custom.css`:

```css
/* Add your logo to header */
.header-logo::before {
  content: '';
  background-image: url('/static/brandfactory-logo.png');
  width: 40px;
  height: 40px;
  display: inline-block;
  margin-right: 10px;
}
```

### Change Sidebar Appearance

```css
.sidebar {
  background: linear-gradient(180deg, #YOUR_COLOR 0%, #YOUR_COLOR2 100%);
}

.sidebar-item:hover {
  background: rgba(255, 255, 255, 0.1);
}
```

### Customize Chat Bubbles

```css
.user-message {
  background: var(--primary-color);
  border-radius: 20px;
}

.ai-message {
  background: var(--secondary-color);
  border-radius: 20px;
}
```

### Add Custom Fonts

```css
@import url('https://fonts.googleapis.com/css2?family=Your+Font&display=swap');

body {
  font-family: 'Your Font', sans-serif;
}
```

---

## 📊 Comparison: Current vs Enterprise

| Feature | Current (CSS) | Enterprise License |
|---------|--------------|-------------------|
| Custom Theme | ✅ | ✅ |
| Your Logo | Side-by-side | Replaces |
| Custom Colors | ✅ | ✅ |
| "BrandFactory" Name | With "(Open WebUI)" | Standalone |
| "Open WebUI" Visible | ✅ Yes (required) | ❌ Removed |
| Commercial Use | ✅ Legal | ✅ Legal |
| Cost | Free | Contact Sales |
| Our Scripts Work | Partially | Fully |

---

## 🎨 CSS Customization Best Practices

### Browser DevTools Workflow:

1. **Open BrandFactory** in Chrome/Firefox
2. **Right-click** → Inspect Element
3. **Find the CSS class** you want to style
4. **Test changes** in DevTools console
5. **Copy working CSS** to `custom.css`
6. **Commit and push** to deploy

### Example Workflow:

```bash
# 1. Test in browser DevTools
# 2. Once you like it, add to custom.css
vim custom.css

# 3. Deploy
git add custom.css
git commit -m "Update chat bubble styling"
git push

# 4. Render auto-deploys in ~2 minutes
```

---

## 🆘 Support & Resources

**Your Project:**
- GitHub: https://github.com/Kesaramb/open-webui-multi-agent
- Live: https://brandfactory.onrender.com

**Licensing Questions:**
- Read: `LICENSING_GUIDE.md`
- Enterprise: sales@openwebui.com

**CSS Help:**
- Inspect elements in browser DevTools
- Check `custom.css` for examples
- MDN CSS Reference: https://developer.mozilla.org/en-US/docs/Web/CSS

---

## ✅ Current Status Summary

**Legal:** ✅ Fully compliant, no license needed
**Commercial Use:** ✅ Allowed
**Branding:** 🟡 Co-branded (BrandFactory + Open WebUI)
**Customization:** ✅ Full CSS control
**Cost:** ✅ Free forever
**Deployed:** ✅ Live at brandfactory.onrender.com

**Your white-labeling scripts are preserved** in `archive/` - ready to use if you get enterprise license later!

---

**Questions?** Check `LICENSING_GUIDE.md` for complete licensing details.
