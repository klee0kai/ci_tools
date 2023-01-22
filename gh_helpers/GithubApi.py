import json
import os, sys
import requests
import secrets


class GithubApi:

    def __init__(self):
        self.repository = os.environ["GITHUB_REPOSITORY"]
        self.api_url = os.environ["GITHUB_API_URL"]
        self.token = os.environ["GITHUB_API_TOKEN"]
        self.session = requests.Session()
        self.session.headers["Authorization"] = f"Bearer {self.token}"
        return

    def commit_pulls(self, commit):
        return json.loads(requests.get(f"{self.api_url}/repos/{self.repository}/commits/{commit}/pulls").text)
