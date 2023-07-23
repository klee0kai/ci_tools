import os, sys
import subprocess
from dataclasses import dataclass

HASH_LEN = 40


@dataclass
class MachineResources:
    disk: str = None
    mem: str = None
    uptime: str = None


class MachineInfo:

    def available_resources(self) -> MachineResources:
        disk = subprocess.getoutput(f"df -h")
        mem = subprocess.getoutput(f"free -h")
        uptime = subprocess.getoutput(f"uptime")
        return MachineResources(
            disk=disk,
            mem=mem,
            uptime=uptime,
        )
