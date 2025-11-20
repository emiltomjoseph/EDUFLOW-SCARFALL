from PyPDF2 import PdfReader
from typing import List

def extract_text_from_pdf(path: str) -> str:
    reader = PdfReader(path)
    texts = []
    for page in reader.pages:
        texts.append(page.extract_text() or "")
    return "\n".join(texts)

def chunk_text(text: str, chunk_size_words: int=800) -> List[str]:
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunks.append(" ".join(words[i:i+chunk_size_words]))
        i += chunk_size_words
    return chunks
