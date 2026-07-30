import json
from datetime import datetime

LOG_FILE = "logs/run.jsonl"

def write_log(question, response):
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps({
            "timestamp": datetime.utcnow().isoformat(),
            "question": question,
            "response": response
        }) + "\n")
