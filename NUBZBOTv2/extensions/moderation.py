import hikari
import lightbulb
import os
import logging
import asyncio
import time

os.chdir(os.path.dirname(__file__) + "\\")

logging.basicConfig(filename="log.txt", filemode="a", format="%(levelname)s - %(asctime)s >> %(message)s", level=logging.INFO, datefmt="%a %b %d, %Y %I:%M:%S %p")

def log(level, msg):

    if level == logging.DEBUG: logging.debug(msg)
    if level == logging.INFO: logging.info(msg)
    if level == logging.WARNING: logging.warn(msg)
    if level == logging.ERROR: logging.error(msg)
    if level == logging.CRITICAL: logging.critical(msg)


Plugin = lightbulb.Plugin("moderation")


@Plugin.command()
@lightbulb.option(name="reason", description="Reason to ban the member", default="None", required=False, type=str, modifier=lightbulb.OptionModifier.CONSUME_REST)
@lightbulb.option(name="member", description="Member to ban", type=hikari.Member)
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.BAN_MEMBERS))
@lightbulb.command("ban", "Permanently bans a member from the server")
@lightbulb.implements(lightbulb.PrefixCommand)
async def ban(ctx: lightbulb.Context) -> None:

    user, reason = ctx.options.member, ctx.options.reason

    await user.ban(reason="reason")
    await ctx.respond(f"Banned {user} for: {reason}")

    embed = hikari.Embed(title="Oh Noes! You've been banned!", description=f"Oh Snap! You've been banned from {ctx.get_guild()} for: {reason}!", color=(255, 0, 0))
    embed.set_thumbnail("data:image/jpeg;base64,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")
    await user.send(embed=embed)

    log(logging.INFO, f"{ctx.author} banned {user} from {ctx.guild_id} for: {reason}, in guild {ctx.guild_id}")


@Plugin.command()
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.BAN_MEMBERS))
@lightbulb.option(name="member", description="Member to unban", type=hikari.User)
@lightbulb.command("unban", "Unbans a member from the server")
@lightbulb.implements(lightbulb.PrefixCommand)
async def unban(ctx: lightbulb.Context) -> None:

    user = ctx.options.member

    username, user_disc = user.username, user.discriminator

    ban_list = await ctx.bot.rest.fetch_bans(int(ctx.guild_id))
    for x in ban_list:
        bannedGuy_name, bannedGuy_disc = str(x.user).split("#")

        if (bannedGuy_name, bannedGuy_disc) == (username, user_disc):

            await ctx.bot.rest.unban_user(guild=ctx.guild_id, user=user)
            await ctx.respond(f"Unbanned {user}")

            embed = hikari.Embed(title="Lesgoo", decription=f"You've been unbanned from {ctx.get_guild()}!", color=(0, 255, 0))
            await ctx.bot.rest.create_message(channel=user.fetch_dm_channel, user=user, embed=embed)

            log(logging.INFO, f"{ctx.author} unbanned {user} from {ctx.guild_id}")

            return


@Plugin.command()
@lightbulb.option(name="reason", description="Reason to kick the member", default="None", required=False, type=str, modifier=lightbulb.OptionModifier.CONSUME_REST)
@lightbulb.option(name="member", description="Member to kick", type=hikari.Member)
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.KICK_MEMBERS))
@lightbulb.command("kick", "Kicks a member from the server")
@lightbulb.implements(lightbulb.PrefixCommand)
async def kick(ctx: lightbulb.Context) -> None:

    user, reason = ctx.options.member, ctx.options.reason

    await user.kick(reason=reason)
    await ctx.respond(f"Kicked {user} for: {reason}")

    embed = hikari.Embed(title="Oh Noes! You've been kicked!", description=f"Oh Snap! You've been kicked from {ctx.get_guild()} for: {reason}!", color=(255, 0, 0))
    embed.set_thumbnail("data:image/jpeg;base64,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")
    await user.send(embed=embed)

    log(logging.INFO, f"{ctx.author} kicked {user} for: {reason}, in guild {ctx.guild_id}")


@Plugin.command()
@lightbulb.option(name="reason", description="Reason to tempban the user", default="None", type=str, modifier=lightbulb.OptionModifier.CONSUME_REST)
@lightbulb.option(name="smhd", description="Second, minute, hour, or days", type=str)
@lightbulb.option(name="timeInterval", description="Interval for the time", type=int)
@lightbulb.option(name="member", description="Member to kick", type=hikari.Member)
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.BAN_MEMBERS))
@lightbulb.command("tempban", "Temporarily bans a member from a server")
@lightbulb.implements(lightbulb.PrefixCommand)
async def tempban(ctx: lightbulb.Context) -> None:

    user = ctx.options.member
    interval = ctx.options.timeInterval
    smhd = ctx.options.smhd
    reason = ctx.options.reason

    await user.ban(reason=reason)
    await ctx.respond(f"Banned {user} for {interval}{smhd} for: {reason}")

    embed = hikari.Embed(title="Oh Noes! You've been tempbanned!", description=f"Oh Snap! You've been tempbanned from {ctx.get_guild()} for: {reason}! You have been banned for {interval}{smhd}!", color=(255, 0, 0))
    embed.set_thumbnail("data:image/jpeg;base64,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")
    await user.send(embed=embed)

    log(logging.INFO, f"{ctx.author} temp banned {user} for {interval}{smhd} for: {reason}, in guild {ctx.guild_id}")

    if smhd == "s": 
        await asyncio.sleep(interval)
    elif smhd == "m": 
        await asyncio.sleep(interval*60)
    elif smhd == "h": 
        await asyncio.sleep(interval*60*60)
    elif smhd == "d": 
        await asyncio.sleep(interval*60*60*24)
    else:
        await ctx.respond("Invalid interval")
        return None

    await user.unban()
    await ctx.respond(f"Unbanned {user}.")

    embed = hikari.Embed(title="Lesgoo", decription=f"You've been unbanned from {ctx.get_guild()} after {interval}{smhd}!", color=(0, 255, 0))
    await user.send(embed=embed)

    log(logging.INFO, f"{user} got unbanned from guild {ctx.guild_id} after {interval}{smhd} for: {reason}. Banner: {ctx.author}")


@Plugin.command()
@lightbulb.option(name="reason", description="Reason for mute", type=str, default="None", modifier=lightbulb.OptionModifier.CONSUME_REST)
@lightbulb.option(name="member", description="User to mute", type=hikari.Member)
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.MUTE_MEMBERS))
@lightbulb.command("mute", "Mutes a member")
@lightbulb.implements(lightbulb.PrefixCommand)
async def clear(ctx: lightbulb.Context) -> None:

    user, reason = ctx.options.member, ctx.options.reason

    is_muted_role = None

    for role in await ctx.bot.rest.fetch_roles(guild=ctx.guild_id):
        if str(role) == "Muted":
            is_muted_role = True

            for channel in await ctx.bot.rest.fetch_guild_channels(guild=ctx.guild_id):

                await channel.edit_overwrite(target=role, deny=2099200, allow=0)

            break


    if is_muted_role:

        await user.add_role(role)
        await ctx.respond(f"Muted {user} for: {reason}")

        log(logging.INFO, f"{ctx.author} muted {user} for: {reason}, in guild {ctx.guild_id}")

    else:

        muted = await ctx.bot.rest.create_role(guild=ctx.guild_id, name="Muted", color=(128, 128, 128), permissions=None)
        for channel in await ctx.bot.rest.fetch_guild_channels(guild=ctx.guild_id):

            await channel.edit_overwrite(target=muted, deny=2099200, allow=0)
        
        await user.add_role(muted)
        await ctx.respond(f"Muted {user} for {reason}")

        log(logging.INFO, f"{ctx.author} muted {user} for: {reason}, in guild {ctx.guild_id}")


@Plugin.command()
@lightbulb.option(name="member", description="User to unmute", type=hikari.Member)
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.MUTE_MEMBERS))
@lightbulb.command("unmute", "Unmutes a member")
@lightbulb.implements(lightbulb.PrefixCommand)
async def unmute(ctx: lightbulb.Context):

    user = ctx.options.member

    for role in await ctx.bot.rest.fetch_roles(guild=ctx.guild_id):
        if str(role) == "Muted":
            muted = role

            break

    await ctx.bot.rest.remove_role_from_member(guild=ctx.guild_id, user=user, role=muted)

    await ctx.respond(f"Unmuted {user}")

    log(logging.INFO, f"{ctx.author} unmuted {user} in guild {ctx.guild_id}")


@Plugin.command()
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.MUTE_MEMBERS))
@lightbulb.option(name="reason", description="Reason to tempban the user", default="None", type=str, modifier=lightbulb.OptionModifier.CONSUME_REST)
@lightbulb.option(name="smhd", description="Second, minute, hour, or days", type=str)
@lightbulb.option(name="timeInterval", description="Interval for the time", type=int)
@lightbulb.option(name="member", description="Member to kick", type=hikari.Member)
@lightbulb.command("tempmute", "Temporarily mutes a user")
@lightbulb.implements(lightbulb.PrefixCommand)
async def tempmute(ctx: lightbulb.Context) -> None:
    
    user = ctx.options.member
    interval = ctx.options.timeInterval
    smhd = ctx.options.smhd
    reason = ctx.options.reason


    is_muted_role = None

    for role in await ctx.bot.rest.fetch_roles(guild=ctx.guild_id):
        if str(role) == "Muted":
            is_muted_role = True

            for channel in await ctx.bot.rest.fetch_guild_channels(guild=ctx.guild_id):

                await channel.edit_overwrite(target=role, deny=2099200, allow=0)

            break


    if is_muted_role:

        await user.add_role(role)
        await ctx.respond(f"Muted {user} for: {reason}")

        log(logging.INFO, f"{ctx.author} tempmuted {user} for: {reason}, time: {interval}{smhd}. In guild {ctx.guild_id}")

    else:

        muted = await ctx.bot.rest.create_role(guild=ctx.guild_id, name="Muted", color=(128, 128, 128), permissions=None)
        for channel in await ctx.bot.rest.fetch_guild_channels(guild=ctx.guild_id):

            await channel.edit_overwrite(target=muted, deny=2099200, allow=0)
        
        await user.add_role(muted)
        await ctx.respond(f"Muted {user} for: {reason}")

        log(logging.INFO, f"{ctx.author} tempmuted {user} for: {reason}, time: {interval}{smhd}. In guild {ctx.guild_id}")


    if smhd == "s": 
        await asyncio.sleep(interval)
    elif smhd == "m": 
        await asyncio.sleep(interval*60)
    elif smhd == "h": 
        await asyncio.sleep(interval*60*60)
    elif smhd == "d": 
        await asyncio.sleep(interval*60*60*24)
    else:
        await ctx.respond("Invalid interval")
        return None


    for role in await ctx.bot.rest.fetch_roles(guild=ctx.guild_id):
        if str(role) == "Muted":
            await user.remove_role(role)

    await ctx.respond(f"Unmuted {user}")

    log(logging.INFO, f"{user} was unmuted from {ctx.guild_id} after {interval}{smhd} for: {reason}. Muter: {ctx.author}")


@Plugin.command()
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.MANAGE_MESSAGES))
@lightbulb.option(name="Amount", description="Amount of messages to delete", type=int, default=6)
@lightbulb.command("purge", "Deletes amount of messages")
@lightbulb.implements(lightbulb.PrefixCommand)
async def purge(ctx: lightbulb.Context) -> None:

    amount = ctx.options.Amount


    iterator = ctx.bot.rest.fetch_messages(ctx.channel_id).limit(amount + 1)
    

    async for messages in iterator.chunk(100):

        await ctx.bot.rest.delete_messages(ctx.channel_id, messages)

    await ctx.respond(f"Deleted {amount} previous messages.", delete_after=5)

    log(logging.INFO, f"{ctx.author} purged {amount} messages in {ctx.guild_id}")




def load(Bot):
    Bot.add_plugin(Plugin)

def unload(Bot):
    Bot.remove_plugin(Plugin)