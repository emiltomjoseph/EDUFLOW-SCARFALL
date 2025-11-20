from agents.tracker_agent import get_pending_assignments
from agents.observability_agent import log_event

def create_daily_plan(user_id: str, date_str: str, timetable: list) -> dict:
    """
    timetable: list of {"start":"09:00","end":"10:00","title":"Math"}
    Creates a plan consisting of class slots and study blocks for top pending assignments.
    """
    pending = get_pending_assignments(user_id)
    plan = {"date": date_str, "slots": []}
    # Append classes
    for slot in timetable:
        plan["slots"].append({"type": "class", **slot})
    # Add study slots for up to two pending assignments
    for i, assignment in enumerate(pending[:2]):
        plan["slots"].append({"type":"study", "title": assignment["title"], "due": assignment["due_date"], "duration_mins": 60})
    log_event("PlannerAgent", "plan_created", {"user_id": user_id, "date": date_str, "num_slots": len(plan["slots"])})
    return plan
