import aiohttp
import json
from .api.url_factory import URLFactory
from .structures.pulse import *
from .structures.stats import *
from .structures.teams import *
from .structures.users import *


class Client:
    def __init__(self):
        self._url = URLFactory("http://api.whatpulse.org")
        self._session = aiohttp.ClientSession()

    async def _get(self, url) -> dict:
        async with self._session.get(url) as r:
            if r.status != 200:
                raise RuntimeError(
                    "from Client: " f"Server returned non-200 code: {r.status}"
                )
            if r.content_length == 0:
                return None
            j = json.loads(await r.text())
            if "err" in j:
                raise RuntimeError(f"from Client: {j['err']}")

            return j

    async def get_user(self, id):
        url = self._url.make_webapi("user", {"user": id})
        j = await self._get(url)
        if j is None:
            return None

        return User(j)

    async def get_team(self, id):
        url = self._url.make_webapi("team", {"team": id})
        j = await self._get(url)
        if j is None:
            return None

        return Team(j)

    async def get_user_pulses(self, id):
        url = self._url.make_webapi("pulses", {"user": id})
        j = await self._get(url)
        if j is None:
            return None

        return [Pulse(j[k]) for k in j]

    async def get_team_pulses(self, id):
        url = self._url.make_webapi("pulses", {"team": id})
        j = await self._get(url)
        if j is None:
            return []

        return [Pulse(j[k]) for k in j]

    async def get_local_totals(self):
        url = self._url.make_clientapi("account-totals")
        j = await self._get(url)
        if j is None:
            return None

        return Stats(j), Ranks(j["ranks"])

    async def pulse_local(self):
        url = self._url.make_clientapi("pulse")

        async with self._session.post(url) as r:
            if r.status != 200:
                raise RuntimeError(
                    "from Client: " f"Server returned non-200 code: {r.status}"
                )

    async def get_local_unpulsed(self):
        url = self._url.make_clientapi("unpulsed")
        j = await self._get(url)
        if j is None:
            return None

        return Stats(j)

    async def close(self):
        await self._session.close()
