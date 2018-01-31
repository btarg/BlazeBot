# Josh's commands
# ya like jazzzzz???

import discord
from discord.ext import commands

class bee():
    def __init__(self, client):
        self.client = client

    @commands.command() # Print the Bee Movie script from "beemovie.txt" on the Download Archive
    async def beemovie(self):
        """teh best movieh evar"""
        await self.client.say("https://icrazyblaze.github.io/Download-archive/dl/beemovie.txt")


def setup(client):
    client.add_cog(bee(client))
