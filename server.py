from fastapi import FastAPI
from fastapi.responses import FileResponse
import threading

from app.bot import run_bot

app = FastAPI()


@app.on_event("startup")
def startup():
    thread = threading.Thread(target=run_bot, daemon=True)
    thread.start()


@app.get("/health")
def health():
    return {"ok": True}


@app.get("/run.jsonl")
def run_jsonl():
    return FileResponse(
        "logs/run.jsonl",
        media_type="application/json"
    )
