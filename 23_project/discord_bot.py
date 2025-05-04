import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} is now online!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == 'hello':
        await message.channel.send('Hi there!')

client.run(TOKEN)
