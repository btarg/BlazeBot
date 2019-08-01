import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import platform
import sys
import os
import random
import requests
import urllib.request
import json
import time
import datetime
now = datetime.datetime.now()
diff = datetime.datetime(now.year, 12, 25) - \
    datetime.datetime.today()  # Days until Christmas

import logging
from pyfiglet import figlet_format, FontNotFound


# Config.py setup
##################################################################################
if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")

else:
    import config  # config.py is required to run; found in the same directory.
    from setup import ver # setup.py is used to get the version number
##################################################################################


# This code logs all events including chat to discord.log. This file will be overwritten when the bot is restarted - rename the file if you want to keep it.
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename=config.logfile, encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


# IMPORTANT - DO NOT TOUCH! Setup bot as "client", with description and prefix from config.py
client = Bot(description=config.des, command_prefix=config.pref)


# This message lets us know that the script is running correctly
print("Connecting...")


# Start bot and print status to console
@client.event
async def on_ready():
    print("Bot online!\n")
    f = open('logo.txt', 'r')
    print(f.read())
    f.close()
    print("Discord.py API version:", discord.__version__)
    print("Python version:", platform.python_version())
    print("Running on:", platform.system(), platform.release(), "(" + os.name + ")")
    print("BlazeBot version:", ver)
    print("Name : {}".format(client.user.name))
    print("Client ID : {}".format(client.user.id))
    print("Currently active on " + str(len(client.guilds)) + " server(s).\n")
    logger.info("Bot started successfully.")

    # Set "playing" status
    if diff.days < 2:
        print("Merry Christmas!")
        game = "Merry Christmas! <3"
    else:
        game = "BlazeBot.py | {0}help | Python version: {1} | Discord API version: {2} | Running on: {3} {4} ({5})".format(config.pref, platform.python_version(), discord.__version__, platform.platform, platform.release(), os.name)
        
    await client.change_presence(status=discord.Status.online, activity=discord.Game(game))


# Default BlazeBot commands

@client.command(aliases=['remove', 'delete'])
async def purge(ctx, number: int):
    """Bulk-deletes messages from the channel."""
    try:
        if ctx.message.author.guild_permissions.administrator:
        
            deleted = await ctx.channel.purge(limit=number)
            print('Deleted {} message(s)'.format(len(deleted)))
            logger.info('Deleted {} message(s)'.format(len(deleted)))

        else:
            await ctx.send(config.err_mesg_permission)
    except:
        await ctx.send(config.err_mesg_generic)


@client.command()
async def roles(context):
    """Lists the current roles on the server."""

    roles = context.message.guild.roles
    result = "**The roles on this server are: **"
    for role in roles:
        result += role.name + ", "
    await ctx.send(result)


@client.command()
async def hug(ctx, *, member: discord.Member = None):
    """Hug someone on the server <3"""
    try:
        if member is None:
            await ctx.send(ctx.message.author.mention + " has been hugged!")
        else:
            if member.id == ctx.message.author.id:
                await ctx.send(ctx.message.author.mention + " has hugged themself!")
            else:
                await ctx.send(member.mention + " has been hugged by " + ctx.message.author.mention + "!")

    except:
        await ctx.send(config.err_mesg_generic)


@client.command(aliases=['say'])
async def echo(ctx, *msg):
    """Makes the bot talk."""
    try:
        say = ' '.join(msg)
        await client.delete_message(ctx.message)
        return await ctx.send(say)
    except:
        await ctx.send(config.err_mesg_generic)


@client.command(aliases=['saytts'])
async def echotts(ctx, *msg):
    """Makes the bot talk, with TTS."""
    try:
        say = ' '.join(msg)
        await client.delete_message(ctx.message)
        return await ctx.send(say, tts=True)
    except:
        await ctx.send(config.err_mesg_generic)


@client.command(aliases=["fancy"])
async def fancify(ctx, *, text):
    """Makes text fancy!"""
    try:
        def strip_non_ascii(string):
            """Returns the string without non ASCII characters."""
            stripped = (c for c in string if 0 < ord(c) < 127)
            return ''.join(stripped)

        text = strip_non_ascii(text)
        if len(text.strip()) < 1:
            return await self.ctx.send(":x: ASCII characters only please!")
        output = ""
        for letter in text:
            if 65 <= ord(letter) <= 90:
                output += chr(ord(letter) + 119951)
            elif 97 <= ord(letter) <= 122:
                output += chr(ord(letter) + 119919)
            elif letter == " ":
                output += " "
        await ctx.send(output)

    except:
        await ctx.send(config.err_mesg_generic)


@client.command()
async def bigtext(ctx, *, text):
    """Enlarges text."""
    try:
        await ctx.send("```fix\n" + figlet_format(text, font="big") + "```")
    except:
        await ctx.send(config.err_mesg_generic)


@client.command(aliases=['game', 'presence'])
async def setgame(ctx, *args):
    """Sets the 'Playing' status."""
    try:
        if ctx.message.author.guild_permissions.administrator:
            setgame = ' '.join(args)
            await client.change_presence(status=discord.Status.online, activity=discord.Game(setgame))
            await ctx.send(":ballot_box_with_check: Game name set to: `" + setgame + "`")
            print("Game set to: `" + setgame + "`")
        else:
            await ctx.send(config.err_mesg_permission)
    except:
        await ctx.send(config.err_mesg_generic)


@client.command()
async def botplatform(ctx):
    """Shows what OS the bot is running on."""
    try:
        await ctx.send("The bot is currently running on: ```" + str(platform.platform()) + "```")
    except:
        await ctx.send(config.err_mesg_generic)



@client.command()
async def serverlist(ctx):
    """List the servers that the bot is active on."""
    x = ', '.join([str(server) for server in client.guilds])
    y = len(client.guilds)
    print("Server list: " + x)
    if y > 40:
        embed = discord.Embed(title="Currently active on " + str(y) + " servers:", description=config.err_mesg_generic + "```json\nCan't display more than 40 servers!```", colour=0xFFFFF)
        return await ctx.send(embed=embed)
    elif y < 40:
        embed = discord.Embed(title="Currently active on " + str(y) + " servers:", description="```json\n" + x + "```", colour=0xFFFFF)
        return await ctx.send(embed=embed)


@client.command()
async def getbans(ctx):
	"""Lists all banned users on the current server."""
	
	if ctx.message.author.guild_permissions.ban_members:
		x = await ctx.message.guild.bans()
		x = '\n'.join([str(y.user) for y in x])
		embed = discord.Embed(title="List of Banned Members", description=x, colour=0xFFFFF)
		return await ctx.send(embed=embed)
	else:
		await ctx.send(config.err_mesg_permission)
	



@client.command(aliases=['user'])
async def info(ctx, user: discord.Member):
	"""Gets info on a member, such as their ID."""
	try:
		embed = discord.Embed(title="User profile: " + user.name, colour=user.colour)
		embed.add_field(name="Name:", value=user.name)
		embed.add_field(name="ID:", value=user.id)
		embed.add_field(name="Status:", value=user.status)
		embed.add_field(name="Highest role:", value=user.top_role)
		embed.add_field(name="Joined:", value=user.joined_at)
		embed.set_thumbnail(url=user.avatar_url)
		await ctx.send(embed=embed)
	except:
		await ctx.send(config.err_mesg_generic)



@client.command()
async def ping(ctx):
    """Pings the bot and gets a response time."""
    try:
        pingtime = time.time()
        pingms = await ctx.send("*Pinging...*")
        ping = (time.time() - pingtime) * 1000
        await client.edit_message(pingms, "**Pong!** :ping_pong:  The ping time is `%dms`" % ping)
        print("Pinged bot with a response time of %dms." % ping)
        logger.info("Pinged bot with a response time of %dms." % ping)
    except:
        await ctx.send(config.err_mesg_generic)


# Choose a random insult from the list in config.py
@client.command()
async def insult(ctx):
    """Says something mean about you."""
    await ctx.send(ctx.message.author.mention + " " + random.choice(config.insults))  # Mention the user and say the insult


@client.command(aliases=['ud'])
async def urban(ctx, *msg):
    """Searches on the Urban Dictionary."""
    try:
        word = ' '.join(msg)
        api = "http://api.urbandictionary.com/v0/define"
		logger.info("Making request to " + api)
        # Send request to the Urban Dictionary API and grab info
        response = requests.get(api, params=[("term", word)]).json()
        embed = discord.Embed(description="No results found!", colour=0xFF0000)
        if len(response["list"]) == 0:
            return await ctx.send(embed=embed)
        # Add results to the embed
        embed = discord.Embed(title="Word", description=word, colour=embed.colour)
        embed.add_field(name="Top definition:", value=response['list'][0]['definition'])
        embed.add_field(name="Examples:", value=response['list'][0]['example'])
        await ctx.send(embed=embed)
    except:
        await ctx.send(config.err_mesg_generic)


@client.command(aliases=['ytid'])
async def youtubeid(ctx, *, channelid):
    """Gets statistics for a YouTube channel using ID."""
    try:
        # Make requests to YouTube API and grab info
        data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + channelid + "&key=" + config.key).read()
        logger.info("Making request to " + "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + channelid + "&key=" + config.key)
        subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
        views = json.loads(data)["items"][0]["statistics"]["viewCount"]
        vids = json.loads(data)["items"][0]["statistics"]["videoCount"]

        # Generate embed and say
        embed=discord.Embed(colour=0xff0000)
        embed.add_field(name="Subscribers:", value="{:,d}".format(int(subs)), inline=False)
        embed.add_field(name="Total views:", value="{:,d}".format(int(views)), inline=False)
        embed.add_field(name="Total videos:", value="{:,d}".format(int(vids)), inline=False)
        embed.set_thumbnail(url="https://s.ytimg.com/yts/mobile/img/apple-touch-icon-144x144-precomposed-vflopw1IA.png")
        embed.set_footer(text="Powered by YouTube API")
        await ctx.send(embed=embed)
    except:
        await ctx.send(config.err_mesg_generic)



@client.command(aliases=['ytstats'])
async def youtube(ctx, *, name):
    """Gets statistics for a YouTube channel."""
    try:
        # Make requests to YouTube API and grab info
        data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+name+"&key="+config.key).read()
        logger.info("Making request to " + "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+name+"&key="+config.key)
        subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
        views = json.loads(data)["items"][0]["statistics"]["viewCount"]
        vids = json.loads(data)["items"][0]["statistics"]["videoCount"]

        # Generate embed and say
        embed=discord.Embed(colour=0xff0000)
        embed.add_field(name="Subscribers:", value="{:,d}".format(int(subs)), inline=False)
        embed.add_field(name="Total views:", value="{:,d}".format(int(views)), inline=False)
        embed.add_field(name="Total videos:", value="{:,d}".format(int(vids)), inline=False)
        embed.set_thumbnail(url="https://s.ytimg.com/yts/mobile/img/apple-touch-icon-144x144-precomposed-vflopw1IA.png")
        embed.set_footer(text="Powered by YouTube API")
        await ctx.send(embed=embed)
    except:
        await ctx.send(config.err_mesg_generic)



@client.command()
async def load(ctx):
    """Loads startup extensions."""
    if __name__ == "__main__":  # Load startup extensions, specified in config.py
        for extension in config.startup_extensions:
            try:
                client.load_extension(extension)
                print("Loaded extension '{0}'".format(extension))
                logger.info("Loaded extension '{0}'".format(extension))
            except Exception as e:
                exc = '{0}: {1}'.format(type(e).__name__, e)
                print('Failed to load extension {0}\nError: {1}'.format(extension, exc))
                logger.info('Failed to load extension {0}\nError: {1}'.format(extension, exc))


@client.command()
async def unload(ctx, extension_name: str):
    """Unloads an extension."""
    client.unload_extension(extension_name)
    await ctx.send("{0} unloaded.".format(extension_name))



# Christmas countdown!
@client.command(aliases=['xmas', 'chrimbo'])
async def christmas(ctx):
    """Christmas countdown!"""
    await ctx.send("**{0}** day(s) left until Christmas day! :christmas_tree:".format(str(diff.days)))  # Convert the 'diff' integer into a string and say the message


@client.command(aliases=['gh', 'code', 'website'])
async def github(ctx):
    """Gives you a link to the GitHub website."""
    await ctx.send("**GitHub:** https://icrazyblaze.github.io/BlazeBot/")


if __name__ == "__main__":  # Load startup extensions, specified in config.py

    if not config.startup_extensions:
        print("No extensions enabled.")
    else:
        print("Loading extensions...")

    for extension in config.startup_extensions:
        try:
            client.load_extension(extension)
            print("Loaded extension '{0}'".format(extension))
            logger.info("Loaded extension '{0}'".format(extension))
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\nError: {}'.format(extension, exc))
            logger.info('Failed to load extension {}\nError: {}'.format(extension, exc))



if __name__ == "__main__":

    # Read client token from "config.py" (which should be in the same directory as this file)
    client.run(config.bbtoken)
