from datetime import datetime
from .stats import Stats, Ranks


class Team:
    def __init__(self, src):
        _src = src.copy()
        src = {}
        for k,v in _src.items():
            src[k.lower()] = v
        
        self._src = src

        self.id = src["teamid"]
        self.name = src["name"]
        self.description = src["description"]
        self.users = src["users"]

        self.stats = Stats(src)
        self.ranks = Ranks(src["ranks"])

        self.formed = datetime.utcfromtimestamp(int(src["dateformedunixtimestamp"]))
        self.founder = src["founder"]

        # the docs lied to me :(
        # self.subteams = [Subteam(s) for s in src["subteams"].values()]


class Subteam:
    def __init__(self, src):
        _src = src.copy()
        src = {}
        for k,v in _src.items():
            src[k.lower()] = v
        
        self._src = src

        self.id = int(src["subteamid"])
        self.name = src["subteamname"]
        self.founder = src["founder"]
        self.formed = datetime.utcfromtimestamp(int(src["dateformedynixtimestamp"]))
        self.users = int(src["users"])

        self.stats = Stats(src)
        self.ranks = Ranks(src["ranks"])
