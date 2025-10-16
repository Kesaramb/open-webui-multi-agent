# Use official Open WebUI image
FROM ghcr.io/open-webui/open-webui:main

# Set working directory
WORKDIR /app

# Copy custom functions
COPY functions/ /app/backend/functions/

# Copy configuration files
COPY config.yaml /app/backend/data/config.yaml 2>/dev/null || true

# Expose port
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8080/health || exit 1

# Start Open WebUI
CMD ["bash", "start.sh"]
