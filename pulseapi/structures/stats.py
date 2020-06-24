def get_uptime_tuple(sec):
    days, t = divmod(sec, 24 * 60 ** 2)
    hours, t = divmod(t, 60 ** 2)
    minutes, t = divmod(t, 60)
    seconds = t
    return days, hours, minutes, seconds


class Stats:
    def __init__(self, src):
        _src = src.copy()
        src = {}
        for k in _src:
            src[k.lower()] = _src[k]

        self._src = src

        self.keys = int(src["keys"])
        self.clicks = int(src["clicks"])

        if "downloadmb" in src:
            self.download = int(src["downloadmb"])
        else:
            self.download = int(src["download"])

        if "uploadmb" in src:
            self.upload = int(src["uploadmb"])
        else:

            self.upload = int(src["upload"])
        if "uptime" in src:
            uptime = int(src["uptime"])
        else:
            uptime = int(src["uptimeseconds"])
        self.uptime = get_uptime_tuple(uptime)

        if "pulses" in src:
            self.pulses = int(src["pulses"])
        else:
            self.pulses = -1


class Ranks:
    def __init__(self, src):
        _src = src.copy()
        src = {}
        for k in _src:
            src[k.lower().replace("rank_", "")] = _src[k]

        self._src = src

        self.keys = int(src["keys"])
        self.clicks = int(src["clicks"])
        self.download = int(src["download"])
        self.upload = int(src["upload"])
        self.uptime = int(src["uptime"])
