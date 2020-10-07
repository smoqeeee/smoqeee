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
  
@client.command()
async def commands(ctx):
await ctx.send('Current Commands: s!lenny ')

@client.command()
async def lenny(ctx):
await ctx.send('( ͡° ͜ʖ ͡°) ')
        


client.run(str(os.environ.get('BOT_TOKEN')))
