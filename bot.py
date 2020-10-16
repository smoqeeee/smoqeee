import os

import discord
from discord.ext import commands

client = commands.Bot(command_prefix='l!')


@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print('-----')
    await client.change_presence(activity=discord.Game(name='' ,emoji='🖥️'))
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
