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

       
      if message.content.startswith("Hello"):
          await message.channel.send('Hello there.')

      if message.content.startswith("hello"):
          await message.channel.send('Hello there.')

      if message.content.startswith("du hurensohn"):
          await message.channel.send('du')
            
      if message.content.startswith("king"):
          await message.channel.send('spiegel')
      
      if message.content.startswith("!invites"):
          await message.channel.send('Its .invites brother')
        
 from discord.ext import commands
        bot = commands.Bot(command_prefix='!')

@bot.command()
async def say(ctx, *, arg):
    await ctx.send(arg)


@say.error
async def say_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please tell me what to say')

     


client = MyClient()
client.run(str(os.environ.get('BOT_TOKEN')))
