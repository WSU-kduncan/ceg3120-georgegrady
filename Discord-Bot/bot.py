import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    quotes = [
        'Not knowing you cannot do something, is sometimes all it takes to do it. - Ally Carter',
        'If people make fun of you, that probably means you are doing something right. - Evanescence',
        'I have had a lot of worries in my life, most of which never happened. - Mark Twain',
        'If we all did the things we are really capable of doing, we would literally astound ourselves. - Thomas A. Edison',
    ]

    if message.content == '!motivateme':
        response = random.choice(quotes)
        await message.channel.send(response)

client.run(TOKEN)
