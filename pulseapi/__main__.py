import asyncio
import pulseapi

CLIENT = pulseapi.Client()

async def __userstats(*args):
    """Returns the stats of a user.
Usage: user <id or name>"""
    if len(args) > 0:
        user = await CLIENT.get_user(' '.join(args))
        if user is None:
            return "Could not fetch user."
        else:
            return f"""Clicks - {user.stats.clicks}
Keys - {user.stats.keys}
Download - {user.stats.download}
Upload - {user.stats.upload}
Uptime - {user.stats.uptime}"""
    else:
        return "Please specify user. (ID or name)"

async def __teamstats(*args):
    """Returns the stats of a team.
Usage: team <id or name>"""
    if len(args) > 0:
        team = await CLIENT.get_team(' '.join(args))
        if team is None:
            return "Could not fetch user."
        else:
            return f"""Clicks - {team.stats.clicks}
Keys - {team.stats.keys}
Download - {team.stats.download}
Upload - {team.stats.upload}
Uptime - {team.stats.uptime}"""
    else:
        return "Please specify team. (ID or name)"

async def __pulse(*args):
    """Executes a pulse on the local client."""
    await CLIENT.pulse_local()

async def __quit(*args):
    """Exit the CLI."""
    pass

# ==================== PULSEAPI ENDS HERE ==================== #

async def _help(*args):
    """Gets help on a command.
Usage: help <command>"""
    if len(args) > 0:
        if args[0].lower() in CMD_LIST:
            return CMD_LIST[args[0].lower()].__doc__
        else:
            return f"ERROR: Command `{args[0]}` not found."
    else:
        return "Type the name of the command after `help` to get help on that"
        "command."

async def __commands(*args):
    """Returns a list of commands."""
    return ('\n'.join([
            f"{n} - {c.__doc__.splitlines()[0]}"  for n,c in CMD_LIST.items()
        ]))

CMD_LIST = {
    "help":_help,
    "cmd":__commands,
    "user":__userstats,
    "team":__teamstats,
    "pulse":__pulse,
    "quit":__quit
}

async def main():
    print(f"""puleapi v{pulseapi.__version__}
Type `help` for help.
Type `cmd` for a list of commands.
""")
    while True:
        raw = input("? ")
        cmd = raw.lower().split(" ")[0]
        args = raw.split(" ")[1:]

        if cmd == "quit":
            await CLIENT.close()
            break
        elif cmd in CMD_LIST:
            print(await CMD_LIST[cmd](*args))
        else:
            print(f"ERROR: Invalid command `{cmd}`.")
        print()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())