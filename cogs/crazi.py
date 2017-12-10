#Discord.py extension (cog) template
import discord
from discord.ext import commands

class The_Crazi_Rally():
    def __init__(self, client):
        self.client = client
    
        
    @commands.command(pass_context = True)
    async def pcmasterrace(self, ctx): #Joke commands
            """Consoles are better than PCs!"""
            await self.client.say(ctx.message.author.mention + " Joined the dark side!! SUCK IT CONSOLE PEASANTS!!")
	
	
    @commands.command(pass_context = True)
    async def consolemasterrace(self, ctx): #Joke commands
            """PCs are better than consoles!"""
            await self.client.say(ctx.message.author.mention + " Is just plain stupid.")


def setup(client):
    client.add_cog(The_Crazi_Rally(client))
