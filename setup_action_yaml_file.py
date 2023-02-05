#!/bin/python3

import argparse
import logging
import yaml

from gh_helpers.GithubConfigs import GithubConfigs
from ci_tools import create_app_map

if __name__ == '__main__':
    app_map = create_app_map()

    print(yaml.dump({
        "name": app_map.name,
        "description": app_map.description,

        "run": {
            "arg": "fdfd"
        }
    }))
