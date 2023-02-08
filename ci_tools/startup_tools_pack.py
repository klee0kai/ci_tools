from helpers.GitStatus import GitStatus
from helpers.MachineInfo import MachineInfo

from result_poet.MarkdownPoet import MarkdownPoet


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
        md = MarkdownPoet()

        md.heading(f"Hello {who_to_greet}")
        md.text("Welcome to CI deploy tools")

        md.heading(f"Repository Info", level=2)
        md.text("git status:")
        md.code(GitStatus().git_status())
        md.text("git branches:")
        md.code(GitStatus().available_branches())

        md.heading(f"Machine info", level=2)
        machine = MachineInfo()
        resources = machine.available_resources()
        md.text("disk space:")
        md.code(resources.disk)
        md.text("mem free:")
        md.code(resources.mem)
        md.text("uptime:")
        md.code(resources.uptime)

        return str(md)
