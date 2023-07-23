#!/bin/python3
import os
import shutil

HOME = os.environ.get("HOME")

if __name__ == "__main__":
    # screwdriver
    shutil.rmtree(os.path.join(HOME, ".local/bin/screwdriver"), ignore_errors=True)
    shutil.copyfile("screwdriver.py", os.path.join(HOME, ".local/bin/screwdriver"))
    os.chmod(os.path.join(HOME, ".local/bin/screwdriver"), 0o775)
