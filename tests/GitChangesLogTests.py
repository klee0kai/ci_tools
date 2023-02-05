import os
from unittest import TestCase

from ci_tools.github_tools_pack import GithubToolsPack


class GitChangesLogTests(TestCase):

    def test_log_parse(self):
        os.chdir(f"{os.getcwd()}/tests/some_git_rep")
        print(f"cur path {os.getcwd()}")
        tools = GithubToolsPack()
        md = tools.release_diff("0.0.1")

        print(md)
