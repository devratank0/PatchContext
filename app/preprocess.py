import json
from app.config import RAW_DATA_DIR, PROCESSED_DATA_DIR
from app.utils import save_json


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def process():
    commits = load_json(RAW_DATA_DIR / "commits.json")
    pulls = load_json(RAW_DATA_DIR / "pull_requests.json")
    issues = load_json(RAW_DATA_DIR / "issues.json")

    documents = []

    for c in commits:
        documents.append({
            "type": "commit",
            "title": c["commit"]["message"].split("\n")[0],
            "text": c["commit"]["message"],
            "url": c["html_url"]
        })

    for p in pulls:
        documents.append({
            "type": "pull_request",
            "title": p["title"],
            "text": p.get("body") or "",
            "url": p["html_url"]
        })

    for i in issues:
        documents.append({
            "type": "issue",
            "title": i["title"],
            "text": i.get("body") or "",
            "url": i["html_url"]
        })

    save_json(documents, PROCESSED_DATA_DIR / "documents.json")
    print(f"Saved {len(documents)} documents.")


if __name__ == "__main__":
    process()