# How to Remove "(Open WebUI)" Suffix

The WEBUI_NAME environment variable has been set to "BrandFactory OS", but Open WebUI automatically adds "(Open WebUI)" suffix.

## Current Display
- Shows: **BrandFactory OS (Open WebUI)**
- Desired: **BrandFactory OS**

## Solution Options

### Option 1: Admin Panel Configuration (After Deployment)
1. Log in to your Open WebUI instance at `/workspace`
2. Go to **Admin Panel** (gear icon)
3. Navigate to **Settings** → **General**
4. Find **"App Name"** or **"WebUI Name"** field
5. Change it to just **"BrandFactory OS"** (without any suffix)
6. Save changes

This should override the environment variable and remove the suffix.

### Option 2: JavaScript Client-Side Fix (Already Prepared)
A custom JavaScript file has been created at `/static/custom-branding.js` that:
- Removes "(Open WebUI)" text from the browser display
- Updates the document title
- Runs automatically on page load

To activate this:
1. The script is already copied to `/app/backend/static/custom-branding.js`
2. You need to inject it into the HTML - this can be done via:
   - Admin Panel → Settings → Custom HTML
   - Or by modifying the index.html template

### Option 3: Accept the Current Branding
The current display "BrandFactory OS (Open WebUI)" is:
- Legally compliant with Open WebUI's MIT license
- Transparent about the underlying technology
- A good compromise between custom branding and attribution

## Recommended Approach
Try **Option 1** first (Admin Panel), as it's the officially supported method and doesn't require code modifications.

If that doesn't work, we can implement Option 2 by injecting the custom JavaScript.

---

*Note: Complete removal of "Open WebUI" branding may violate the project's license unless your deployment has <50 users/month or you have an enterprise license.*
