# 🎨 Complete White-Labeling Guide for BrandFactory

This document explains how we've completely removed all OpenWebUI branding and replaced it with BrandFactory.

---

## 🚫 Problem with Default Open WebUI

By default, Open WebUI shows branding in multiple places:
- ❌ "Open WebUI" in page titles
- ❌ "Powered by Open WebUI" in footers
- ❌ "(Open WebUI)" appended to custom names
- ❌ OpenWebUI logos and favicons
- ❌ Links to github.com/open-webui
- ❌ References in meta tags and HTML

**Users would know it's Open WebUI** - Not good for white-labeling!

---

## ✅ Our Complete White-Label Solution

### 1. **Custom Entrypoint Script**
`scripts/entrypoint.sh` runs on container startup and:
- Executes white-labeling modifications BEFORE the server starts
- Ensures every deploy has BrandFactory branding

### 2. **White-Label Script**
`scripts/white-label.sh` performs:
- Text replacement in compiled frontend files
- Removes "Open WebUI" → Replaces with "BrandFactory"
- Removes "Powered by" footers
- Updates links and meta tags
- Changes all casings (OpenWebUI, open-webui, etc.)

### 3. **Environment Variables**
```yaml
WEBUI_NAME: "BrandFactory"
WEBUI_URL: "https://brandfactory.onrender.com"
WEBUI_FAVICON_URL: "/brandfactory/brandfactory-logo.png"
```

### 4. **Custom Assets**
- **Logo:** `static/brandfactory-logo.png`
- **Favicon:** Served from static directory
- **Custom CSS:** (Can be added via admin panel after deployment)

---

## 📋 What Gets Replaced

### Text Replacements:
| Original | Replaced With |
|----------|---------------|
| `Open WebUI` | `BrandFactory` |
| `OpenWebUI` | `BrandFactory` |
| `open-webui` | `brandfactory` |
| `openwebui` | `brandfactory` |
| `Powered by Open WebUI` | *(removed)* |
| `Powered by` | *(removed)* |

### Link Replacements:
| Original | Replaced With |
|----------|---------------|
| `https://github.com/open-webui/open-webui` | `https://brandfactory.ai` |
| `https://openwebui.com` | `https://brandfactory.ai` |

### Meta Tags:
| Original | Replaced With |
|----------|---------------|
| `<title>Open WebUI</title>` | `<title>BrandFactory - AI Multi-Agent Workspace</title>` |

---

## 🔍 How It Works

### Build Process:
```
1. Docker builds image from ghcr.io/open-webui/open-webui:main
   ↓
2. Copies scripts/white-label.sh and scripts/entrypoint.sh
   ↓
3. Sets ENTRYPOINT to scripts/entrypoint.sh
```

### Runtime Process (Every Container Start):
```
1. Container starts
   ↓
2. entrypoint.sh executes
   ↓
3. white-label.sh runs:
      - Scans /app/build directory (compiled frontend)
      - Replaces ALL instances of OpenWebUI branding
      - Updates meta tags, titles, links
   ↓
4. Open WebUI server starts
   ↓
5. Users see ONLY "BrandFactory" branding ✅
```

---

## 🛠️ Files Modified

### Docker Configuration:
```dockerfile
# Dockerfile
- Installs sed/bash for text replacement
- Copies scripts/ directory
- Sets custom ENTRYPOINT
```

### Scripts:
```bash
scripts/
├── entrypoint.sh      # Container startup script
└── white-label.sh     # Branding replacement logic
```

### Configuration:
```yaml
# render.yaml
- WEBUI_NAME: "BrandFactory"
- WEBUI_URL: Custom URL
- WEBUI_FAVICON_URL: Custom favicon
```

---

## 🎯 What Users Will See

### ✅ After White-Labeling:

**Browser Tab:**
```
BrandFactory - AI Multi-Agent Workspace
[Your Logo Favicon]
```

**Page Title:**
```
BrandFactory
```

**Footer:**
```
© 2024 BrandFactory
(No "Powered by Open WebUI" text)
```

**Sidebar/Header:**
```
🏭 BrandFactory
```

**Links:**
```
All links point to brandfactory.ai
(No github.com/open-webui links)
```

---

## 🔧 Advanced Customization

### Add More Replacements:

Edit `scripts/white-label.sh` and add:

```bash
# Example: Replace additional text
find $FRONTEND_DIR -type f -name "*.js" -exec sed -i 's/OLD_TEXT/NEW_TEXT/g' {} +
```

### Custom CSS Overrides:

After deployment, as admin:
1. Go to **Settings** → **Admin Panel** → **Interface**
2. Add custom CSS:
```css
/* Hide any remaining OpenWebUI references */
[data-brand*="openwebui"],
[class*="openwebui"] {
    display: none !important;
}

/* Custom branding colors */
:root {
    --primary-color: #YOUR_BRAND_COLOR;
}
```

### Update Logo:

Replace `static/brandfactory-logo.png` with your logo:
```bash
# Recommended size: 512x512px PNG with transparency
cp your-new-logo.png static/brandfactory-logo.png
git add static/brandfactory-logo.png
git commit -m "Update logo"
git push
```

---

## 🧪 Testing the White-Label

### Local Testing:

```bash
# Build and run locally
docker build -t brandfactory .
docker run -p 8080:8080 brandfactory

# Open http://localhost:8080
# Verify: No "Open WebUI" text anywhere
```

### Check for Branding Leaks:

```bash
# SSH into running container
docker exec -it container_id bash

# Search for remaining "Open WebUI" references
grep -r "Open WebUI" /app/build/ 2>/dev/null || echo "✅ No OpenWebUI branding found!"
```

---

## 📊 Branding Checklist

After deployment, verify these areas:

- [ ] **Browser tab title** shows "BrandFactory"
- [ ] **Favicon** is your custom logo
- [ ] **Login page** shows BrandFactory
- [ ] **Sidebar** has no OpenWebUI references
- [ ] **Footer** has no "Powered by" text
- [ ] **Settings pages** show BrandFactory
- [ ] **Error pages** show BrandFactory
- [ ] **Email templates** (if using auth) show BrandFactory
- [ ] **API documentation** shows BrandFactory
- [ ] **External links** don't point to openwebui.com

---

## 🚨 Important Notes

### Persistence:
- White-labeling happens **every container start**
- Changes are NOT permanent (reapplied on restart)
- This ensures consistency across deployments

### Updates:
- When Open WebUI updates, white-labeling automatically reapplies
- No manual intervention needed
- Always up-to-date with latest OpenWebUI features

### Licensing:
- Open WebUI is MIT licensed
- White-labeling is permitted
- Attribution not legally required (but appreciated!)
- Our implementation complies with MIT license terms

---

## 🔄 Updating BrandFactory

### Method 1: Via Git

```bash
# Update configuration
vim render.yaml  # Edit branding
vim scripts/white-label.sh  # Edit replacements

# Commit and push
git add .
git commit -m "Update branding"
git push

# Render auto-deploys
```

### Method 2: Via Render Dashboard

1. Go to Render dashboard
2. Environment variables → Edit
3. Update `WEBUI_NAME` or `WEBUI_URL`
4. Save → Auto redeploys

---

## 🎓 Advanced: Fork for Custom Frontend

If you need MORE customization (custom UI components, layouts):

### Option 1: Fork Open WebUI
```bash
git clone https://github.com/open-webui/open-webui
cd open-webui
# Make frontend changes in src/
npm run build
# Build custom Docker image
```

### Option 2: Use This Solution (Recommended)
- ✅ Easier to maintain
- ✅ Automatic updates from upstream
- ✅ No frontend build knowledge needed
- ✅ Works for 99% of white-labeling needs

---

## 🏆 Result

**Your users will NEVER know this is Open WebUI.**

They will see a completely branded "BrandFactory" experience with:
- Custom name throughout
- Custom logo and favicon
- No attribution to Open WebUI
- Professional, white-labeled interface
- Your branding in all touchpoints

---

## 📞 Troubleshooting

### "Still seeing OpenWebUI text"

1. **Check scripts ran:**
   ```bash
   # In Render logs, look for:
   "🎨 Applying white-label customizations..."
   "✅ White-labeling complete!"
   ```

2. **Check frontend directory:**
   ```bash
   # SSH to container
   ls -la /app/build/
   ```

3. **Manual test:**
   ```bash
   # Run white-label script manually
   bash /app/scripts/white-label.sh
   ```

### "Script not executing"

- Verify `/app/scripts/` exists
- Check file permissions: `ls -la /app/scripts/`
- Check entrypoint: `cat /proc/1/cmdline`

### "Errors in logs"

- Check sed is installed: `which sed`
- Check bash is installed: `which bash`
- Verify files are readable: `ls -la /app/build/`

---

**Complete white-labeling achieved! 🎨✨**

*No user will discover this is Open WebUI*
