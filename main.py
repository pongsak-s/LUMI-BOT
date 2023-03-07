import discord
import os
from discord.ext import commands
from lumi import get_lumi_price, get_lumi_price_usd, get_lumi_series
from plot import plot
import base64
import io
from exchange import get_usdthb

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0}'.format(bot.user))

@bot.command()
async def justprice(ctx):
    await ctx.send(get_lumi_price())

@bot.command()
async def price(ctx):
    lumi_series = get_lumi_series()
    lumi_usd = get_lumi_price_usd(lumi_series)
    await ctx.send(get_lumi_price(lumi_usd))
    lumi_thb="{:.2f}".format(lumi_usd* get_usdthb())
    await ctx.send("ราคาไทย: "+lumi_thb+" บาท")
    await ctx.send("one sec. we are fetching the chart ...... (v2)")
    png_base64 = base64.b64encode(plot(lumi_series)).decode('ascii')
    file = discord.File(io.BytesIO(base64.b64decode(png_base64)), filename="image.png")
    await ctx.send(file=file)

@bot.command()
async def test(ctx):
    print(read_file())
    write_file(33.31)
    await ctx.send(get_lumi_price())

bot.run(os.getenv('TOKEN'))
