import discord
import os
from lumi import get_lumi_price

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$price'):
        await message.channel.send(get_lumi_price())


client.run(os.getenv('TOKEN'))
