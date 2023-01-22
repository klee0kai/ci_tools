import os
from unittest import TestCase

from github_ci_tools import GithubCITools


class GitChangesLogTests(TestCase):

    def test_log_parse(self):
        os.chdir(f"{os.getcwd()}/tests/some_git_rep")
        print(f"cur path {os.getcwd()}")
        tools = GithubCITools()
        md = tools.release_diff("0.0.1")

        print(md)
