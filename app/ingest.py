from app.github_client import GitHubClient
from app.utils import save_json
from app.config import RAW_DATA_DIR


def main():
    client = GitHubClient()

    print("Downloading commits...")
    commits = client.get_commits()

    print("Downloading pull requests...")
    pulls = client.get_pull_requests()

    print("Downloading issues...")
    issues = client.get_issues()

    save_json(commits, RAW_DATA_DIR / "commits.json")
    save_json(pulls, RAW_DATA_DIR / "pull_requests.json")
    save_json(issues, RAW_DATA_DIR / "issues.json")

    print("Done!")


if __name__ == "__main__":
    main()