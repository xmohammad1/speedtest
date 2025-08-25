# app.py
# Import necessary libraries from Flask and standard Python libraries
from flask import Flask, render_template, Response, request
import time
import os

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
    """
    A simple endpoint to measure latency.
    The client-side JavaScript will fetch this and measure the round-trip time.
    It returns a simple 'pong' response with headers to prevent caching.
    """
    response = Response("pong")
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

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
    # Running the app on 0.0.0.0 makes it accessible from other devices on the same network.
    # Debug mode is turned off for a more production-like environment.
    app.run(host='0.0.0.0', port=80, debug=False)
