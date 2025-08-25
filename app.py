# app.py
# Import necessary libraries from Flask and standard Python libraries
from flask import Flask, render_template, Response, request, abort
import time
import os
from pathlib import Path
from ping3 import ping as icmp_ping


def load_env_file(path: str = '.env') -> None:
    """Simple .env loader without external dependencies."""
    env_path = Path(path)
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith('#'):
                key, _, value = line.partition('=')
                os.environ.setdefault(key, value)


load_env_file()

DOMAINS = [d.strip() for d in os.getenv('DOMAINS', '').split(',') if d.strip()]
HOST = os.getenv('HOST', '0.0.0.0')
PORT = int(os.getenv('PORT', 443))
SSL_CERT_FILE = os.getenv('SSL_CERT_FILE')
SSL_KEY_FILE = os.getenv('SSL_KEY_FILE')

# Initialize the Flask application
app = Flask(__name__)

# Define the main route for the website
@app.route('/')
def index():
    """
    Serves the main HTML page for the speed test.
    Flask looks for this file in the 'templates' folder.
    """
    return render_template('index.html')

@app.route('/ping')
def ping():
    """Measure latency using an ICMP echo request."""
    client_ip = request.remote_addr
    try:
        delay = icmp_ping(client_ip, unit="ms")
    except PermissionError:
        return Response("ICMP requires administrative privileges", status=500)

    if delay is None:
        return Response("timeout", status=504)

    response = Response(str(delay))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


@app.before_request
def restrict_host():
    """Restrict requests to configured domains if provided."""
    if DOMAINS:
        host = request.host.split(':', 1)[0]
        if host not in DOMAINS:
            abort(403)

@app.route('/download')
def download():
    """
    This endpoint serves a large chunk of data for the download speed test.
    It uses a generator function to stream data in chunks, which is more
    memory-efficient than generating the whole file at once.
    """
    # Define the size of each chunk and the total number of chunks
    chunk_size = 8192  # 8 KB
    total_chunks = 20000 # Results in a ~160 MB file

    def generate_chunks():
        """
        A generator function that yields chunks of zero-byte data.
        This is efficient as it doesn't store the large data in memory.
        """
        for _ in range(total_chunks):
            yield os.urandom(chunk_size)

    # Return a streaming response
    return Response(generate_chunks(), mimetype='application/octet-stream')

@app.route('/upload', methods=['POST'])
def upload():
    """
    This endpoint handles the upload speed test.
    The client sends a large amount of data here.
    The server simply receives the data and discards it, then returns a success status.
    The actual speed is measured by the client based on how long the upload takes.
    """
    # We don't need to do anything with the data, just receive it.
    # The 'request.data' property holds the uploaded data.
    # By accessing it, we ensure the data is read from the stream.
    _ = request.data
    return "OK"

# This block ensures the app runs only when the script is executed directly
if __name__ == '__main__':
    # Running the app on the specified host and port with HTTPS.
    # Debug mode is turned off for a more production-like environment.
    app.run(host=HOST, port=PORT, debug=False, ssl_context=(SSL_CERT_FILE, SSL_KEY_FILE))
