"""
GitHub API Client
"""

import requests
from config import API_URL, HEADERS


class GitHubClient:

    def __init__(self):
        self.base_url = API_URL

    def fetch_all(self, endpoint, params=None):
        """
        Fetch all pages from GitHub API.
        """

        page = 1
        results = []

        while True:

            query = {
                "page": page,
                "per_page": 100
            }

            if params:
                query.update(params)

            response = requests.get(
                f"{self.base_url}/{endpoint}",
                headers=HEADERS,
                params=query
            )

            response.raise_for_status()

            data = response.json()

            if len(data) == 0:
                break

            results.extend(data)

            page += 1

        return results
