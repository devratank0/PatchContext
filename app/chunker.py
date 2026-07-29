"""
Chunk documents into smaller pieces for embedding.
"""

import json
from app.utils import save_json
from app.config import PROCESSED_DATA_DIR


def load_documents():
    """Load processed documents."""
    with open(PROCESSED_DATA_DIR / "documents.json", "r", encoding="utf-8") as f:
        return json.load(f)


def split_text(text, chunk_size=500, overlap=100):
    """
    Split text into overlapping chunks.
    """
    chunks = []

    if not text:
        return chunks

    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        if chunk.strip():
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


def main():
    documents = load_documents()

    chunks = []

    for doc in documents:
        text_chunks = split_text(doc["text"])

        for text in text_chunks:
            chunks.append({
                "type": doc["type"],
                "title": doc["title"],
                "text": text,
                "url": doc["url"]
            })

    save_json(chunks, PROCESSED_DATA_DIR / "chunks.json")

    print(f"Created {len(chunks)} chunks.")


if __name__ == "__main__":
    main()