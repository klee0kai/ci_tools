import argparse

from ci_tools.github_tools_pack import GithubToolsPack
from ci_tools.startup_tools_pack import StartupToolsPack
from model.AppMap import AppMap, ArgMap, CmdMap, ArgAction

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


def create_app_map():
    cmds = []
    for toolPack in [startupToolsPack, githubToolsPack]:
        for m in list(toolPack.__dir__()):
            if m[:2] == "__":
                continue
            doc_desc, doc_dict = __structured_doc_from(getattr(toolPack, m).__doc__)

            code = getattr(toolPack, m).__code__
            arguments = code.co_varnames[1:code.co_argcount]
            args_map = list(
                map(lambda a: ArgMap(
                    long_name=a,
                    action=ArgAction.STR,
                    description=doc_dict[a] if doc_dict is not None and a in doc_dict else None
                ), arguments)
            )
            cmds += [
                CmdMap(
                    name=m,
                    description=doc_desc if doc_desc is not None else "Github Action Tool",
                    method=getattr(toolPack, m),
                    args=args_map
                )
            ]

    app_map = AppMap(
        name='CI Deploy Tools',
        description='Collection of ci/cd deploy tools',
        args=[
            ArgMap(name="w", long_name="write_to", action=ArgAction.STR, description="write to file"),
            ArgMap(long_name="summary", description="Write result as github report summary",
                   action=ArgAction.STORE_TRUE),
            ArgMap(name="l", description="Log result to console", action=ArgAction.STORE_TRUE),
            ArgMap(name="d", description="Debug log", action=ArgAction.STORE_TRUE),
        ],
        cmds=cmds
    )
    return app_map


def create_arg_parser():
    app_map = create_app_map()

    arg_parser = argparse.ArgumentParser(add_help=True, description=app_map.description)
    for arg in app_map.args[:1]:
        arg_parser.add_argument(**arg.to_arg_paser())

    subparsers = arg_parser.add_subparsers(help='sub-command help')
    for cmd in app_map.cmds:
        parser_cmd = subparsers.add_parser(
            cmd.name,
            help=cmd.description if cmd.description is not None else "Github Action Tool",
        )
        parser_cmd.set_defaults(func=cmd.method)
        for arg in cmd.args:
            parser_cmd.add_argument(**arg.to_arg_paser())

    return arg_parser
