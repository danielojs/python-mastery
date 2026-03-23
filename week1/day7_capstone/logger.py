# logger.py - Append a JSON summary log after each run

import json
import os
from datetime import datetime
from exceptions import LogWriteError


def save_run_log(meta: dict, log_path: str = "run_log.json") -> None:
    """
    Append a run summary dict to a JSON log file.
    Each entry includes a timestamp automatically.
    Raises LogWriteError if writing fails.
    """
    meta["timestamp"] = datetime.now().isoformat()

    # Load existing log or start fresh
    logs = []
    if os.path.exists(log_path):
        try:
            with open(log_path, "r") as f:
                logs = json.load(f)
        except (json.JSONDecodeError, OSError):
            logs = [] # corrupt log - start fresh

    logs.append(meta)

    try:
        with open(log_path, "w") as f:
            json.dump(logs, f, indent=2)
        print(f"  Run logged -> '{log_path}'")
    except OSError as e:
        raise LogWriteError(log_path, str(e))

