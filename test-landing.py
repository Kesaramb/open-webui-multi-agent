#!/usr/bin/env python3
"""
Simple test server to demonstrate the landing page approach
- Landing page on http://localhost:8081
- Proxies /workspace to http://localhost:8080 (your running Open WebUI)
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import urllib.request
import urllib.error
import os

class LandingPageHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Root path - serve landing page
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            with open('landing/index.html', 'rb') as f:
                self.wfile.write(f.read())

        # Workspace path - proxy to Open WebUI
        elif self.path.startswith('/workspace'):
            # In real deployment, nginx would proxy this
            # For demo, just redirect
            self.send_response(302)
            self.send_header('Location', 'http://localhost:8080')
            self.end_headers()

        # BrandFactory static files
        elif self.path.startswith('/brandfactory/'):
            try:
                # Remove /brandfactory/ prefix
                file_path = 'static' + self.path.replace('/brandfactory', '')

                if os.path.exists(file_path):
                    self.send_response(200)
                    if file_path.endswith('.png'):
                        self.send_header('Content-type', 'image/png')
                    self.end_headers()

                    with open(file_path, 'rb') as f:
                        self.wfile.write(f.read())
                else:
                    self.send_error(404, 'File not found')
            except Exception as e:
                self.send_error(500, str(e))

        else:
            self.send_error(404, 'Not found')

    def log_message(self, format, *args):
        print(f"[Landing Page Server] {format % args}")

if __name__ == '__main__':
    port = 8081
    server = HTTPServer(('localhost', port), LandingPageHandler)

    print("╔══════════════════════════════════════════════════════════╗")
    print("║  🎨 BrandFactory Landing Page Demo Server               ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print("")
    print("📍 Landing Page:  http://localhost:8081")
    print("📍 Workspace:     http://localhost:8081/workspace → redirects to :8080")
    print("📍 Direct WebUI:  http://localhost:8080")
    print("")
    print("✨ This demonstrates how users will experience BrandFactory:")
    print("   1. First see the branded landing page (:8081)")
    print("   2. Click 'Launch Workspace' → redirected to Open WebUI (:8080)")
    print("")
    print("Press Ctrl+C to stop the server")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\n🛑 Stopping server...")
        server.shutdown()
