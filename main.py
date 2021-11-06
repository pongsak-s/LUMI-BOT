import discord
import os
from lumi import get_lumi_price, get_lumi_price_usd
from plot import plot
import base64
import io
from exchange import get_usdthb

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$justprice'):
        await message.channel.send(get_lumi_price())

    if message.content.startswith('$price'):
        await message.channel.send(get_lumi_price())
        lumi_thb="{:.2f}".format(get_lumi_price_usd()*get_usdthb())
        await message.channel.send("ราคาไทย: "+lumi_thb+" บาท")
        await message.channel.send("one sec. we are fectching the chart ......")
        png_base64 = base64.b64encode(plot()).decode('ascii')
        file = discord.File(io.BytesIO(base64.b64decode(png_base64)), filename="image.png")
        await message.channel.send(file=file)


client.run(os.getenv('TOKEN'))
