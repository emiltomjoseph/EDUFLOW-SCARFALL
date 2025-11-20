import requests
from bs4 import BeautifulSoup
from typing import List, Dict

def simple_web_search(query: str, max_results: int = 5) -> List[Dict]:
    """
    Simple scraping via DuckDuckGo HTML front-end. Fragile — use SerpAPI for robust results.
    """
    try:
        url = "https://html.duckduckgo.com/html/"
        headers = {"User-Agent": "EduFlowBot/1.0"}
        resp = requests.post(url, data={"q": query}, headers=headers, timeout=10)
        soup = BeautifulSoup(resp.text, "html.parser")
        results = []
        anchors = soup.select(".result__a")
        for a in anchors[:max_results]:
            title = a.get_text()
            href = a.get("href")
            snippet = ""
            results.append({"title": title, "snippet": snippet, "url": href})
        return results
    except Exception as e:
        return []
