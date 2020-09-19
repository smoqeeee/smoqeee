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
       await client.change_presence(game=discord.Activity(name="https://shoppy.gg/@LunaticService"))

    async def on_message(self, message):
      if message.author == client.user:
            return

      if message.content.startswith("Hello"):
          await message.channel.send('Hello there.')

      if message.content.startswith("hello"):
          await message.channel.send('Hello there.')

      if message.content.startswith("du hurensohn"):
          await message.channel.send('du')





client = MyClient()
client.run(str(os.environ.get('BOT_TOKEN')))
