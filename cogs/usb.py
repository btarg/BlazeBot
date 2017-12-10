#USB toggle commands for BlazeBot (cog)
import discord
from discord.ext import commands

class usb():
    def __init__(self, client):
        self.client = client


    #These commands only work on the Raspberry Pi.
    @commands.command(pass_context = True)
    async def usbon(self, ctx): #All USBs on
        try:
            if not os.name == 'nt':
                os.system("echo '1-1' | sudo tee /sys/bus/usb/drivers/usb/bind")
                await self.client.say(":ballot_box_with_check: **USB input turned on.**")
                print("USB input turned on.")
            else:
                await self.client.say(config.err_mesg_pi)
        except:
            await self.client.say(config.err_mesg)


    @commands.command(pass_context = True)
    async def usboff(self, ctx): #All USBs off
        try:
            if not os.name == 'nt':
                os.system("echo '1-1' | sudo tee /sys/bus/usb/drivers/usb/unbind")
                await self.client.say(":ballot_box_with_check: **USB input turned off.**")
                print("USB input turned off.")
            else:
                await self.client.say(config.err_mesg_pi)
        except:
            await self.client.say(config.err_mesg)



def setup(client):
    client.add_cog(usb(client))
