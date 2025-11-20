from tools.pdf_reader_tool import extract_text_from_pdf, chunk_text
from agents.observability_agent import log_event

# Lightweight summarizer stub; replace with LLM integration later.
def summarize_chunk_stub(chunk: str) -> str:
    # return a short preview summary for demo
    preview = chunk.strip().replace("\n", " ")[:400]
    return preview + ("..." if len(chunk) > 400 else "")

def summarize_pdf(path: str) -> dict:
    raw = extract_text_from_pdf(path)
    if not raw:
        log_event("NotesAgent", "empty_pdf", {"path": path})
        return {"summary": "", "chunks": 0}
    chunks = chunk_text(raw, chunk_size_words=800)
    summaries = []
    for i, c in enumerate(chunks):
        s = summarize_chunk_stub(c)
        summaries.append(s)
        log_event("NotesAgent", "chunk_summarized", {"index": i, "words": len(c.split())})
    combined = "\n\n".join(summaries)
    log_event("NotesAgent", "pdf_summarized", {"path": path, "num_chunks": len(chunks)})
    return {"summary": combined, "chunks": len(chunks)}
