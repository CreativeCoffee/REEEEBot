import discord
from discord.ext import commands
import random
import time

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def roll(self, ctx):
        await ctx.send(f'You rolled {random.randrange(1, 6)}')
    @commands.command()
    async def coinflip(self, ctx):
        sides = ['heads', 'tails']
        coin = random.choice(sides)
        await ctx.send(f'*flips coin*')
        time.sleep(1)
        await ctx.send(f'Its {coin}')
    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, question):
        answers = [
            'It is certain.', 
            'It is decidedly so.', 
            'Without a doubt.', 
            'Yes – definitely.', 
            'You may rely on it.', 
            'As I see it, yes.', 
            'Most likely.', 
            'Outlook good.', 
            'Yes.',
            'Signs point to yes.', 
            'Reply hazy, try again.', 
            'Ask again later.', 
            'Better not tell you now.', 
            'Cannot predict now.', 
            'Concentrate and ask again.', 
            "Don't count on it.",             
            'My reply is no.', 
            'My sources say no.', 
            'Outlook not so good.', 
            'Very doubtful.' 
        ]
        response = random.choice(answers)
        await ctx.send(response)

def setup(bot):
    bot.add_cog(Games(bot))