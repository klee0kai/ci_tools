#!/bin/python3

import argparse

from gh_helpers.GithubConfigs import GithubConfigs
from github_ci_tools import GithubCITools

if __name__ == '__main__':
    configs = GithubConfigs()
    tools = GithubCITools()

    parser = argparse.ArgumentParser(add_help=True, description="ci_tools - CI Tools")
    parser.add_argument("-f", type=str, default=None, help="Result to file")
    parser.add_argument("--summary", action='store_true', help="Same result as github report summary")
    parser.add_argument("-l", action='store_true', help="Log result to console")

    subparsers = parser.add_subparsers(help='sub-command help')

    for m in list(tools.__dir__()):
        if m[:2] == "__":
            continue
        arguments = getattr(tools, m).__code__
        parser_cmd = subparsers.add_parser(m, help="Github Action Tool")
        parser_cmd.set_defaults(func=getattr(tools, m))
        for arg in arguments.co_varnames[1:]:
            parser_cmd.add_argument(f"--{arg}", type=str)
        pass

    args = parser.parse_args()

    if not 'func' in args or args.func is None:
        parser.print_help()
        exit(0)

    func = args.func
    cmd_optionals = dict(args._get_kwargs())
    options = dict()
    for arg in func.__code__.co_varnames[1:]:
        if not cmd_optionals[arg] is None:
            options[arg] = cmd_optionals[arg]
    result = func(**options)

    if args.l:
        print(result)

    if not args.f is None:
        with(open(args.f, "w")) as f:
            f.write(result)

    if args.summary:
        with(open(configs.summary_file, "w")) as f:
            f.write(result)
