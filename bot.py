import os

import discord
from discord.ext import commands

client = commands.Bot(command_prefix='l!')


@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print('-----')


newUserMessage = """ 
    Welcome
    to
    Lunatic Service!
   
 """

@client.event
async def on_member_join(member):
    print("Recognised that a member called " + member.name + " joined")
    try: 
    await client.send_message(member, newUserMessage)
    print("Sent message to " + member.name)
    except:
        print("Couldn't message " + member.name)

@client.command()
async def test(ctx):
    await ctx.send('not ready yet ')


@client.command()
async def commands(ctx):
    await ctx.send('Current Commands: l!lenny ')


@client.command()
async def lenny(ctx):
    await ctx.send('( ͡° ͜ʖ ͡°) ')


client.run(str(os.environ.get('BOT_TOKEN')))
