from collections import defaultdict, namedtuple
from typing import Any, NamedTuple

class LogEntry(NamedTuple):
    index: int
    value: Any


class Logger:
    def __init__(self):
        self.logs = defaultdict(list)

    def log(self, channel: str, logentry: LogEntry):
        self.logs[channel].append(logentry)

    def __getitem__(self, channel):
        return self.logs[channel]
