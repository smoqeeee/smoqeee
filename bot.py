import discord
from discord.ext import commands
import asyncio
import os
import requests




 
class MyClient(discord.Client):
 

    async def on_ready(self):
       print("logged in as smoqeee V1.0")
       print(client.user.name)
       print(client.user.id)
       print("------------")
       await client.change_presence(activity=discord.Streaming(name="shoppy.gg/@LunaticService", url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"))

    async def on_message(self, message):
      if message.author == client.user:
            return
       
client = commands.Bot(command_prefix='!')
@client.command()
async def info(ctx):
 await ctx.send('test')
        


client = MyClient()
client.run(str(os.environ.get('BOT_TOKEN')))
