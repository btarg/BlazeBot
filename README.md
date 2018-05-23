# BlazeBot
A multipurpose Discord bot written in Python with the [discord.py](https://github.com/Rapptz/discord.py) module.

[![Discord.py](https://img.shields.io/pypi/v/discord.py.svg)](https://pypi.python.org/pypi/discord.py/)
[![Python](https://img.shields.io/badge/Python-3.5%2C%203.6-blue.svg)](https://python.org/)
[![BlazeBot](https://img.shields.io/badge/BlazeBot%20version-1.5.5-brightgreen.svg)](https://icrazyblaze.github.io/BlazeBot)

# Installing dependencies
The following packages are required to run (as well as [Python](https://python.org) 3.5 or over):

```
python -m pip install requests
```

```
python -m pip install discord
```

However, to easily setup BlazeBot and change tokens and API keys at any time, you should use the `Setup-Linux.sh` script, or if you're on Windows, `Setup-Windows.bat` script to launch the setup.

If these commands don't work, try using `python3.6` or `python3` instead of the regular command, or use `sudo` on Linux.

You can also use the scripts found in the `misc` folder that will do this for you. Remember to run the `Python35` version if you're using Python 3.5! However, these are deprecated, and you should use the new `setup.py` script to set up the bot.

# Downloading the source code
To download with Git, type this command into a terminal:
```
git clone https://github.com/iCrazyBlaze/BlazeBot
```
Alternatively, you can use the [GitHub Desktop Client](https://desktop.github.com/) to download it. (Recommended!)

You can also download the repository as a ZIP or TAR file, but I don't recommend doing this.

If you're on Linux and you want to be able to easily clone and update BlazeBot, you can use [this script](https://gist.github.com/iCrazyBlaze/c2e4413ba4700083355833100d262d10) which will remove the `BlazeBot` directory if it exists (otherwise it will just say "directory not found") before using the `git clone` command to download the code. This has proved really useful for me when I'm using multiple machines.

To run the script on Windows with [Git Bash](https://git-scm.com/downloads), delete `sudo` from the first line and it should run.

# Setting up and config
BlazeBot comes with a `config.py` file. Here you will add your Discord App token, and add startup extensions. You can generate a token at *https://discordapp.com/developers/applications/me.*

Find the string `"token here"` in the config file and replace it with your token.

In the `config.py` file, you can also customise insults, error messages, bot prefix, bot description and the file you want the bot to log events to.


# Creating an extension (cog)
Inside the `misc` folder, you will find templates for commands and cogs.

Replace `test` with the category name, for example `Crazi`. Also, make sure the extension's filename the same as this, to avoid confusion.

You can refer to [this documentation](https://twentysix26.github.io/Red-Docs/red_guide_make_cog/) for how to create a cog, and you can find examples of existing cogs [here](https://gist.github.com/leovoel/46cd89ed6a8f41fd09c5), but make sure to replace all instances of `bot` with `client`, which is what BlazeBot uses.


# Loading/Unloading an extension (cog)
Use the command `load` to load commands from `startup_extensions` in config.py. You can unload them separately with the `unload` command.

You can also load cogs from a folder, by using the format: `folder.filename`

BlazeBot loads the `Crazi.py` plugin from the `cogs` folder.

# Starting the bot
On Windows, the bot can be started using the `BlazeBot-Windows.bat` file.

On Linux/Unix, the bot can be started using the `BlazeBot-Linux.sh` file. (This only works with Python 3.6.X - if you're using Python 3.5 then make sure you use the `BlazeBot-Python35.sh` Launcher instead.)

I recommend on any Linux system that you use [Thonny](http://thonny.org) or [IDLE](https://python.org) (Python's default code editor).

# Inviting to servers
Use the [Discord Permissions Calculator](https://discordapi.com/permissions.html) to invite the bot to your server using the ID printed to the console, and make sure that it has admin permissions.

If you want to invite your bot to other people's servers, make sure to tick "Public bot" on the Apps page.

# Speech Recognition
**Speech-to-Discord** lets you type a command and talk to BlazeBot, and it will send your message to the same channel where you typed the command. By default, this cog is disabled. To enable it, add it to `startup_extensions` in the config file. You will need a microphone so that the program can recognise your voice (duuhh...), and it works best on Windows 10.

# Tips
Make sure to always update BlazeBot. You can create [GitHub Webhooks for Discord](https://support.discordapp.com/hc/en-us/articles/228383668-Intro-to-Webhooks) to get notified whenever a repo is updated.

When you do this, always keep a backup! It's also useful to write down your token, but **NEVER** give this to anyone you don't trust. Don't worry though - you can generate a new token whenever you want on the Apps page.

To read this properly offline, [Atom](https://atom.io) has a built-in Markdown Previewer that you can open by hitting **CTRL+SHIFT+M** on a PC or **CMD+SHIFT+M** on a Mac.

# See Also
Here are some useful GitHub repositories related to BlazeBot:

https://github.com/Cog-Creators/Red-DiscordBot

https://github.com/Rapptz/discord.py
