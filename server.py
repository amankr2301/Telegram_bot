from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/run.jsonl")
def log():
    return FileResponse("logs/run.jsonl", media_type="application/json")
