# Simple Flask-based speed test service

This application provides basic endpoints for checking network latency,
download, and upload speeds. By default the server enforces HTTPS: any HTTP
request is redirected to the HTTPS version of the URL.

## Running

1. **Install dependencies** (Flask is the only requirement):

   ```bash
   pip install flask
   ```

2. **Provide certificate and key files** by exporting their paths. When both
   variables are defined the application automatically listens on port `443` and
   serves requests via HTTPS:

   ```bash
   export CERT_FILE=/path/to/cert.pem
   export KEY_FILE=/path/to/key.pem
   python app.py
   ```

   If the variables are not set the app falls back to HTTP on port `80`.

All HTTP requests are redirected to HTTPS, allowing the service to respond only
over secure connections.

