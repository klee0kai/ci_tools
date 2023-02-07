import argparse

from ci_tools.github_tools_pack import GithubToolsPack
from ci_tools.startup_tools_pack import StartupToolsPack

startupToolsPack = StartupToolsPack()
githubToolsPack = GithubToolsPack()


def __structured_doc_from(doc_txt):
    if doc_txt is None:
        return None, None
    doc_lines = doc_txt.split("\n")
    doc_lines = [d.strip() for d in doc_lines]
    doc_desc = "\n".join([d for d in doc_lines if not d.startswith(":") and len(d) > 0])
    doc_dict_list = [d.split(':')[1:] for d in doc_lines if d.startswith(":") and len(d.split(':')) > 1]
    doc_dict = {d[0].lstrip("param").strip(): d[1] for d in doc_dict_list}
    return doc_desc, doc_dict


def add_common_args(parser):
    parser.add_argument("-w", type=str, default=None, help="Result write to file")
    parser.add_argument("--summary", action='store_true', help="Same result as github report summary")
    parser.add_argument("-l", action='store_true', help="Log result to console")
    parser.add_argument("-d", action='store_true', help="Debug log")

def create_arg_parser():
    arg_parser = argparse.ArgumentParser(add_help=True, description='Collection of ci/cd deploy tools')

    subparsers = arg_parser.add_subparsers(help='sub-command help')
    for toolPack in [startupToolsPack, githubToolsPack]:
        for m in list(toolPack.__dir__()):
            if m[:2] == "__":
                continue
            doc_desc, doc_dict = __structured_doc_from(getattr(toolPack, m).__doc__)

            code = getattr(toolPack, m).__code__

            parser_cmd = subparsers.add_parser(
                m,
                help=doc_desc if doc_desc is not None else "Github Action Tool",
            )
            parser_cmd.set_defaults(func=getattr(toolPack, m))
            add_common_args(parser_cmd)
            for arg in code.co_varnames[1:code.co_argcount]:
                parser_cmd.add_argument(f"--{arg}", type=str)

    return arg_parser
