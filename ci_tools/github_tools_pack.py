from gh_helpers.GithubApi import GithubApi
from git_helper.GitChangesLog import GitChangesLog


class GithubToolsPack:
    def __init__(self):
        pass

    def release_diff(self, master_branch="origin/master"):
        """
        Collect release change log from Github pull requests
        :param master_branch: master or main branch for collecting changes
        :return:
        """
        repo = GitChangesLog()
        github_api = GithubApi()

        commits = list(map(lambda l: l['hash'], repo.log_bettween(master_branch)))
        merges = repo.only_merges(commits)
        pulls = list(map(lambda c: github_api.commit_pulls(c), merges))

        markdown = "# Changes List\n"
        for commit_pulls in pulls:
            for p in commit_pulls:
                if 'merge_commit_sha' not in p or p['merge_commit_sha'] not in merges:
                    continue
                markdown += "\n\n\n"
                markdown += f"## {p['title']}\n"
                if not p['body'] is None:
                    body = p['body']
                    ## simplify headers
                    body = body.replace("\n# ", "\n## ")
                    markdown += f"{body}\n\n"

                markdown += f"### Links:\n"
                markdown += f" - [Pull Request]({p['html_url']})\n\n"
                if 'issue_url' in p:
                    markdown += f" - [Issue Task]({p['issue_url']})\n\n"
                pass

        return markdown
