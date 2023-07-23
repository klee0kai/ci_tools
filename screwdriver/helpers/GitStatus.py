import os, sys
import subprocess


class GitStatus:

    def git_status(self):
        result = subprocess.getoutput(f"git status ")
        return result

    def available_branches(self):
        result = subprocess.getoutput(f"git branch -a")
        return result
