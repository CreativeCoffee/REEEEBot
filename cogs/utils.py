import discord
from discord.ext import commands



class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(help="Vote on something")
    async def vote(self, ctx, * , poll):
        embed = discord.Embed(
            title = poll,
            description = "Vote Now!",
        )
        msg = await ctx.send('', embed=embed)
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")


def setup(bot):
    bot.add_cog(Utility(bot))