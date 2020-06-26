from datetime import datetime
from .stats import Stats, Ranks


class Computer:
    def __init__(self, src):
        _src = src.copy()
        src = {}
        for k,v in _src.items():
            src[k.lower()] = v

        self._src = src

        self.id = int(src["computerid"])
        self.name = src["name"]
        self.stats = Stats(src)

        if src["lastpulseunixtimestamp"] is not None:
            self.last_pulse = datetime.utcfromtimestamp(
                int(src["lastpulseunixtimestamp"])
            )
        else:
            self.last_pulse = datetime.utcfromtimestamp(0)


class User:
    def __init__(self, src):
        _src = src.copy()
        src = {}
        for k,v in _src.items():
            src[k.lower()] = v
        
        self._src = src

        self.id = int(src["userid"])
        self.name = src["accountname"]
        self.country = src["country"]
        self.country_short = src["tld"]
        self.homepage = src["homepage"]
        self.team_id = int(src["team"]["TeamID"])

        self.joined = datetime.utcfromtimestamp(int(src["datejoinedunixtimestamp"]))
        self.last_pulse = datetime.utcfromtimestamp(int(src["lastpulseunixtimestamp"]))

        self.stats = Stats(src)
        self.ranks = Ranks(src["ranks"])
        self.computers = [Computer(s) for s in src["computers"].values()]
