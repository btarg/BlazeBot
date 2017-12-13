#Discord Emoji Info extension for BlazeBot
import discord
from discord.ext import commands

class Emoji():
    def __init__(self, client):
        self.client = client

    #Get emotes from all servers
    @commands.command(pass_context = True, aliases=["Emotes", "emojis"])
    async def emotes(self, ctx):
        """Display all emotes avaiable on a Server."""
        embed=discord.Embed(title="Emojis", description="Here are all the emojis available on the servers with BlazeBot:", color=0x00ff00) #setup embed
        for ej in self.client.get_all_emojis():
            output = ej.name, ej.id, ej.managed, ej.server.name
            output2 = ("```" + str(output) + "```") #Here we need 2 strings to add the backtick styling and avoid "too many arguments" errors
            embed.add_field(name=ej.name, value=output2, inline=False) #Add info to list (embed)
        await self.client.say(embed=embed)
            #await self.client.say(output2)


def setup(client):
    client.add_cog(Emoji(client))
