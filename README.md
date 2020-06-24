# pulseapi
qeaml's asynchronous, straight-to-the-point API wrapper for [WhatPulse](https://whatpulse.org)'s API. This wrapper includes interactions with both the online API and the local client API. (more below)

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