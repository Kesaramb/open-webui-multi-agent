# BrandFactory with Custom Landing Page
# Legal approach: Custom landing page + Open WebUI (keeps branding)

FROM ghcr.io/open-webui/open-webui:main

# Switch to root for installations
USER root

# Install nginx for reverse proxy (Open WebUI uses Debian/Ubuntu base)
RUN apt-get update && \
    apt-get install -y --no-install-recommends nginx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy custom functions
COPY --chown=1000:1000 functions/ /app/backend/functions/

# Copy BrandFactory static assets
COPY --chown=1000:1000 static/ /app/backend/static/brandfactory/

# Copy landing page
COPY --chown=1000:1000 landing/ /app/landing/

# Copy nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Copy startup script
COPY scripts/start-with-landing.sh /app/scripts/start-with-landing.sh
RUN chmod +x /app/scripts/start-with-landing.sh

# Create nginx directories and set permissions
RUN mkdir -p /var/log/nginx /var/lib/nginx /var/cache/nginx /run && \
    chown -R 1000:1000 /var/log/nginx /var/lib/nginx /var/cache/nginx /run && \
    touch /run/nginx.pid && \
    chown 1000:1000 /run/nginx.pid

# Switch back to non-root user
USER 1000:1000

# Expose port 8080 (nginx listens here, proxies to Open WebUI on 3000)
EXPOSE 8080

# Use custom startup script
ENTRYPOINT ["/bin/bash", "/app/scripts/start-with-landing.sh"]
