from gh_helpers.GithubApi import GithubApi
from git_helper.GitChangesLog import GitChangesLog


class StartupToolsPack:
    def __init__(self):
        pass

    def hello_world(
            self,
            who_to_greet='World',
    ):
        """
        Print welcome summary
        :param who_to_greet: Whom we greet
        :return:
        """
        markdown1 = f"# Hello {who_to_greet}\n"
        markdown1 += "Welcome to CI deploy tools\n"
        return markdown1
