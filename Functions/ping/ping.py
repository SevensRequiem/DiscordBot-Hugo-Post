import random

from discord.ext import commands


class ping(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def ping(self, ctx):
        """
        Picks a random user from the server to win your giveaway.
        """
        await ctx.send(f"pong!")


def setup(bot):
    bot.add_cog(ping(bot))
