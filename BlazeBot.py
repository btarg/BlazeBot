import platform
import os
import time
import random
import requests
#import traceback
import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import logging
import sys
import datetime
now = datetime.datetime.now()
diff = datetime.datetime(now.year, 12, 25) - datetime.datetime.today() #Days until Christmas

#Config.py setup
##################################################################################
if not os.path.isfile("config.py"):
            sys.exit("'config.py' not found! Please add it and try again.")

else:
    import config #config.py is required to run; found in the same directory.
##################################################################################


#This code logs all events including chat to discord.log. This file will be overwritten when the bot is restarted - rename the file if you want to keep it.

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename=config.logfile, encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


#IMPORTANT - DO NOT TOUCH! Setup bot
client = Bot(description=config.des, command_prefix=config.pref)


#This message lets us know that the script is running correctly
print("Connecting...")

#Start bot and print status to console
@client.event
async def on_ready():
	print("Bot online!")
	f = open('logo.txt', 'r')
	file_contents = f.read()
	print (file_contents)
	f.close()
	print("Discord.py API version:", discord.__version__)
	print("Python version:", platform.python_version())
	print("Running on:", platform.system(), platform.release(), "(" + os.name + ")")
	print("Name : {}".format(client.user.name))
	print("ID : {}".format(client.user.id))
	print("Currently active on " + str(len(client.servers)) + " servers.")
	print("")
	logger.info("Bot started successfully.")
	#Set "playing" status
	if diff.days < 2:
            print('Merry Christmas!')
            await client.change_presence(game=discord.Game(name="Merry Christmas! <3"))
	else: 
            await client.change_presence(game=discord.Game(name=config.presence))


#Commands


@client.command(pass_context = True, aliases=['remove', 'delete'])
async def purge(ctx, number):
    """Bulk-deletes messages from the channel."""
    try:
        if ctx.message.author.server_permissions.ban_members:
                mgs = [] #Empty list to put all the messages in the log
                number = int(number) #Converting the amount of messages to delete to an integer
                async for x in client.logs_from(ctx.message.channel, limit = number):
                    mgs.append(x)
                await client.delete_messages(mgs)
                print("Purged {} messages.".format(number))
                logger.info("Purged {} messages.".format(number))
        else:
                await client.say(config.err_mesg_permission)
    except:
	    await client.say(config.err_mesg)


@client.command(pass_context = True)
async def roles(context):
    """Lists the current roles on the server."""

    roles = context.message.server.roles
    result = "**The roles on this server are: **"
    for role in roles:
        result += role.name +  ", "
    await client.say(result)



@client.command(pass_context = True)
async def hug(ctx, *, member : discord.Member = None):
    """Hug someone on the server <3"""
    try:
	    if member is None:
	    	await client.say(ctx.message.author.mention + " has been hugged!")
	    else:
                    if member.id == ctx.message.author.id:
                        await client.say(ctx.message.author.mention + " has hugged themself!")
                    else:
                        await client.say(member.mention + " has been hugged by " + ctx.message.author.mention + "!")

    except:
    	await client.say(config.err_mesg)



@client.command(pass_context = True, aliases=['say'])
async def echo(ctx, *msg):
    """Makes the bot talk."""
    try:
        say = ' '.join(msg)
        await client.delete_message(ctx.message)
        return await client.say(say)
    except:
        await client.say(config.err_mesg)


@client.command(pass_context = True, aliases=['saytts'])
async def echotts(ctx, *msg):
    """Makes the bot talk, with TTS."""
    try:
        say = ' '.join(msg)
        await client.delete_message(ctx.message)
        return await client.say(say, tts=True)
    except:
        await client.say(config.err_mesg)




@client.command(pass_context = True)
async def servers(ctx):
    """Shows how many servers the bot is active on."""
    try:
        await client.say("Currently active on " + str(len(client.servers)) + " servers.")
    except:
        await client.say(config.err_mesg)


@client.command(pass_context = True)
async def serverlist(ctx):
    """List the servers that the bot is active on."""
    x = ', '.join([str(server) for server in client.servers])
    y = len(client.servers)
    print("Server list: " + x)
    if y > 40:
        embed = discord.Embed(title = "Currently active on " + str(y) + " servers:", description = config.err_mesg + "```json\nCan't display more than 40 servers!```", color = 0xFFFFF)
        return await client.say(embed = embed)
    elif y < 40:
        embed = discord.Embed(title = "Currently active on " + str(y) + " servers:", description = "```json\n" + x + "```", color = 0xFFFFF)
        return await client.say(embed = embed)




@client.command(pass_context = True)
async def getbans(ctx):
    """Lists all banned users on the current server."""
    x = await client.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of Banned Members", description = x, colour = 0xFFFFF)
    return await client.say(embed = embed)



@client.command(pass_context=True, aliases=['user'])
async def info(ctx, user: discord.Member):
    """Gets info on a member, such as their ID."""
    try:
	    await client.say("`The user's name is: {}`".format(user.name))
	    await client.say("`The user's ID is: {}`".format(user.id))
	    await client.say("`The user's status is: {}`".format(user.status))
	    await client.say("`The user's highest role is: {}`".format(user.top_role))
	    await client.say("`The user joined at: {}`".format(user.joined_at))

    except:
	    await client.say(config.err_mesg)



@client.command(pass_context = True)
async def ping(ctx):
    """Pings the bot and gets a response time."""
    try:
            pingtime = time.time()
            pingms = await client.say("*Pinging...*")
            ping = (time.time() - pingtime) * 1000
            await client.edit_message(pingms, "**Pong!** :ping_pong:  The ping time is `%dms`" % ping)
            print("Pinged bot with a response time of %dms." % ping)
            logger.info("Pinged bot with a response time of %dms." % ping)
    except:
            await client.say(config.err_mesg)



@client.command(pass_context = True) #Choose a random insult from the list in config.py
async def insult(ctx):
    """Says something mean about you."""
    await client.say(ctx.message.author.mention + " " + random.choice(config.answers)) #Mention the user and say the insult



@client.command(aliases=['ud'])
async def urban(*msg):
    """Searches on the Urban Dictionary."""
    try:
	    word = ' '.join(msg)
	    api = "http://api.urbandictionary.com/v0/define"
	    response = requests.get(api, params=[("term", word)]).json() #Send request to the API and grab info
	    embed = discord.Embed(description = "No results found!", colour = 0xFF0000)
	    if len(response["list"]) == 0: return await client.say(embed = embed)
	    #Add results to the embed (list)
	    embed = discord.Embed(title = "Word", description = word, colour = embed.colour)
	    embed.add_field(name = "Top definition:", value = response['list'][0]['definition'])
	    embed.add_field(name = "Examples:", value = response['list'][0]["example"])
	    embed.set_footer(text = "Tags: " + ', '.join(response['tags']))

	    await client.say(embed = embed)

    except:
	    await client.say(config.err_mesg)



@client.command(pass_context = True)
async def load(extension_name : str):
    """Loads an extension."""
    try:
        client.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await client.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await client.say("{} loaded.".format(extension_name))


@client.command()
async def unload(extension_name : str):
    """Unloads an extension."""
    client.unload_extension(extension_name)
    await client.say("{} unloaded.".format(extension_name))



@client.command(pass_context = True, aliases=['cls'])
async def clear(ctx): #Clear the console from Discord (doesn't work with Thonny)
        if ctx.message.author.server_permissions.ban_members:
            await client.say(":ballot_box_with_check: **Console cleared!**")
            os.system('cls' if os.name == 'nt' else 'clear') #checks if the script running on Windows or Unix
            print("Console cleared!")
            print("")
        else:
            await client.say(err_mesg_permission)



@client.command(pass_context = True, aliases=['xmas', 'chrimbo']) #Christmas countdown!
async def christmas(ctx):
    """Christmas countdown!"""
    await client.say("**" + str(diff.days) +"**" + " day(s) left until Christmas day! :christmas_tree:") #Convert the 'diff' integer into a string and say the message


#It's reccommended that you keep the logout command disabled.

##@client.command(pass_context = True)
##async def logout(ctx):
##    """Disconnects the bot from all servers."""
##    if ctx.message.author.server_permissions.ban_members:
##        await client.say("**Goodbye!** :zzz:")
##        print("Exiting bot...")
##        await client.logout()
##    else:
##        await client.say(config.err_mesg_permission)



if __name__ == "__main__": #Load startup extensions, specified in config.py
    for extension in config.startup_extensions:
        try:
            client.load_extension(extension)
            print("Loaded extension '" + extension + "'")
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))


#Read client token from "config.py" (which should be in the same directory as this file)
client.run(config.bbtoken)
