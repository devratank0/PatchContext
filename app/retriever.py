"""
Retrieve the most relevant chunks from the FAISS vector store.
"""

import json
from pathlib import Path

import faiss
from sentence_transformers import SentenceTransformer

VECTORSTORE_DIR = Path("vectorstore")

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index(str(VECTORSTORE_DIR / "index.faiss"))

# Load metadata
with open(VECTORSTORE_DIR / "chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)


def search(query, k=5):
    """
    Search for the most relevant chunks.
    """

    query_embedding = model.encode([query])

    distances, indices = index.search(query_embedding, k)

    results = []

    for idx in indices[0]:
        results.append(chunks[idx])

    return results


if __name__ == "__main__":

    while True:
        question = input("\nAsk a question (or type exit): ")

        if question.lower() == "exit":
            break

        results = search(question)

        print("\nTop Results:\n")

        for i, r in enumerate(results, 1):
            print("=" * 80)
            print(f"Result {i}")
            print(r["title"])
            print(r["url"])
            print()
            print(r["text"][:500])
            print()