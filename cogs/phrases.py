import discord
from discord.ext import commands

class Phrases(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Commands
    @commands.command()
    async def wave(self, ctx, user):
        await ctx.send(f'{ctx.author.mention} waves at {user}!!')
    @commands.command()
    async def slap(self, ctx, user):
        await ctx.send(f'{ctx.author.mention} slaps {user} in the face')
    @commands.command()
    async def shout(self, ctx, user):
        await ctx.send(f'{ctx.author.mention} shouts at {user}!!')
    @commands.command()
    async def egg(self, ctx, user):
        await ctx.send(f'{ctx.author.mention} throws eggs at {user}!!')
    @commands.command()
    async def yeet(self, ctx, user):
        await ctx.send(f'{ctx.author.mention} YEETS {user} into oblivion!!')
    @commands.command()
    async def crab(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/382960871468564480/615324920116674581/fftad9ltrni31.png')
    @commands.command()
    async def vibe(self, ctx):
        await ctx.send('https://tenor.com/view/dance-weekend-vibe-mood-gif-14019019')
    @commands.command()
    async def NoU(self, ctx):
        await ctx.send('https://tenor.com/view/no-u-uno-reverse-card-no-you-its-you-gif-16190166')
    @commands.command()
    async def UwU(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/382960871468564480/724663428580376596/unknown.png')
    



def setup(bot):
     bot.add_cog(Phrases(bot))