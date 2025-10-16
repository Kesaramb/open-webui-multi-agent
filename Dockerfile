# Use official Open WebUI image
FROM ghcr.io/open-webui/open-webui:main

# Set working directory
WORKDIR /app

# Copy custom functions
COPY functions/ /app/backend/functions/

# Expose port
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8080/health || exit 1

# Start Open WebUI with the correct command
CMD ["bash", "-c", "open-webui serve"]
