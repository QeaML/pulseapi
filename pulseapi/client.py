import aiohttp
import json
import os
from .api.url_factory import URLFactory
from .structures.pulse import *
from .structures.stats import *
from .structures.teams import *
from .structures.users import *


class Client:
    """
        Client for interacting with WhatPulse's web API and [client API].
        The client always assumes the local WhatPulse client has it's client API
        enabled on port 3490. Customizable ports are not supported.
    """
    def __init__(self):
        self._url = URLFactory("http://api.whatpulse.org")
        self._session = aiohttp.ClientSession()
        
    async def _check_avil(self) -> bool:
        try:
            async with self._session.get("http://localhost:3490") as r:
                return r.status == 200
        except aiohttp.ClientConnectionError as e:
            return False

    async def _get(self, url) -> dict:
        try:
            async with self._session.get(url) as r:
                if r.status == 404:
                    return None
                elif r.status != 200:
                    raise RuntimeError(
                        "from Client: " f"Server returned non-200 code: {r.status}"
                    )
                elif r.content_length == 0:
                    return None
                j = json.loads(await r.text())
                if "err" in j:
                    raise RuntimeError(f"from Client: {j['err']}")

                return j
        except aiohttp.ClientConnectionError as e:
            return None

    async def get_user(self, id) -> User:
        """
            Retrieve a WhatPulse user from the web API.
        """
        url = self._url.make_webapi("user", {"user": id})
        j = await self._get(url)
        if j is None:
            return None

        return User(j)

    async def get_team(self, id) -> Team:
        """
            Retrieve a WhatPulse team from the web API.
        """
        url = self._url.make_webapi("team", {"team": id})
        j = await self._get(url)
        if j is None:
            return None

        return Team(j)

    async def get_user_pulses(self, id) -> list:
        """
            Retrieve a list of a WhatPulse user's pulses from the web API.
        """
        url = self._url.make_webapi("pulses", {"user": id})
        j = await self._get(url)
        if j is None:
            return None

        return [Pulse(j[k]) for k in j]

    async def get_team_pulses(self, id) -> list:
        """
            Retrieve a list of a WhatPulse team's pulses from the web API.
        """
        url = self._url.make_webapi("pulses", {"team": id})
        j = await self._get(url)
        if j is None:
            return []

        return [Pulse(j[k]) for k in j]

    async def get_local_totals(self) -> tuple:
        """
            Retrieve the account totals from the local WhatPulse client.
            Returns a tuple containing (Stats, Ranks).
        """
        url = self._url.make_clientapi("account-totals")
        j = await self._get(url)
        if j is None:
            return None

        return Stats(j), Ranks(j["ranks"])

    async def pulse_local(self) -> None:
        """
            Executes a pulse on the local WhatPulse client.
        """
        url = self._url.make_clientapi("pulse")

        async with self._session.post(url) as r:
            if r.status != 200:
                raise RuntimeError(
                    "from Client: " f"Server returned non-200 code: {r.status}"
                )

    async def get_local_unpulsed(self) -> Stats:
        """
            Retrieve the unpulsed stats from the local WhatPulse client.
        """
        url = self._url.make_clientapi("unpulsed")
        j = await self._get(url)
        if j is None:
            return None

        return Stats(j)

    async def close(self):
        await self._session.close()
