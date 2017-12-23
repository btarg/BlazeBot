#Discord.py extension (cog) template
import discord
from discord.ext import commands

class test():
    def __init__(self, client):
        self.client = client

    @commands.command() #This is how a command should look in cog format.
    async def test(self):
        """TEST COMMAND 2"""
        await self.client.say("This is a test message")


def setup(client):
    client.add_cog(test(client))
