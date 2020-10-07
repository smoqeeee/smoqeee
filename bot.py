import discord
from discord.ext import commands
import asyncio
import os
import requests

client = commands.Bot(command_prefix = 's!')

@client.event
async def on_ready():
  print('logged in as smoqeee')
  await client.change_presence(activity=discord.Streaming(name="LunaticService", url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"))

        


client.run(str(os.environ.get('BOT_TOKEN')))
