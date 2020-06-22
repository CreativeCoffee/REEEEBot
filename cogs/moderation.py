import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Events

    # Commands
    @commands.command()
    @commands.has_role(582681219909550103)
    async def warn(self, ctx, member: discord.Member=None, *, reason=None):
            await ctx.send(f'{member.mention} you have been warned for {reason}')
            # Log
            channel =  self.bot.get_channel(723989048452186123)
            embed = discord.Embed(title=f'{ctx.author.name} Warned {member.name}', description=reason)
            await channel.send(embed=embed)
    @commands.command()
    @commands.has_role(582681219909550103)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await ctx.send(f'{ctx.author.mention} kicked {member.name}')
        await ctx.guild.kick(user=member, reason=reason)

        # Log
        channel =  self.bot.get_channel(723989048452186123)
        embed = discord.Embed(title=f'{ctx.author.name} Kicked {member.name}', description=reason)
        await channel.send(embed=embed)
    @commands.command()
    @commands.has_role(582681219909550103)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await ctx.send(f'{ctx.author.mention} banned {member.name}')
        await ctx.guild.ban(user=member, reason=reason)

        # Log
        channel =  self.bot.get_channel(723989048452186123)
        embed = discord.Embed(title=f'{ctx.author.name} Banned {member.name}', description=reason)
        await channel.send(embed=embed)

    @commands.command()
    @commands.has_role(582681219909550103)
    async def unban(self, ctx, member, *, reason=None):
        await ctx.send(f'{ctx.author.mention} unbanned {member}')
        member = await self.bot.fetch_user(int(member))
        await ctx.guild.unban(member, reason=reason)

        # Log
        channel =  self.bot.get_channel(723989048452186123)
        embed = discord.Embed(title=f'{ctx.author.name} Unbanned {member.name}', description=reason)
        await channel.send(embed=embed)
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clean(self, ctx, numberOfMessages=5):
        await ctx.channel.purge(limit=numberOfMessages)

    




def setup(bot):
    bot.add_cog(Moderation(bot))

