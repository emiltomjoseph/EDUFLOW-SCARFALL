from tools.google_search_tool import simple_web_search
from agents.observability_agent import log_event

def find_study_materials(query: str, max_results: int = 5):
    results = simple_web_search(query, max_results=max_results)
    log_event("SearchAgent", "search", {"query": query, "num_results": len(results)})
    return results
