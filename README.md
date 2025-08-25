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

## TCP Ping Utility

In scenarios where ICMP echo requests are blocked, you can measure latency using
TCP packets with the included `tcp_ping.py` script. The tool attempts to
establish a TCP connection to a target host and reports the time taken for the
handshake, providing output similar to the standard `ping` command.

Usage example:

```bash
python tcp_ping.py example.com 443 -c 5
```

This command runs five TCP probes against `example.com` on port `443` and prints
the latency for each attempt along with the average.
