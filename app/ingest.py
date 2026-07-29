import os
import json
import requests
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

OWNER = "fastapi"
REPO = "fastapi"

BASE_URL = f"https://api.github.com/repos/{OWNER}/{REPO}"

HEADERS = {
    "Accept": "application/vnd.github+json"
}

if GITHUB_TOKEN:
    HEADERS["Authorization"] = f"Bearer {GITHUB_TOKEN}"


def fetch_data(endpoint, params=None):
    """Fetch paginated data from GitHub API."""
    results = []
    page = 1

    while True:
        query = {"per_page": 100, "page": page}

        if params:
            query.update(params)

        response = requests.get(
            f"{BASE_URL}/{endpoint}",
            headers=HEADERS,
            params=query
        )

        response.raise_for_status()

        data = response.json()

        if not data:
            break

        results.extend(data)
        page += 1

    return results


def save_json(data, path):
    """Save data to a JSON file."""
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def main():

    print("\nDownloading commits...")
    commits = fetch_data("commits")
    save_json(commits, "data/commits/commits.json")

    print("Downloading pull requests...")
    prs = fetch_data("pulls", {"state": "all"})
    save_json(prs, "data/pull_requests/pull_requests.json")

    print("Downloading issues...")
    issues = fetch_data("issues", {"state": "all"})
    save_json(issues, "data/issues/issues.json")

    print("\nDownload Complete!")
    print(f"Commits : {len(commits)}")
    print(f"PRs     : {len(prs)}")
    print(f"Issues  : {len(issues)}")


if __name__ == "__main__":
    main()
