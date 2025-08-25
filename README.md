# Speedtest

Simple Flask application for measuring network speed.

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

## Ping Test

Latency measurements now use ICMP echo requests via the [`ping3`](https://pypi.org/project/ping3/) library. Make sure the
environment has the package installed:

```
pip install ping3
```

Running ICMP pings may require administrative privileges depending on the operating system.
