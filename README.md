# pulseapi
qeaml's asynchronous, straight-to-the-point API wrapper for [WhatPulse](https://whatpulse.org)'s API. This wrapper includes interactions with both the online API and the client API. (more below)

# Example
```py
import asyncio
import pulseapi

async def main():
    wp = pulseapi.Client()
    user = await wp.get_user("QML")
    
    if user is not None:
        print(user.id, user.name)
    
    await wp.close()        # always remember to close() your client !

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```

# Web API
The web API is avilable under [`api.whatpulse.org`][https://dev.whatpulse.org/],
and allows us to query WhatPule users, teams and pulses.

# Client API
The client API is locally hosted by the WhatPulse client itself. It is
avilable under [`localhost:3490`][https://dev.whatpulse.org/], and allows us to
retreive the local client's account totals (online stats + local unpulsed),
local unpulsed stats and execute pulses.