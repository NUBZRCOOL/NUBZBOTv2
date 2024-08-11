import hikari
import lightbulb
import os
from os.path import dirname, abspath
from __init__ import *
from logSetup import logger

os.chdir(dirname(abspath(__file__)))


Bot = lightbulb.BotApp(
    token=TOKEN,
    intents=hikari.Intents.ALL,
    help_class=None,
)

# @Bot.command()
# @lightbulb.add_checks(lightbulb.owner_only)
# @lightbulb.command("test", "test")
# @lightbulb.implements(lightbulb.PrefixCommand)
# async def test(ctx: lightbulb.Context) -> None:
    
#     members = await ctx.bot.rest.fetch_members(guild=ctx.get_guild())
#     print(members)


@Bot.listen(lightbulb.CommandErrorEvent)
async def command_error(event: lightbulb.CommandErrorEvent) -> None:

    if isinstance(event.exception, lightbulb.CommandNotFound):
        await event.context.respond(f"Oh Noes! There is no command like that!")
        logger.warning(f"{event.context.author} tried usig and unknown cmd, in guild {event.context.guild_id}")

    if isinstance(event.exception, lightbulb.MissingRequiredPermission):
        await event.context.respond("Invalid permissions!")
        logger.warning(f"{event.context.author} tried using a cmd without valid auth, in guild {event.context.guild}")

    if isinstance(event.exception, lightbulb.NotOwner):
        await event.context.respond("ur not the owner of this bot lol. You can't use this command!")
        logger.warning(f"{event.context.author}, ur not the owner of this bot lol, in guild {event.context.guild_id}")

    if isinstance(event.exception, lightbulb.NotEnoughArguments):
        await  event.context.respond("Invalid arguments.")
        logger.warning(f"{event.context.author} didn't use enough args in a cmd, in guild {event.context.guild_id}")

@Bot.listen(hikari.StartingEvent)
async def starting(event):
    
    logger.info("Starting Bot")

@Bot.listen(hikari.GuildJoinEvent)
async def guild_join(guild):

    logger.info(f"Joined guild {guild.guild_id}")


@Bot.listen(hikari.GuildLeaveEvent)
async def guild_leave(guild):

    logger.info(f"Left guild {guild.guild_id}")


@Bot.listen(hikari.StoppingEvent)
async def bot_shutdown(event):

    logger.info("Bot shutdown")


@Bot.command()
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.command("owner", "Are you my owner 0_0?.")
@lightbulb.implements(lightbulb.SlashCommand)
async def owner(ctx) -> None:

    await ctx.respond(f"{ctx.author.mention} is my owner!")


def run() -> None:

    if os.name != "nt":
        import uvloop
        uvloop.install()

    for file in os.listdir("extensions"):
        if file[:1] != "_":
            Bot.load_extensions(f"extensions.{file[:-3]}")

    logger.info("Bot started!")

    Bot.run()