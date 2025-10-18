# Legal CSS Customization Approach (No White-Labeling)
# This keeps Open WebUI branding while adding your custom theme

FROM ghcr.io/open-webui/open-webui:main

# Copy custom functions
COPY --chown=1000:1000 functions/ /app/backend/functions/

# Copy BrandFactory static assets (logo for co-branding)
COPY --chown=1000:1000 static/ /app/backend/static/brandfactory/

# Copy custom CSS theme
COPY --chown=1000:1000 custom.css /app/build/static/custom.css

# Note: This approach maintains Open WebUI branding as required by the license
# Your BrandFactory branding appears alongside (not replacing) Open WebUI
