from datetime import datetime
import json

def log_event(agent_name: str, event_type: str, details):
    """Simple print logger producing JSON-style output for observability."""
    msg = {
        "ts": datetime.utcnow().isoformat(),
        "agent": agent_name,
        "event": event_type,
        "details": details
    }
    print(json.dumps(msg))
