from datetime import datetime
from .stats import Stats, Ranks


class Team:
    def __init__(self, src):
        self._src = src

        self.id = src["TeamID"]
        self.name = src["Name"]
        self.description = src["Description"]
        self.users = src["Users"]

        self.stats = Stats(src)
        self.ranks = Ranks(src["Ranks"])

        self.formed = datetime.utcfromtimestamp(int(src["DateFormedUnixTimestamp"]))
        self.founder = src["Founder"]

        # the docs lied to me :(
        # self.subteams = [Subteam(src["Subteams"][k]) for k in src["Subteams"]]


class Subteam:
    def __init__(self, src):
        self._src = src

        self.id = int(src["SubTeamID"])
        self.name = src["SubTeamName"]
        self.founder = src["Founder"]
        self.formed = datetime.utcfromtimestamp(int(src["DateFormedUnixTimestamp"]))
        self.users = int(src["Users"])

        self.stats = Stats(src)
        self.ranks = Ranks(src["Ranks"])
