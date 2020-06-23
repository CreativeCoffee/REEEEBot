import discord
from discord.ext import commands


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(help="Vote on something")
    async def vote(self, ctx, * , poll):
        await ctx.message.add_reaction("👍")
        await ctx.message.add_reaction("👎")


def setup(bot):
    bot.add_cog(Utility(bot))