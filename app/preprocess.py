"""
Preprocess GitHub data for RAG indexing.
"""

import json
import os
from config import RAW_DATA, PROCESSED_DATA


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def process_commits():

    commits = load_json(f"{RAW_DATA}/commits.json")

    docs = []

    for item in commits:

        docs.append({
            "type": "commit",
            "id": item["sha"],
            "title": item["commit"]["message"],
            "text": item["commit"]["message"],
            "url": item["html_url"],
            "author": item["commit"]["author"]["name"],
            "date": item["commit"]["author"]["date"]
        })

    return docs


def process_pull_requests():

    prs = load_json(f"{RAW_DATA}/pull_requests.json")

    docs = []

    for pr in prs:

        docs.append({
            "type": "pull_request",
            "id": pr["number"],
            "title": pr["title"],
            "text": pr.get("body") or "",
            "url": pr["html_url"],
            "author": pr["user"]["login"],
            "date": pr["created_at"]
        })

    return docs


def process_issues():

    issues = load_json(f"{RAW_DATA}/issues.json")

    docs = []

    for issue in issues:

        docs.append({
            "type": "issue",
            "id": issue["number"],
            "title": issue["title"],
            "text": issue.get("body") or "",
            "url": issue["html_url"],
            "author": issue["user"]["login"],
            "date": issue["created_at"]
        })

    return docs


def main():

    documents = []

    documents.extend(process_commits())
    documents.extend(process_pull_requests())
    documents.extend(process_issues())

    save_json(
        documents,
        f"{PROCESSED_DATA}/documents.json"
    )

    print(f"Processed {len(documents)} documents.")


if __name__ == "__main__":
    main()
