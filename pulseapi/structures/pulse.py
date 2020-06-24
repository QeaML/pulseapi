from datetime import datetime
from .stats import Stats


class Pulse:
    def __init__(self, src):
        self.user_id = int(src["UserID"])
        self.user_name = src["Username"]
        self.computer_name = src["Computer"]
        self.os_name = src["OS"]

        self.stats = Stats(src)

        self.timestamp = datetime.utcfromtimestamp(int(src["Timestamp"]))
