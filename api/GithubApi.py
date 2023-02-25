import json
import os, sys
import requests
import secrets
import requests_cache

from api.GithubConfigs import CACHE_FILE


class GithubApi:

    def __init__(self):
        self.repository = os.environ["GITHUB_REPOSITORY"]
        self.api_url = os.environ["GITHUB_API_URL"]
        self.token = os.environ["SECRETS_GH_API_TOKEN"]
        self.session = requests_cache.CachedSession(CACHE_FILE)
        self.session.headers["Authorization"] = f"Bearer {self.token}"

    def commit_pulls(self, commit):
        resp = self.session.get(f"{self.api_url}/repos/{self.repository}/commits/{commit}/pulls")
        return json.loads(resp.text)
