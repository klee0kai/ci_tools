import json
import os
import requests_cache

from screwdriver.api.GithubConfigs import CACHE_FILE


class GithubApi:

    def __init__(self):
        self.repository = os.getenv("GITHUB_REPOSITORY", None)
        self.api_url = os.getenv("GITHUB_API_URL", None)
        self.token = os.getenv("SECRETS_GH_API_TOKEN", None)
        self.session = requests_cache.CachedSession(CACHE_FILE)
        self.session.headers["Authorization"] = f"Bearer {self.token}"

    def commit_pulls(self, commit):
        resp = self.session.get(f"{self.api_url}/repos/{self.repository}/commits/{commit}/pulls")
        return json.loads(resp.text)
