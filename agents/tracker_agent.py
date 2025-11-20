# agents/tracker_agent.py
from datetime import datetime
from agents.observability_agent import log_event

# Simple in-memory store for demo
MEMORY_BANK = {"assignments": {}}

def add_assignment(user_id: str, assignment_id: str, title: str, due_date: str, meta: dict=None):
    MEMORY_BANK["assignments"][assignment_id] = {
        "user": user_id,
        "title": title,
        "due_date": due_date,
        "meta": meta or {},
        "status": "pending",
        "created_at": datetime.utcnow().isoformat()
    }
    log_event("TrackerAgent", "assignment_added", {"assignment_id": assignment_id, "title": title})
    return True

def get_pending_assignments(user_id: str):
    pending = [v for v in MEMORY_BANK["assignments"].values() if v["user"] == user_id and v["status"] == "pending"]
    log_event("TrackerAgent", "get_pending", {"user_id": user_id, "count": len(pending)})
    return pending

def mark_assignment_done(assignment_id: str):
    if assignment_id in MEMORY_BANK["assignments"]:
        MEMORY_BANK["assignments"][assignment_id]["status"] = "done"
        log_event("TrackerAgent", "assignment_done", {"assignment_id": assignment_id})
        return True
    return False
