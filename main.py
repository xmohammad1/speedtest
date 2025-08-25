from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

@app.get('/ping')
async def ping() -> PlainTextResponse:
    """Return a minimal response for latency tests."""
    return PlainTextResponse('pong')

@app.get('/download')
async def download(size: int = 10 * 1024 * 1024) -> StreamingResponse:
    """Stream random bytes to the client for download speed tests.

    Args:
        size: Number of bytes to stream. Defaults to 10MB.
    """
    chunk = 1024 * 1024  # 1MB chunks

    def generate():
        remaining = size
        while remaining > 0:
            data = os.urandom(min(chunk, remaining))
            remaining -= len(data)
            yield data

    headers = {"Content-Length": str(size)}
    return StreamingResponse(generate(), media_type='application/octet-stream', headers=headers)

@app.post('/upload')
async def upload(request: Request) -> dict:
    """Consume uploaded data without storing it for upload speed tests."""
    total = 0
    async for part in request.stream():
        total += len(part)
    return {"received_bytes": total}

# Serve static files for a simple frontend
app.mount('/', StaticFiles(directory='static', html=True), name='static')
