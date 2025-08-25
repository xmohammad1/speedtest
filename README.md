## Speedtest Server

This repository hosts a small Flask application used for network speed
testing. The server is configured to respond exclusively over HTTPS and
automatically redirects any HTTP requests to HTTPS.

### TLS Configuration

Provide paths to your TLS certificate and key via environment variables
before starting the application:

```
export SSL_CERT_FILE=/path/to/cert.pem
export SSL_KEY_FILE=/path/to/key.pem
python app.py
```

If no certificate/key is supplied the server falls back to a temporary
self‑signed certificate (suitable for local testing only).
