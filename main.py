import discord
import os
from lumi import get_lumi_price, get_lumi_price_usd, get_lumi_series
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
        lumi_series = get_lumi_series()
        lumi_usd = get_lumi_price_usd(lumi_series)
        await message.channel.send(get_lumi_price(lumi_usd))
        lumi_thb="{:.2f}".format(lumi_usd* get_usdthb())
        await message.channel.send("ราคาไทย: "+lumi_thb+" บาท")
        await message.channel.send("one sec. we are fectching the chart ......")
        png_base64 = base64.b64encode(plot(lumi_series)).decode('ascii')
        file = discord.File(io.BytesIO(base64.b64decode(png_base64)), filename="image.png")
        await message.channel.send(file=file)

    if message.content.startswith('$test'):
        print(read_file())
        write_file(33.31)
        await message.channel.send(get_lumi_price())

client.run(os.getenv('TOKEN'))
