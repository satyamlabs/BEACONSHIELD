import json
import datetime

LOG_FILE = "scan_results.log"

def log_result(data):
    timestamp = datetime.datetime.now().isoformat()
    entry = {
        "timestamp": timestamp,
        "data": data
    }
    try:
        with open(LOG_FILE, "a+", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
    except Exception as e:
        print("[LOGGER ERROR]", str(e))