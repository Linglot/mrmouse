import discord

from settings.constants import INFO_COLOR, ERROR_COLOR, MOD_ROLES


# Just a convenient way to make error boxes
async def send_error_embed(ctx, message, dm=False):
    embed = discord.Embed(description=message, colour=discord.Colour(ERROR_COLOR))
    if dm:
        await ctx.author.dm_channel.send(embed=embed)
    else:
        await ctx.send(embed=embed)


# Just a convenient way to make info boxes
async def send_info_embed(ctx, message):
    embed = discord.Embed(description=message, colour=discord.Colour(INFO_COLOR))
    await ctx.send(embed=embed)


def is_mod(member):
    return any([role in MOD_ROLES for role in member.roles])
