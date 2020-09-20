import discord
from discord.ext import commands
import asyncio
import os
import requests

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
  print('logged in as smoqeee')
  await client.change_presence(activity=discord.Streaming(name="shoppy.gg/@LunaticService", url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"))

    
@client.command()
async def commands(ctx):
 await ctx.send('Current Commands: There arent any :KEKW: ')
        


client.run(str(os.environ.get('BOT_TOKEN')))
