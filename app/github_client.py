"""
GitHub API Client
-----------------
Handles communication with the GitHub REST API.
"""

import requests
from app.config import GITHUB_API_BASE, GITHUB_OWNER, GITHUB_REPO, HEADERS


class GitHubClient:
    """Client for fetching repository data from GitHub."""

    def __init__(self):
        self.base_url = f"{GITHUB_API_BASE}/repos/{GITHUB_OWNER}/{GITHUB_REPO}"

    def fetch(self, endpoint, params=None):
        """Fetch data from a GitHub API endpoint."""

        url = f"{self.base_url}/{endpoint}"

        response = requests.get(
            url,
            headers=HEADERS,
            params=params,
            timeout=30,
        )

        response.raise_for_status()

        return response.json()

    def get_commits(self, per_page=100):
        """Fetch commits."""
        return self.fetch(
            "commits",
            {"per_page": per_page},
        )

    def get_pull_requests(self, per_page=100):
        """Fetch pull requests."""
        return self.fetch(
            "pulls",
            {
                "state": "all",
                "per_page": per_page,
            },
        )

    def get_issues(self, per_page=100):
        """Fetch issues."""
        return self.fetch(
            "issues",
            {
                "state": "all",
                "per_page": per_page,
            },
        )