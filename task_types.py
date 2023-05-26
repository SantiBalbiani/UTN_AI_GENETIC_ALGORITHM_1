import enum
from dataclasses import dataclass


class Priority(enum.IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


@dataclass
class Task:
    name: str
    priority: Priority
    duration: int
    value: int
