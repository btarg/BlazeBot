# BlazeBot
A Discord bot written in Python with the discord.py module.


# Installing dependencies
The following packages are required to run (as well as [Python](https://python.org) 3.5 or over):

`python -m pip install requests`

`python -m pip install discord`

If these commands don't work, try using `python3.6` or `python3` instead of the regular command, or use `sudo` on Linux.


# Setting up and config
BlazeBot comes with a `config.py` file. Here you will add your Discord App token, and add startup extensions. You can generate a token at https://discordapp.com/developers/applications/me.

Find the string `Token goes here` in the config file and replace it with your token.


# Creating an extension (cog)
Inside the `misc` folder, you will find templates for commands and cogs.

Replace `categorynamegoeshere` with the category name, for example `RNG`. It's also good practice to make the extension's filename the same as this.


# Loading/Unloading an extension (cog)
Use the command `load` or add to `startup_extensions` in config.py to load an extension. Unload them with the `unload` command.

You can find examples of cogs [here](https://gist.github.com/leovoel/46cd89ed6a8f41fd09c5), but make sure to replace all instances of `bot` with `client`, which is what BlazeBot uses.

You can also load cogs from a folder, by using the format: `folder.filename`. BlazeBot loads the `Crazi.py` plugin from the `cogs` folder.

# Starting the bot
On Windows, the bot can be started using the `BlazeBot-Windows.bat` file.

On Linux/Unix, the bot can be started using the `BlazeBot-Linux.sh` file.

I reccommend on any other system that you use [Thonny](http://thonny.org) or IDLE.

# Inviting to servers
Use the [Discord Permissions Calculator](https://discordapi.com/permissions.html) to invite the bot to your server using the ID printed to the console, and make sure that it has admin permissions.

