import hikari
import lightbulb
import os
from os.path import dirname, abspath
from logSetup import logger

os.chdir(dirname(abspath(__file__)))


Plugin = lightbulb.Plugin("help")



@Plugin.command()
@lightbulb.command("help", "Shows all avaliable commands.")
@lightbulb.implements(lightbulb.SlashCommand)
async def help(ctx) -> None:

    embed = hikari.Embed(title="**NUBZBOT** - Help\n_", color=(0, 255, 0))


    embed.add_field(name="Help", value="Shows this message\nCommand name: `help`\nNote: Can be used as `" + "/" + "helpcmd {commandName}`\n_", inline=False)
    embed.add_field(name="Whois", value="Finds user Info\nCommand name: `whois`\nUsage: `" + "/" + "whois {user[OPTIONAL]}`\n_", inline=False)
    embed.add_field(name="Adminoverview", value="Displays all admin commands\nCommand name: `adminoverview`\nUsage: `" + "/" + "adminoverview {command[OPTIONAL]}`\n_", inline=False)
    embed.set_footer("Bot Developer: NUBZRCOOL#4627")

    logger.info(f"{ctx.author} used help cmd: help in guild, {ctx.guild_id})")

    await ctx.respond(embed=embed)

@Plugin.command()
@lightbulb.command("helpcmd", "Shows all avaliable commands.")
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def helpcmd(ctx) -> None:

    pass


@helpcmd.child
@lightbulb.command("help", "Gets info of `help` command.")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def help_sub(ctx):

    embed = hikari.Embed(title="**Help** >> Help\n_", color=(0, 255, 0))


    embed.add_field(name="Help", value="Shows all avaliable commands for the default server role.\nNote: Can be used as `" + "/" + "help {commandName}`", inline=False)
    embed.set_footer("Bot Developer: NUBZRCOOL#4627")

    logger.info(f"{ctx.author} used help cmd: helpcmd help in guild, {ctx.guild_id}")

    await ctx.respond(embed=embed)


@helpcmd.child
@lightbulb.command("whois", "Gets info of user")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def whois_sub(ctx):

    embed = hikari.Embed(title="Help >> Whois", color=(0, 255, 0))


    embed.add_field(name="Whois", value="Gets user info. If user not specified, will automatically choose command author.\nCommand name: `whois`\nUsage: `" + "/" + "whois {user[OPTIONAL]}`\n_", inline=False)
    embed.set_footer("Bot Developer: NUBZRCOOL#4627")

    logger.info(f"{ctx.author} used help cmd: helpcmd whois in guild {ctx.guild_id}")

    await ctx.respond(embed=embed)



@Plugin.command()
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.MANAGE_MESSAGES))
@lightbulb.command("adminhelp", "Shows all admin commands.")
@lightbulb.implements(lightbulb.SlashCommand)
async def adminhelp(ctx) -> None:

    embed = hikari.Embed(title="**NUBZBOT** - AdminHelp\n_", color=(255, 0, 0))


    embed.add_field(name="Adminhelp", value="Shows this message\nCommand name: `adminhelp`\nNote: Can be used as `" + "/" + "adminhelpcmd {commandName}`\n_", inline=False)
    # embed.add_field(name="Changeprefix", value="Changes this Bot's server prefix.\nCommand name: `changeprefix`\nUsage: `" + "/" + "changeprefix {newPrefix}`\n_", inline=False)
    embed.add_field(name="Ban", value="Bans a member.\nCommand name: `ban`\nUsage: `" + "/" + "ban {member} {reason[OPTIONAL]}`\n_", inline=False)
    embed.add_field(name="Unban", value="Unbans a member.\nCommand name: `unban`\nUsage: `" + "/" + "unban {member}`\n_", inline=False)
    embed.add_field(name="Kick", value="Kicks a member.\nCommand name: `kick`\nUsage: `" + "/" + "kick {member} {reason[OPTIONAL]}`\n_", inline=False)
    embed.add_field(name="Tempban", value="Temporarily bans a member.\nCommand name: `tempban`\nUsage: `" + "/" + "tempban {time} {s, m, h, d} {reason[OPTIONAL]}`\n_", inline=False)
    embed.add_field(name="Mute", value="Adds muted role to specified user.\nCommand name: `mute`\nUsage: `" + "/" + "mute {user} {reason[OPTIONAL]}`\n_", inline=False)
    embed.add_field(name="Unmute", value="Removes muted role from specified user.\nCommand name: `unmute`\nUsage: `" + "/" + "unmute {user}`\n_", inline=False)
    embed.add_field(name="Tempmute", value="Temporartily adds muted role to user\nCommand name: `tempmute`\nUsage: `" + "/" + "tempmute {time} {s, m, h, d} {reason[OPTIONAL]}`\n_")
    embed.add_field(name="Purge", value="Deletes messages in channel\nCommand name: `purge`\nUsage: `" + "/" + "purge {amount[OPTIoNAL]}`\n_")
    embed.set_footer("Bot Developer: NUBZRCOOL#4627")

    logger.info(f"{ctx.author} used help cmd: adminhelp, in guild {ctx.guild_id}")

    await ctx.respond(embed = embed)


@Plugin.command()
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.MANAGE_MESSAGES))
@lightbulb.command("adminhelpcmd", "Shows all admin commands.")
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def adminhelpcmd(ctx) -> None:

    pass


@adminhelpcmd.child
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.MANAGE_MESSAGES))
@lightbulb.command("adminhelp", "Gets info of `adminhelp` command")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def adminhelp_sub(ctx) -> None:

    embed = hikari.Embed(title="**AdminHelp** >> Adminhelp\n_", color=(255, 0, 0))


    embed.add_field(name="AdminHelp", value="Shows all admin commands.\nNote: Can be used as `" + "/" + "adminhelpcmd {commandName}`", inline=False)
    embed.set_footer("Bot Developer: NUBZRCOOL#4627")

    logger.info(f"{ctx.author} used help cmd: adminhelpcmd adminhelp, in guild {ctx.guild_id}")

    await ctx.respond(embed=embed)


# @adminhelpcmd.child
# @lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.MANAGE_MESSAGES))
# @lightbulb.command("changeprefix", "Gets info of `changeprefix` command")
# @lightbulb.implements(lightbulb.SlashSubCommand)
# async def changeprefix_sub(ctx) -> None:

#     embed = hikari.Embed(title="**AdminHelp** >> Changeprefix\n_", color=(255, 0, 0))


#     embed.add_field(name="Changeprefix", value="Changes the bot prefix for this server and stores in a JSON file.\nUsage: `" + "/" + "changeprefix {newPrefix}`", inline=False)
#     embed.set_footer("Bot Developer: NUBZRCOOL#4627")

#     log(logging.INFO, f"{ctx.author} used help cmd: adminhelp changeprefix, in guild {ctx.guild_id}")

#     await ctx.respond(embed=embed)


@adminhelpcmd.child
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.MANAGE_MESSAGES))
@lightbulb.command("ban", "Finds info of `ban` command")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def ban_sub(ctx) -> None:

    embed = hikari.Embed(title="**Adminhelp** >> Ban\n_", color=(255, 0, 0))


    embed.add_field(name="Ban", value="Permanently bans a member from the server.\nUsage: `" + "/" + "ban {member} {reason [OPTIONAL]}`", inline=False)
    embed.set_footer("Bot Developer: NUBZRCOOL#4627")

    logger.info(f"{ctx.author} used help cmd: adminhelpcmd ban, in guild {ctx.guild_id}")

    await ctx.respond(embed=embed)

@adminhelpcmd.child
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.MANAGE_MESSAGES))
@lightbulb.command("unban", "Finds info of `unban` command")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def unban_sub(ctx) -> None:

    embed = hikari.Embed(title="**Adminhelp** >> Unban\n_", color=(255, 0, 0))


    embed.add_field(name="Unban", value="Unbans a member from the server.\nUsage: `" + "/" + "unban {member}`", inline=False)
    embed.set_footer("Bot Developer: NUBZRCOOL#4627")

    logger.info(f"{ctx.author} used help cmd: adminhelpcmd unban, in guild {ctx.guild_id}")

    await ctx.respond(embed=embed)

@adminhelpcmd.child
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.MANAGE_MESSAGES))
@lightbulb.command("kick", "Finds info of `kick` command")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def kick_sub(ctx) -> None:

    embed = hikari.Embed(title="**Adminhelp** >> Kick\n_", color=(255, 0, 0))

    embed.add_field(name="Kick", value="Kicks a user from the server.\nUsage: `" + "/" + "unban {member}`", inline=False)
    embed.set_footer("Bot Developer: NUBZRCOOL#4627")

    logger.info(f"{ctx.author} used help cmd: adminhelpcmd kick, in guild {ctx.guild_id}")

    await ctx.respond(embed=embed)


@adminhelpcmd.child
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.MANAGE_MESSAGES))
@lightbulb.command("tempban", "Finds info of `tempban` command")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def tempban_sub(ctx: lightbulb.Context) -> None:

    embed = hikari.Embed(title="**Adminhelp** >> Tempban\n_", color=(255, 0, 0))
    embed.add_field(name="Tempban", value="Temporarily bans a user from the server, then unbans. Doesn't re-invite.\nUsage: `" + "/" + "tempban {member} {amount} {interval; s, min, hr, day} {reason[OPTIONAL]}`")
    embed.set_footer("Bot Developer: NUBZRCOOL#4627")

    logger.info(f"{ctx.author} used help cmd: adminhelpcmd tempban, in guild {ctx.guild_id}")

    await ctx.respond(embed=embed)


@adminhelpcmd.child
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.MANAGE_MESSAGES))
@lightbulb.command("mute", "Finds info of `mute` command")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def mute_sub(ctx:  lightbulb.Context) -> None:

    embed = hikari.Embed(title="**Adminhelp** >> Mute\n_", color=(255, 0, 0))
    embed.add_field(name="Mute", value="Mutes a user. If there is no muted role, it will be created.\nUsage: `" + "/" + "mute {reason} {reason[OPTIONAL]}`", inline=False)
    embed.set_footer("Bot Developer: NUBZRCOOL#4627")

    logger.info(f"{ctx.author} used help cmd: adminhelpcmd mute, in guild {ctx.guild_id}")

    await ctx.respond(embed=embed)


@adminhelpcmd.child
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.MANAGE_MESSAGES))
@lightbulb.command("unmute", "Finds info of `unmute` command")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def unmute_sub(ctx: lightbulb.Context) -> None:

    embed = hikari.Embed(title="**Adminhelp** >> Unmute\n_", color=(255, 0, 0))
    embed.add_field(name="Unmute", value="Unmutes a user. Removes role if it is specifically named \"Muted\"\nUsage: `" + "/" + "mute {reason} {reason[OPTIONAL]}`", inline=False)
    embed.set_footer("Bot Developer: NUBZRCOOL#4627")

    logger.info(f"{ctx.author} used help cmd: adminhelpcmd unmute, in guild {ctx.guild_id}")

    await ctx.respond(embed=embed)


@adminhelpcmd.child
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.MANAGE_MESSAGES))
@lightbulb.command("tempmute", "Finds info of `tempmute` command")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def tepmute_sub(ctx: lightbulb.Context) -> None:

    embed = hikari.Embed(title="**Adminhelp** >> Tempmute\n_", color=(255, 0, 0))
    embed.add_field(name="Tempute", value="Tempmutes a user. If there is no muted role, it will be created.\nUsage: `" + "/" + "tempute {reason} {reason[OPTIONAL]}`", inline=False)
    embed.set_footer("Bot Developer: NUBZRCOOL#4627")

    logger.info(f"{ctx.author} used help cmd: adminhelpcmd tempmute, in guild {ctx.guild_id}")

    await ctx.respond(embed=embed)


@adminhelpcmd.child
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.MANAGE_MESSAGES))
@lightbulb.command("purge", "Finds info of `purge` command")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def purge_sub(ctx: lightbulb.Context) -> None:

    embed = hikari.Embed(title="**Adminhelp** >> Purge\n_", color=(255, 0, 0))
    embed.add_field(name="Purge", value="Deletes messages in channel. Defaults to 6.\nUsage: `" + "/" + "purge {amount[OPTIONAL]}`", inline=False)
    embed.set_footer("Bot Developer: NUBZRCOOL#4627")

    logger.info(f"{ctx.author} used help cmd: adminhelpcmd purge, in guild {ctx.guild_id}")

    await ctx.respond(embed=embed)





def load(Bot):
    Bot.add_plugin(Plugin)

def unload(Bot):
    Bot.remove_plugin(Plugin)