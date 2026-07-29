"""
Download GitHub repository data.
"""

from github_client import GitHubClient
from utils import save_json
from config import RAW_DATA


client = GitHubClient()


def download_commits():

    commits = client.fetch_all("commits")

    save_json(
        commits,
        f"{RAW_DATA}/commits.json"
    )

    print(f"Downloaded {len(commits)} commits.")


def download_pull_requests():

    prs = client.fetch_all(
        "pulls",
        {
            "state": "all"
        }
    )

    save_json(
        prs,
        f"{RAW_DATA}/pull_requests.json"
    )

    print(f"Downloaded {len(prs)} pull requests.")


def download_issues():

    issues = client.fetch_all(
        "issues",
        {
            "state": "all"
        }
    )

    save_json(
        issues,
        f"{RAW_DATA}/issues.json"
    )

    print(f"Downloaded {len(issues)} issues.")


if __name__ == "__main__":

    print("=" * 50)
    print("PATCHCONTEXT DATA INGESTION")
    print("=" * 50)

    download_commits()

    download_pull_requests()

    download_issues()

    print("\nAll GitHub data downloaded successfully.")
