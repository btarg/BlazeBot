#Discord.py extension (cog) template
from discord.ext import commands

class categorynamegoeshere():
    def __init__(self, client):
        self.client = client

#commands go here!


def setup(client):
    client.add_cog(categorynamegoeshere(client))