# Use official Open WebUI image
FROM ghcr.io/open-webui/open-webui:main

# Install sed for text replacement (might not be in base image)
USER root
RUN apk add --no-cache sed bash || apt-get update && apt-get install -y sed bash || yum install -y sed bash || true

# Copy custom functions to the functions directory
COPY --chown=1000:1000 functions/ /app/backend/functions/

# Copy BrandFactory static assets (logo, branding)
COPY --chown=1000:1000 static/ /app/backend/static/brandfactory/

# Copy white-labeling scripts
COPY --chown=1000:1000 scripts/ /app/scripts/
RUN chmod +x /app/scripts/*.sh

# Switch back to non-root user
USER 1000:1000

# Use custom entrypoint that applies white-labeling
ENTRYPOINT ["/bin/bash", "/app/scripts/entrypoint.sh"]
