# Make an invite link with 100 uses

import discord
from discord.ext import commands
import config

class invite(commands.Cog):
	def __init__(self, client):
		self.client = client

		@commands.command(aliases=["invitelink", "serverlink", "link"])
		async def invite(self, ctx):
			invitelinknew = await self.client.create_invite(destination = ctx.message.channel, xkcd = True, max_uses = 100)
			print(invitelinknew)
			await ctx.send(invitelinknew)


def setup(client):
    client.add_cog(invite(client))



