import os

import discord
from discord.ext import commands

client = commands.Bot(command_prefix='l!')


@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')

await client.change_presence(
    activity=discord.Activity(type=discord.ActivityType.watching, name="users"))

@client.command()
async def test(ctx):
    await ctx.send('not ready yet ')


@client.command()
async def commands(ctx):
    await ctx.send('Current Commands: l!lenny ')


@client.command()
async def lenny(ctx):
    await ctx.send('( ͡° ͜ʖ ͡°) ')

newUserDMMessage = "WELCOME!"
# Public Welcome
@client.event
async def on_member_join(member):
    print("Recognized that " + member.name + " joined")
    await client.send_message(member, newUserDMMessage)
    await client.send_message(discord.Object(id='746442045052157952'), 'Welcome!')
    print("Sent message to " + member.name)
    print("Sent message about " + member.name + " to #🌌〕new-people")


client.run(str(os.environ.get('BOT_TOKEN')))
