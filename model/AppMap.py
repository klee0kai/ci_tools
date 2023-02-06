from dataclasses import dataclass
from enum import Enum


class ArgAction(Enum):
    STORE_TRUE = ["store_true", None]
    STR = ["store", str]


@dataclass
class ArgMap:
    name: str = None
    long_name: str = None
    action: ArgAction = None
    description: str = None
    default: str = None

    def get_action_str(self):
        return self.action.value[0] if self.action is not None else None

    def get_action_type(self):
        return self.action.value[1] if self.action is not None else None

    def to_arg_paser(self):
        arg_map = {
            "dest": f"-{self.name}" if self.name is not None else f"--{self.long_name}",
            "action": self.get_action_str(),
            "type": self.get_action_type(),
            "default": self.default,
            "nargs": '*',
            "help": self.description,
        }
        arg_map = {k: v for k, v in arg_map.items() if not v is None or k == "default"}
        return arg_map


@dataclass
class CmdMap:
    name: str
    description: str
    args: list[ArgMap]
    method: object


@dataclass
class AppMap:
    name: str
    description: str
    args: list[ArgMap]
    cmds: list[CmdMap]
