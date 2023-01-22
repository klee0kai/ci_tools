import os, sys
import subprocess

HASH_LEN = 40


class GitChangesLog:

    def __init__(self):
        pass

    def log_bettween(self, branch1, branch2="HEAD"):
        result = subprocess.getoutput(f"git log --pretty=oneline {branch1}..{branch2}")
        log = []
        for l in result.split("\n"):
            log += [
                {
                    "hash": l[:HASH_LEN],
                    "message": l[HASH_LEN + 1:]
                }
            ]
        return log

    def only_merges(self, commits):
        merges = []
        for c in commits:
            intf = subprocess.getoutput(f"git cat-file -p  {c}").split("\n\n")[0]
            if intf.count("parent") == 2:
                merges += [c]
        return merges
