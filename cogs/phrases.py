import discord
from discord.ext import commands

class Phrases(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Commands
    @commands.command( help="Waves at mentioned user!")
    async def wave(self, ctx, user):
        await ctx.send(f'{ctx.author.mention} waves at {user}!!')
    @commands.command(help="Slaps mentioned user!")
    async def slap(self, ctx, user):
        await ctx.send(f'{ctx.author.mention} slaps {user} in the face')
    @commands.command(help="Shouts mentioned user!")
    async def shout(self, ctx, user):
        await ctx.send(f'{ctx.author.mention} shouts at {user}!!')
    @commands.command(help="Eggs mentioned user!")
    async def egg(self, ctx, user):
        await ctx.send(f'{ctx.author.mention} throws eggs at {user}!!')
    @commands.command(help="YEETS mentioned user!")
    async def yeet(self, ctx, user):
        await ctx.send(f'{ctx.author.mention} YEETS {user} into oblivion!!')
    @commands.command(help="The meaning of life")
    async def crab(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/382960871468564480/615324920116674581/fftad9ltrni31.png')
    @commands.command(help="Vibe Check")
    async def vibe(self, ctx):
        await ctx.send('https://tenor.com/view/dance-weekend-vibe-mood-gif-14019019')
    @commands.command(name="No U", help="The ultimate comeback")
    async def NoU(self, ctx):
        await ctx.send('https://tenor.com/view/no-u-uno-reverse-card-no-you-its-you-gif-16190166')
    @commands.command(help="Unholy Command")
    async def UwU(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/382960871468564480/724663428580376596/unknown.png')
    @commands.command(help="Make the bot say something")
    async def say(self, ctx, *, sentence):
        await ctx.send(f"REEEE Bot says {sentence}")
    



def setup(bot):
     bot.add_cog(Phrases(bot))