# 📋 Open WebUI Licensing & White-Labeling Guide

## ⚠️ IMPORTANT: Licensing Requirements

Open WebUI is **MIT licensed**, but has specific requirements for commercial white-labeling.

---

## What You CAN Do (Free)

### ✅ Allowed Without Enterprise License:

1. **CSS Customization**
   - Change colors, themes, fonts
   - Add custom styles
   - Modify layout appearance

2. **Feature Additions**
   - Add custom functions/plugins
   - Integrate with your services
   - Add custom workflows

3. **Co-Branding**
   - Add your company banner in footer/secondary areas
   - Display alongside Open WebUI branding
   - Add your logo next to (not replacing) Open WebUI logo

4. **Internal Use**
   - Deploy for your company's internal use
   - Any number of employees
   - SSO/LDAP integration

5. **Open Source Contributions**
   - Fork and contribute back
   - Share improvements
   - Build plugins

---

## What You CANNOT Do (Without License)

### ❌ Requires Enterprise License:

1. **Remove/Hide Open WebUI Branding**
   - Cannot remove "Open WebUI" name
   - Cannot hide Open WebUI logo
   - Cannot replace branding completely

2. **Commercial White-Labeling**
   - Cannot sell as your own product
   - Cannot offer as white-labeled SaaS
   - Cannot brand for client-facing deployments

3. **Equal Prominence Branding**
   - Cannot display your brand with equal or greater prominence
   - Open WebUI must remain primary branding

---

## Our Current Implementation Status

### What We Built:

**Files:**
- `Dockerfile` - Full white-labeling (requires license)
- `scripts/white-label.sh` - Removes all Open WebUI branding
- `scripts/entrypoint.sh` - Custom startup process

**Current Status:**
- ✅ Technically works perfectly
- ❌ **Violates licensing for commercial use**
- 🟡 OK for personal/internal testing only

---

## Your Options

### Option 1: Get Enterprise License ⭐ RECOMMENDED

**For Commercial Use:**

**Contact:**
- Email: sales@openwebui.com
- Website: https://openwebui.com

**Request:**
- Enterprise white-labeling license
- Quote for your use case

**Benefits:**
- ✅ Legal full white-labeling
- ✅ Keep our current implementation
- ✅ Remove all Open WebUI branding
- ✅ Enterprise support
- ✅ Priority features
- ✅ Peace of mind

**Our Implementation Ready:**
- Scripts already built and tested
- Just need legal approval
- Can deploy immediately after license

---

### Option 2: Use CSS Customization Only (Free)

**For Internal Use or Open Source Projects:**

**What to Use:**
- `Dockerfile.legal-css-only` - Legal approach
- `custom.css` - Your brand theme
- Keep Open WebUI branding visible

**What You Get:**
- ✅ Custom colors and theme
- ✅ Your logo alongside Open WebUI
- ✅ Custom styling
- ✅ Free forever
- ✅ Fully legal

**What You Keep:**
- "Open WebUI" name visible
- Open WebUI logo present
- Attribution maintained

---

### Option 3: Internal/Non-Commercial Use

**If This Is NOT for:**
- Selling to clients
- Public SaaS offering
- Commercial product

**Then You Can:**
- Use current white-labeling implementation
- Deploy internally at your company
- Test and develop freely
- Switch to enterprise license before commercial launch

---

## How to Switch Approaches

### Currently Using: Full White-Labeling

```dockerfile
# Current Dockerfile
FROM ghcr.io/open-webui/open-webui:main
COPY scripts/ /app/scripts/
ENTRYPOINT ["/bin/bash", "/app/scripts/entrypoint.sh"]
```

### Switch to: Legal CSS-Only

```bash
# Rename files
mv Dockerfile Dockerfile.white-label-enterprise-only
mv Dockerfile.legal-css-only Dockerfile

# Update render.yaml to remove white-label env vars
# Keep only functional configs

# Redeploy to Render
git add .
git commit -m "Switch to legal CSS-only customization"
git push
```

---

## Comparison Table

| Feature | CSS Only (Free) | Enterprise License |
|---------|----------------|-------------------|
| Custom Colors/Theme | ✅ | ✅ |
| Custom Functions | ✅ | ✅ |
| Your Logo | Side-by-side | Replaces |
| "Open WebUI" Name | Visible | Can Remove |
| Open WebUI Logo | Visible | Can Remove |
| Commercial Use | ✅ | ✅ |
| White-Label SaaS | ❌ | ✅ |
| Client Deployments | ❌ | ✅ |
| Cost | Free | Contact Sales |
| Our Scripts Work | Partially | Fully |

---

## Recommended Action Plan

### For Commercial BrandFactory:

**Week 1:**
1. ✅ Continue using current white-label for development
2. 📧 Contact sales@openwebui.com for enterprise quote
3. 📝 Prepare your use case description

**Week 2:**
4. 💰 Get quote and approve budget
5. 📄 Sign enterprise license agreement
6. 🚀 Deploy with full white-labeling legally

**Meanwhile:**
- Keep current implementation (works perfectly)
- Mark as "Internal Beta" or "Development"
- Don't offer publicly until licensed

---

### For Internal/Non-Commercial Use:

**No Changes Needed:**
- ✅ Current implementation is fine
- ✅ Use for internal company tools
- ✅ Personal projects OK
- ⚠️ Switch to enterprise license if going commercial

---

## Legal Text to Include

### If Using CSS-Only Approach:

**Footer Text:**
```
Powered by Open WebUI | Customized by BrandFactory
```

### If Using Enterprise License:

**No attribution required** - Full white-labeling allowed

---

## Questions to Ask Sales

When contacting sales@openwebui.com, ask:

1. **Pricing:**
   - What's the cost for white-labeling license?
   - One-time or subscription?
   - Volume/user-based pricing?

2. **Scope:**
   - Can we deploy to multiple domains?
   - Unlimited users?
   - Can we resell/rebrand to clients?

3. **Technical:**
   - Any restrictions on our implementation?
   - Can we use our existing white-label scripts?
   - Support for custom features?

4. **Timeline:**
   - How quickly can we get licensed?
   - Contract terms?

---

## Bottom Line

**Our Work Isn't Wasted:**
- ✅ Scripts work perfectly and are ready
- ✅ Just need legal approval for commercial use
- ✅ Can switch between approaches easily

**Your Decision:**

**Going Commercial?** → Get enterprise license
**Internal Use Only?** → Current implementation is fine
**Not Sure Yet?** → Use CSS-only approach for now

---

**Need Help Deciding?**

Consider:
- Is this for paying customers? → Enterprise License
- Internal company tool only? → Current approach OK
- Open source project? → CSS-only approach
- Testing/POC phase? → Current approach OK, get license before launch

---

**Contact for Enterprise License:**
- 📧 Email: sales@openwebui.com
- 🌐 Website: https://openwebui.com
- 📋 Reference: "White-labeling for BrandFactory - Multi-Agent Workspace"
