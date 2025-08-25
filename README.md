# Speedtest

Simple Flask application for measuring network speed.

## HTTPS

The server now enforces HTTPS and redirects HTTP requests to HTTPS.
Custom certificate and key files can be specified via the environment
variables `SSL_CERT_FILE` and `SSL_KEY_FILE`. If not provided, a temporary
certificate is generated automatically.
