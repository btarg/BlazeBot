# USB toggle commands for BlazeBot (cog)

import discord
from discord.ext import commands
import config

class usb(commands.Cog):
    def __init__(self, client):
        self.client = client

    # WARNING - use these commands at your own risk!
    # These commands only work on the Raspberry Pi.
    @commands.command()
    async def usbon(self, ctx):  # All USBs on
        try:
            if not os.name == 'nt':
                os.system("echo '1-1' | sudo tee /sys/bus/usb/drivers/usb/bind")
                await self.ctx.send(":ballot_box_with_check: **USB input turned on.**")
                print("USB input turned on.")
            else:
                await self.ctx.send(config.err_mesg_pi)
        except:
            await self.ctx.send(config.err_mesg)

    @commands.command()
    async def usboff(self, ctx):  # All USBs off
        try:
            if not os.name == 'nt':
                os.system(
                    "echo '1-1' | sudo tee /sys/bus/usb/drivers/usb/unbind")
                await self.ctx.send(":ballot_box_with_check: **USB input turned off.**")
                print("USB input turned off.")
            else:
                await self.ctx.send(config.err_mesg_pi)
        except:
            await self.ctx.send(config.err_mesg)


def setup(client):
    client.add_cog(usb(client))
