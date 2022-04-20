import hikari
import lightbulb
import os
import json
from __init__ import *
import logging

os.chdir(os.path.dirname(__file__) + "\\")

logging.basicConfig(filename="log.txt", filemode="a", format="%(levelname)s - %(asctime)s >> %(message)s", level=logging.INFO, datefmt="%a %b %d, %Y %I:%M:%S %p")

def log(level, msg):

    if level == logging.DEBUG: logging.debug(msg)
    if level == logging.INFO: logging.info(msg)
    if level == logging.WARNING: logging.warn(msg)
    if level == logging.ERROR: logging.error(msg)
    if level == logging.CRITICAL: logging.critical(msg)


def getPrefix(Bot, message) -> str:

    with open("..\\data\\prefixes.json", "r") as prefix_file:

        prefixes = json.load(prefix_file)
    try:

        return prefixes[str(message.guild_id)]

    except Exception:
        guildID = message.guild_id

        with open("..\\data\\prefixes.json", "r") as prefix_file:

            prefixes = json.load(prefix_file)

        prefixes[str(guildID)] = "nub!"

        with open("..\\data\\prefixes.json", "w") as prefix_file:

            json.dump(prefixes, prefix_file, indent=4)

        return prefixes[str(guildID)]


Bot = lightbulb.BotApp(
    token=TOKEN,
    prefix=getPrefix,
    intents=hikari.Intents.ALL,
    help_class=None,
)


@Bot.command()
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.command("test", "test")
@lightbulb.implements(lightbulb.PrefixCommand)
async def test(ctx: lightbulb.Context) -> None:
    
    members = await ctx.bot.rest.fetch_members(guild=ctx.get_guild())
    print(members)


@Bot.listen(lightbulb.CommandErrorEvent)
async def command_error(event: lightbulb.CommandErrorEvent) -> None:

    if isinstance(event.exception, lightbulb.CommandNotFound):
        await event.context.respond(f"Oh Noes! There is no command like that!")
        log(logging.WARNING, f"{event.context.author} tried usig and unknown cmd, in guild {event.context.guild_id}")

    if isinstance(event.exception, lightbulb.MissingRequiredPermission):
        await event.context.respond("Invalid permissions!")
        log(logging.WARNING, f"{event.context.author} tried using a cmd without valid auth, in guild {event.context.guild_id}")

    if isinstance(event.exception, lightbulb.NotOwner):
        await event.context.respond("ur not the owner of this bot lol. You can't use this command!")
        log(logging.WARNING, f"{event.context.author}, ur not the owner lol, in guild {event.context.guild_id}")

    if isinstance(event.exception, lightbulb.NotEnoughArguments):
        await  event.context.respond("Invalid arguments.")
        log(logging.WARNING, f"{event.context.author} didn't use enough args in a cmd, in guild {event.context.guild_id}")


@Bot.listen(hikari.GuildJoinEvent)
async def guild_join(guild):

    with open("..\\data\\prefixes.json", "r") as prefix_file:

        prefixes = json.load(prefix_file)

    prefixes[str(guild.id)] = "nub!"

    with open("..\\data\\prefixes.json", "w") as prefix_file:

        json.dump(prefixes, prefix_file, indent=4)

    log(logging.INFO, f"Joined guild {guild}")


@Bot.listen(hikari.GuildLeaveEvent)
async def guild_leave(guild):

    with open("..\\data\\prefixes.json", "r") as prefix_file:

        prefixes = json.load(prefix_file)

    prefixes.pop(str(guild.id))

    with open("..\\data\\prefixes.json", "w") as prefix_file:

        json.dump(prefixes, prefix_file, indent=4)

    log(logging.INFO, f"Left guild {guild}")


@Bot.listen(hikari.StoppingEvent)
async def bot_shutdown(event):

    log(logging.INFO, f"Bot shutdown")


@Bot.command()
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.command("owner", "Are you my owner 0_0?.")
@lightbulb.implements(lightbulb.PrefixCommand)
async def owner(ctx) -> None:

    await ctx.respond(f"{ctx.author.mention} is my owner!")


@Bot.command()
@lightbulb.option("new_prefix", "New server prefix", str)
@lightbulb.command("changeprefix", "Change server prefix.")
@lightbulb.implements(lightbulb.PrefixCommand)
async def changeprefix(ctx: lightbulb.Context) -> None:

    new_prefix = ctx.options.new_prefix

    with open("..\\data\\prefixes.json", "r") as prefix_file:

        prefixes = json.load(prefix_file)

    prefixes[str(ctx.guild_id)] = new_prefix

    with open("..\\data\\prefixes.json", "w") as prefix_file:

        json.dump(prefixes, prefix_file, indent=4)

    await ctx.respond(f"New Bot prefix: {new_prefix}")

    log(logging.INFO, f"{ctx.author} changed server prefix on guild {ctx.guild_id} to {new_prefix}")


def run() -> None:

    if os.name != "nt":
        import uvloop
        uvloop.install()

    for file in os.listdir("extensions"):
        if file[:1] != "_":
            Bot.load_extensions(f"extensions.{file[:-3]}")

    log(logging.INFO, "Bot started!")

    Bot.run()