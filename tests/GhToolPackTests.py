from unittest import TestCase

from screwdriver.ci_tools.github_tools_pack import GithubToolsPack


class GhToolPackTests(TestCase):

    def test_release_changes(self):
        tool = GithubToolsPack()
        changes = tool.gh_release_diff(master_branch="0.0.11", head="0.0.12")

        print(changes)

        with(open("changes.md", "w")) as f:
            f.write(changes)