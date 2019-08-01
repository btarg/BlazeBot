# BlazeBot 2 (beta)
A multipurpose, semi-modular Discord bot written in Python with the new [discord.py](https://github.com/Rapptz/discord.py) module.

[![Discord.py](https://img.shields.io/pypi/v/discord.py.svg)](https://pypi.python.org/pypi/discord.py/)
[![Python](https://img.shields.io/badge/Python-3.5%2C%203.6%2C%203.7-blue.svg)](https://python.org/)
[![BlazeBot](https://img.shields.io/badge/BlazeBot%20version-2.0-brightgreen.svg)](https://icrazyblaze.github.io/BlazeBot)

# Installing dependencies
The following packages are required to run (as well as [Python](https://python.org) 3.5 or over):

```
python -m pip install -r requirements.txt
```

**To easily setup BlazeBot and change tokens and API keys at any time, you should use the `Setup.py` script.**

> Not working? Try replacing `python` with `py` or `python3`.

# Downloading the source code
To download with Git, type this command into a terminal:
```
git clone https://github.com/iCrazyBlaze/BlazeBot
```
Alternatively, you can use the [GitHub Desktop Client](https://desktop.github.com/) to download it.

You can also download the repository as a ZIP or TAR file.

If you're on Linux and you want to be able to easily clone and update BlazeBot, you can use [this script](https://gist.github.com/iCrazyBlaze/c2e4413ba4700083355833100d262d10) which will remove the `BlazeBot` directory if it exists (otherwise it will just say "directory not found") before using the `git clone` command to download the code. This has proved really useful for me when I'm using multiple machines.

To run the script on Windows with [Git Bash](https://git-scm.com/downloads), delete `sudo` from the first line and it should run.

# Setting up and config
BlazeBot comes with a `config.py` file. Here you will add your Discord App token, and add startup extensions. You can generate a token at *https://discordapp.com/developers/applications/me.*

Find the string `"token here"` in the config file and replace it with your token.

In the `config.py` file, you can also customise insults, error messages, bot prefix, bot description and the file you want the bot to log events to.


# Creating an extension (cog)
Inside the `misc` folder, you will find templates for commands and cogs.

Replace `test` with the command category's name. Also, make sure the extension's filename the same as this, to avoid confusion.

You can refer to [this documentation](https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html?highlight=cogs) for how to create a cog, but make sure to replace all instances of `bot` with `client`, as this is what BlazeBot uses.


# Loading/Unloading an extension (cog)
Use the command `load` to load commands from `startup_extensions` in config.py. You can unload them separately with the `unload` command.

You can also load cogs from a folder, by using the format: `folder.filename`

BlazeBot's plugins are found in the `cogs` folder.

# Starting the bot
You can start the bot by launching `BlazeBot.py` directly, or using a Python IDE such as Thonny.


# Inviting to servers
Use the [Discord Permissions Calculator](https://discordapi.com/permissions.html) to invite the bot to your server using the ID printed to the console, and make sure that it has admin permissions.

If you want to invite your bot to other people's servers, make sure to tick "Public bot" on the Apps page.


# Tips
Make sure to always update BlazeBot. You can create [GitHub Webhooks for Discord](https://support.discordapp.com/hc/en-us/articles/228383668-Intro-to-Webhooks) to get notified whenever a repo is updated.

When you do this, always keep a backup! It's also useful to write down your token, but **NEVER** give this to anyone you don't trust, or publish it to your GitHub. Don't worry though - you can generate a new token whenever you want on the Discord developer portal.

To read and edit this document properly offline, [Atom](https://atom.io/) and [VS Code](https://code.visualstudio.com/) both have a built-in Markdown Previewer that you can open by hitting <kbd>ctrl</kbd> + <kbd>shift</kbd> + <kbd>v</kbd> on a PC or <kbd>cmd</kbd> + <kbd>shift</kbd> + <kbd>v</kbd> on a Mac.

# See Also
See the discord.py repo for more information on the API: https://github.com/Rapptz/discord.py
