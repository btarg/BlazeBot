# Discord.py extension (cog) template

import discord
from discord.ext import commands

class test(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command() # This is how a command should look in cog format.
    async def test(self, ctx): # Always invoke "self"!
        """Description goes here"""
        await ctx.send("This is a test message")


def setup(client):
    client.add_cog(test(client))
