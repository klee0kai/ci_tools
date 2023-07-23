from screwdriver.api.GithubApi import GithubApi
from screwdriver.helpers.GitChangesLog import GitChangesLog
from screwdriver.result_poet.MarkdownPoet import MarkdownPoet, make_link
from screwdriver.utils.Collections import remove_doubles


class GithubToolsPack:
    def __init__(self):
        pass

    def gh_release_diff(self, master_branch="origin/master", head='HEAD'):
        """
        Collect release change log from Github pull requests
        :param master_branch: master or main branch for collecting changes
        :param head: current branch
        :return:
        """
        repo = GitChangesLog()
        github_api = GithubApi()

        commits = list(map(lambda l: l['hash'], repo.log_bettween(branch1=master_branch, branch2=head)))
        merges = repo.only_merges(commits)
        pulls = list(map(lambda c: github_api.commit_pulls(c), merges))

        # filter only merged
        pulls = list(map(
            lambda p_list:
            [
                p for p in p_list
                if 'merge_commit_sha' in p and p['merge_commit_sha'] in merges
            ],
            pulls
        ))
        # flat
        pulls = [p for p in pulls if len(p) > 0]
        pulls = list(map(lambda p: p[0], pulls))
        pulls = remove_doubles(pulls, lambda x: x["id"])

        md = MarkdownPoet()
        md.heading("Changes List")
        for p in pulls:
            md.heading(p['title'], level=2)
            if not p['body'] is None:
                body = p['body']
                ## simplify headers
                body = body.replace("\n# ", "\n## ")
                md.text(body)

            assignee = p['assignee']
            if assignee is not None:
                link = make_link("@" + assignee["login"], assignee["html_url"])
                md.text(f"Developed by {link}")

            md.heading("Links", level=3)
            md.bulleted_link("Pull Request", p['html_url'])
            pass

        return str(md)
