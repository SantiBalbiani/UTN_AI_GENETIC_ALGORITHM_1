import enum
from dataclasses import dataclass


class Priority(enum.IntEnum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2
    CRITICAL = 3


@dataclass
class Task:
    name: str
    priority: Priority
    duration: int
    value: int
