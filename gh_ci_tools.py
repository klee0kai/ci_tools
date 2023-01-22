import argparse
import os, sys
import secrets
from gh_ci.GithubConfigs import GithubConfigs
from main import GithubCITools

if __name__ == '__main__':
    configs = GithubConfigs()
    tools = GithubCITools()

    parser = argparse.ArgumentParser(add_help=True, description="gh_ci_tools - Github CI (Actions) Tools")
    subparsers = parser.add_subparsers(help='sub-command help')

    for m in list(tools.__dir__()):
        if m[:2] == "__":
            continue
        arguments = getattr(tools, m).__code__
        parser_cmd = subparsers.add_parser(m)
        parser_cmd.set_defaults(func=getattr(tools, m))
        for arg in arguments.co_varnames[1:]:
            parser_cmd.add_argument(f"--{arg}", type=str, default="master")
        pass

    args = parser.parse_args()

    if 'func' in args and not args.func is None:
        func = args.func
        cmd_optionals = dict(args._get_kwargs())
        options = dict()
        for arg in func.__code__.co_varnames[1:]:
            options[arg] = cmd_optionals[arg]
        func(**options)
    else:
        parser.print_help()

