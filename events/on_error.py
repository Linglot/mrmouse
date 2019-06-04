from math import ceil

from discord import Forbidden
from discord.ext.commands import CommandOnCooldown, CheckFailure, NoPrivateMessage, CommandNotFound

from settings.lines import text_lines
from utils.utils import send_error_embed


class OnError:
    def __init__(self, bot):
        self.bot = bot

    # Basically sends a custom error message for every major errors
    async def on_command_error(self, ctx, exception):
        channel = ctx.channel

        if isinstance(exception, CommandOnCooldown):
            seconds = exception.retry_after
            if seconds > 60:
                await send_error_embed(ctx, text_lines['roles']['ping']['slow_down_m'].format(ceil(seconds / 60)))
            else:
                await send_error_embed(ctx, text_lines['roles']['ping']['slow_down_s'].format(seconds))
        elif isinstance(exception, NoPrivateMessage):
            await send_error_embed(ctx, text_lines['technical']['cant_do_in_pm'])
        elif isinstance(exception, CheckFailure):
            await send_error_embed(ctx, text_lines['roles']['ping']['no_access'])
        elif isinstance(exception, CommandNotFound):
            return
        elif isinstance(exception, Forbidden):
            # This one is quite unique, cuz it has `dm=true` which means the error will be sent into user DMs
            await send_error_embed(ctx, text_lines['technical']['forbidden'].format(channel.name, ctx.guild), dm=True)
        else:
            await send_error_embed(ctx, text_lines['technical']['unknown_error'].format(exception))


def setup(bot):
    bot.add_cog(OnError(bot))
