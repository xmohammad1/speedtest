# Speedtest

Simple Flask application for measuring network speed.

The `/ping` endpoint forces the TCP connection to close on every request so
that latency is calculated over a fresh TCP handshake similar to speedtest.net.

## Configuration

Create a `.env` file in the project root to configure HTTPS and allowed domains:

```
DOMAINS=example.com,www.example.com
SSL_CERT_FILE=/etc/ssl/certs/example.com.crt
SSL_KEY_FILE=/etc/ssl/private/example.com.key
HOST=0.0.0.0
PORT=443
```

Run the application with:

```
python app.py
```

The server will start on HTTPS port `443` using the provided certificate files.
