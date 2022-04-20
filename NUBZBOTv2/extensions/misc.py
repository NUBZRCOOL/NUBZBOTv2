import hikari
import lightbulb
import logging

logging.basicConfig(filename="log.txt", filemode="a", format="%(levelname)s - %(asctime)s >> %(message)s", level=logging.INFO, datefmt="%a %b %d, %Y %I:%M:%S %p")

def log(level, msg):

    if level == logging.DEBUG: logging.debug(msg)
    if level == logging.INFO: logging.info(msg)
    if level == logging.WARNING: logging.warn(msg)
    if level == logging.ERROR: logging.error(msg)
    if level == logging.CRITICAL: logging.critical(msg)


Plugin = lightbulb.Plugin("misc")

@Plugin.command()
@lightbulb.option("user", "Targeted user", default=None, type=hikari.Member)
@lightbulb.command("whois", "Finds user information")
@lightbulb.implements(lightbulb.PrefixCommand)
async def whois(ctx: lightbulb.Context) -> None:

    user = ctx.options.user

    if user == None:

        user = ctx.member

    user_roles = []
    for role in user.get_roles():
        user_roles.append(role.mention)

    if len(user_roles) == 1:
        user_roles = "@everyone"
    else:
        user_roles[-1] = "@everyone"
        user_roles = ", ".join(user_roles)


    top_role = user.get_top_role().name
    if top_role != "@everyone":
        top_role = user.get_top_role().mention


    embed = hikari.Embed(title=f"Info - {user}", timestamp=ctx.event.message.created_at, color=user.get_top_role().color)
    embed.set_footer(text=f"Requested by {ctx.author}", icon=ctx.author.avatar_url)
    embed.set_thumbnail(user.avatar_url)

    embed.add_field(name="Display name", value=f"{user.display_name}", inline=False)
    embed.add_field(name="User ID", value=user.id, inline=False)
    embed.add_field(name="Created Account at", value=user.created_at.strftime("%a %b %d, %Y %I:%M:%S %p UTC"), inline=False)
    embed.add_field(name="Joined Server at", value=(user.joined_at).strftime("%a %b %d, %Y %I:%M:%S %p UTC"), inline=False)
    embed.add_field(name=f"Roles ({len(user_roles.split(','))})", value=f"{user_roles}", inline=False)
    embed.add_field(name="Top role", value=f"{top_role}", inline=False)
    embed.add_field(name="Is Bot?", value=user.is_bot, inline=False)

    await ctx.respond(embed=embed)

    log(logging.INFO, f"{ctx.author} wanted info of {user}, in guild {ctx.guild_id}")




def load(Bot):
    Bot.add_plugin(Plugin)

def unload(Bot):
    Bot.remove_plugin(Plugin)