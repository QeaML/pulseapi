from datetime import datetime
from .stats import Stats


class Pulse:
    def __init__(self, src):
        _src = src.copy()
        src = {}
        for k,v in _src.items():
            src[k.lower()] = v

        self._src = src
        
        self.user_id = int(src["userid"])
        self.user_name = src["username"]
        self.computer_name = src["computer"]
        self.os_name = src["os"]

        self.stats = Stats(src)

        self.timestamp = datetime.utcfromtimestamp(int(src["timestamp"]))
