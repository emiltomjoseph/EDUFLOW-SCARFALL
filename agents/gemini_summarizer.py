import google.generativeai as genai
from agents.observability_agent import log_event

def configure_gemini(api_key: str):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-1.5-flash")

def gemini_summarize(model, chunk: str):
    prompt = f"""
Summarize the following academic text clearly and concisely:

{chunk}
"""

    try:
        res = model.generate_content(prompt)
        text = res.text.strip()
        log_event("GeminiAgent", "SUMMARIZE_OK", {"chars": len(chunk)})
        return text
    except Exception as e:
        log_event("GeminiAgent", "SUMMARIZE_ERROR", str(e))
        return "Gemini summarization error."
