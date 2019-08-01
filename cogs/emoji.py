# Discord Emoji Info extension for BlazeBot

import discord
from discord.ext import commands


class Emoji(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Get emotes from all servers
    @commands.command(aliases=["emoji", "emojis"])
    async def emotes(self, ctx):
        """Displays all emotes avaiable on a server."""
        embed = discord.Embed(title="Emojis", description="Here are all the emojis available on the servers with BlazeBot:", color=0x00ff00)  # setup embed
		
        for ej in self.client.emojis:
            output = ej.name, ej.id, ej.managed, ej.guild.name
            # Here we need 2 strings to add the backtick styling and avoid "too many arguments" errors
            output2 = ("```{}```".format(str(output)))
            # Add info to list (embed)
            embed.add_field(name=ej.name, value=output2, inline=False)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Emoji(client))
