from datetime import datetime
from .stats import Stats, Ranks


class Computer:
    def __init__(self, src):
        self._src = src

        self.id = int(src["ComputerID"])
        self.name = src["Name"]
        self.stats = Stats(src)

        if src["LastPulseUnixTimestamp"] is not None:
            self.last_pulse = datetime.utcfromtimestamp(
                int(src["LastPulseUnixTimestamp"])
            )
        else:
            self.last_pulse = datetime.utcfromtimestamp(0)


class User:
    def __init__(self, src):
        self._src = src

        self.id = int(src["UserID"])
        self.name = src["AccountName"]
        self.country = src["Country"]
        self.country_short = src["tld"]
        self.homepage = src["Homepage"]
        self.team_id = int(src["Team"]["TeamID"])

        self.joined = datetime.utcfromtimestamp(int(src["DateJoinedUnixTimestamp"]))
        self.last_pulse = datetime.utcfromtimestamp(int(src["LastPulseUnixTimestamp"]))

        self.stats = Stats(src)
        self.ranks = Ranks(src["Ranks"])
        self.computers = [Computer(src["Computers"][s]) for s in src["Computers"]]
