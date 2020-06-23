import discord
import os
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=['h'], help="Shows the help message")
    async def customhelp(self, ctx, *cog):
        try:
            if not cog:
                help_embed = discord.Embed(
                    title="List of Cogs & Uncatagorized Commands",
                    description="Use ?help <cog> to get detailed information"
                )
                cogs_description = ''
                for i in self.bot.cogs:
                    cogs_description += f'{i} - {self.bot.cogs[i].__doc__}\n'
                help_embed.add_field(
                    name="Cogs",
                    value=cogs_description[0: len(cogs_description)-1],
                    inline=False 
                )
                commands_description = ''
                for j in self.bot.walk_commands():
                    if not j.cog_name and not j.hidden:
                        commands_description += f"**{j.name}** - {j.help}\n"
                help_embed.add_field(
                    name="Uncatagorized Commands",
                    value=commands_description[0:len(commands_description)-1],
                    inline=False,
                )
                # await ctx.message.add_reaction("✉")
                await ctx.send('', embed=help_embed)
            else:
                if len(cog) > 1:
                    await ctx.send("Too many arguments")
                else:
                    isCommandFound = False
                    for i in self.bot.cogs:
                        for j in cog:
                            if i == j:
                                help_embed=discord.Embed(
                                    title=f"{cog[0]} Commands",
                                    description=self.bot.cogs[cog[0]].__doc__
                                )
                                for c in self.bot.get_cog(j).get_commands():
                                    if not c.hidden:
                                        help_embed.add_field(
                                            name=c.name,
                                            value=c.help,
                                            inline=False,
                                        )
                                isCommandFound = True
                    if not isCommandFound:
                        ctx.send("That command does not exist")
                    else:
                        # await ctx.message.add_reaction("✉")
                        await ctx.send('', embed=help_embed)
        except:
            await ctx.send("I can't send embeds :')")

def setup(bot):
    bot.add_cog(Help(bot))

