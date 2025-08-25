## Speedtest Server

This Flask application provides simple endpoints for network speed testing.

### HTTPS Only

The server responds exclusively over HTTPS. Any HTTP request is redirected to HTTPS.

To provide your own certificate, set the following environment variables before running the app:

```
export CERT_FILE=/path/to/cert.pem
export KEY_FILE=/path/to/key.pem
```

If these variables are not supplied, a temporary self‑signed certificate is generated.

Run the application with:

```
python app.py
```

The HTTPS server listens on port **443**, while HTTP port **80** is used only for redirects.

