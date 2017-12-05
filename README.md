# BlazeBot
A Discord bot written in Python with the discord.py module.


# Installing dependencies
The following packages are required to run (as well as python):

`python -m pip install requests`

`python -m pip install discord`

If these commands don't work, try using `python3.6` or `python3` instead of the regular command, or use `sudo` on Linux.


# Setting up and config
BlazeBot comes with a `config.py` file. Here you will add your Discord App token, and add startup extensions. You can generate a token at https://discordapp.com/developers/applications/me.


# Creating an extension (cog)
Inside the `misc` folder, you will find templates for commands and cogs.

Replace `categorynamegoeshere` with the category name, for example `RNG`. It's also good practice to make the extension's filename the same as this.


# Loading/Unloading an extension (cog)
Use the commands `load` or add to `startup_extensions` in config.py to load an extension. Unload them with the `unload` command.
