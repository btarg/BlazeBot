# BlazeBot
A multipurpose Discord bot written in Python with the discord.py module. (Version 1.2)

[![PyPI](https://img.shields.io/pypi/v/discord.py.svg)](https://pypi.python.org/pypi/discord.py/)
[![PyPI](https://img.shields.io/badge/Python-3.5%2C%203.6-blue.svg)](https://python.org/)

# Installing dependencies
The following packages are required to run (as well as [Python](https://python.org) 3.5 or over):

`python -m pip install requests`

`python -m pip install discord`

If these commands don't work, try using `python3.6` or `python3` instead of the regular command, or use `sudo` on Linux.

You can also use the scripts found in the `misc` folder that will do this for you. Remember to run the `Python35` version if you're using Python 3.5!


# Setting up and config
BlazeBot comes with a `config.py` file. Here you will add your Discord App token, and add startup extensions. You can generate a token at https://discordapp.com/developers/applications/me.

Find the string `Token goes here` in the config file and replace it with your token.


# Creating an extension (cog)
Inside the `misc` folder, you will find templates for commands and cogs.

Replace `test` with the category name, for example `Crazi`. It's also good practice to make the extension's filename the same as this, to avoid confusion.


# Loading/Unloading an extension (cog)
Use the command `load` or add to `startup_extensions` in config.py to load an extension. Unload them with the `unload` command.

You can find examples of cogs [here](https://gist.github.com/leovoel/46cd89ed6a8f41fd09c5), but make sure to replace all instances of `bot` with `client`, which is what BlazeBot uses.

You can also load cogs from a folder, by using the format: `folder.filename`. BlazeBot loads the `Crazi.py` plugin from the `cogs` folder.

# Starting the bot
On Windows, the bot can be started using the `BlazeBot-Windows.bat` file.

On Linux/Unix, the bot can be started using the `BlazeBot-Linux.sh` file. (This only works with Python 3.6.X - if you're using Python 3.5 then make sure you use the `BlazeBot-Python35.sh` Launcher instead.)

I reccommend on any Linux system that you use [Thonny](http://thonny.org) or IDLE.

# Inviting to servers
Use the [Discord Permissions Calculator](https://discordapi.com/permissions.html) to invite the bot to your server using the ID printed to the console, and make sure that it has admin permissions.

# Tips
Make sure to always update BlazeBot. You can create [GitHub Webhooks for Discord](https://support.discordapp.com/hc/en-us/articles/228383668-Intro-to-Webhooks) to get notified whenever a repo is updated.

When you do this, always keep a backup! It's also useful to write down your token, but NEVER give this to anyone you don't trust. Don't worry though - you can change a token whenever you want on the Apps page.
