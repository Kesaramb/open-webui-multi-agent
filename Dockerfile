# Use official Open WebUI image
FROM ghcr.io/open-webui/open-webui:main

# Copy custom functions to the functions directory
COPY --chown=1000:1000 functions/ /app/backend/functions/

# The base image already exposes port 8080 and has correct CMD
# No need to override anything else
