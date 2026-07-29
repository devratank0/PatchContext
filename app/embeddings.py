"""
Generate embeddings and build a FAISS vector store.
"""

import json
from pathlib import Path

from sentence_transformers import SentenceTransformer
import faiss


CHUNKS_FILE = Path("data/processed/chunks.json")
VECTORSTORE_DIR = Path("vectorstore")


def load_chunks():
    with open(CHUNKS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    VECTORSTORE_DIR.mkdir(exist_ok=True)

    chunks = load_chunks()

    texts = [chunk["text"] for chunk in chunks]

    print("Loading embedding model...")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    print("Generating embeddings...")
    embeddings = model.encode(texts, show_progress_bar=True)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    faiss.write_index(index, str(VECTORSTORE_DIR / "index.faiss"))

    with open(VECTORSTORE_DIR / "chunks.json", "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=4)

    print("Vector store created successfully.")


if __name__ == "__main__":
    main()