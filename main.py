import os
import discord
from webserver import webserver
#my_secret = os.environ['TOKEN']

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$orewaochinchingadaisukinandayo'):
    await message.channel.send(file=discord.File('./memes/bidenblast.jpg'))

  if message.content.startswith('$ass'):
    await message.channel.send(file=discord.File('./memes/as.jpg'))

  if message.content.startswith('$helpme'):
    await message.channel.send(file=discord.File('./memes/indonesian.jpeg'))

webserver()
client.run(os.getenv('TOKEN'))
