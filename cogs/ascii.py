# Pyfiglet and ASCII commands for BlazeBot
import discord
from discord.ext import commands

from pyfiglet import figlet_format, FontNotFound


class ASCII:
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["fancy"])
    async def fancify(self, *, text):
        """Makes text fancy!"""
        try:

            def strip_non_ascii(string):
                """ Returns the string without non ASCII characters"""
                stripped = (c for c in string if 0 < ord(c) < 127)
                return ''.join(stripped)

            text = strip_non_ascii(text)
            if len(text.strip()) < 1:
                return await self.client.say("ASCII characters only please!")
            output = ""
            for letter in text:
                if 65 <= ord(letter) <= 90:
                    output += chr(ord(letter) + 119951)
                elif 97 <= ord(letter) <= 122:
                    output += chr(ord(letter) + 119919)
                elif letter == " ":
                    output += " "
            await self.client.say(output)

        except:
            await self.client.say(config.err_mesg)



    @commands.command()
    async def bigtext(self, *, text):
        """Creates enlarged text."""
        try:
            await self.client.say("```fix\n" + figlet_format(text, font="big") + "```")
        except:
            await self.client.say(config.err_mesg)


def setup(client):
    client.add_cog(ASCII(client))
