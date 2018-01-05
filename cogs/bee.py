#Josh's commands
#ya like jazzzz?????
import discord
from discord.ext import commands

class bee():
    def __init__(self, client):
        self.client = client

    @commands.command() #Print Bee Movie script from "beemovie.txt" on my dankus webshite
    async def beemovie(self):
        """teh best movieh"""
        await self.client.say("https://icrazyblaze.github.io/Download-archive/dl/beemovie.txt")


def setup(client):
    client.add_cog(bee(client))
