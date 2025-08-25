# Speed Test Example

This repository contains a minimal client–server setup for measuring latency, download and upload throughput.

## Backend

The backend uses [FastAPI](https://fastapi.tiangolo.com/) and exposes three endpoints:

- `GET /ping` – returns a quick response for latency tests.
- `GET /download` – streams random bytes to measure download speed.
- `POST /upload` – reads and discards uploaded data to measure upload speed.

Static files under `static/` provide a very simple HTML/JavaScript front‑end that exercises these endpoints.

## Running

```
pip install fastapi uvicorn
uvicorn main:app
```

Open <http://localhost:8000/> in your browser and click **Start Test**.
