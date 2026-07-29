"""
Simple RAG chatbot using the retriever and OpenAI.
"""

import os
from openai import OpenAI

from app.retriever import search

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ask(question):
    docs = search(question)

    context = "\n\n".join(
        [
            f"Title: {d['title']}\n"
            f"Source: {d['url']}\n"
            f"Content:\n{d['text']}"
            for d in docs
        ]
    )

    prompt = f"""
You are an AI assistant for the FastAPI GitHub repository.

Answer ONLY using the context below.

If the answer is not found, say:
"I couldn't find that information in the repository."

Context:

{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content


if __name__ == "__main__":

    while True:

        q = input("\nAsk: ")

        if q.lower() == "exit":
            break

        print()
        print(ask(q))
        print()