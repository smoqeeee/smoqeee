import discord
import asyncio
import os
import requests
class MyClient(discord.Client):
    async def on_ready(self):
        print("logged in")

    async def on_message(self, message):
      if message.author == client.user:
            return

      if message.content.startswith("Hello"):
          await message.channel.send('Hello there.')

      if message.content.startswith("hello"):
          await message.channel.send('Hello there.')







client = MyClient()
client.run(str(os.environ.get('BOT_TOKEN')))
