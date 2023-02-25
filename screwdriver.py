#!/bin/python3

import argparse
import logging
import os
import sys
import shlex

from api.GithubConfigs import GithubConfigs
from ci_tools import create_arg_parser

configs = GithubConfigs()

if __name__ == '__main__':
    sys_args = shlex.split(sys.argv[1]) if len(sys.argv[1:]) == 1 else sys.argv[1:]

    parser = create_arg_parser()
    args = parser.parse_args(sys_args)

    if 'd' in args and args.d:
        logging.basicConfig(level=logging.DEBUG)

    if not 'func' in args or args.func is None:
        parser.print_help()
        exit(0)

    func = args.func
    cmd_optionals = dict(args._get_kwargs())
    options = dict()
    for arg in func.__code__.co_varnames[1:]:
        if arg in cmd_optionals and not cmd_optionals[arg] is None:
            options[arg] = cmd_optionals[arg]
    result = func(**options)

    if args.l:
        print(result)

    if not args.w is None:
        with(open(args.w, "w")) as f:
            f.write(result)

    if args.summary:
        with(open(configs.summary_file, "w")) as f:
            f.write(result)
