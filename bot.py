import os

import discord
from discord.ext import commands

client = commands.Bot(command_prefix='l!')


@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print('-----')
    activity = discord.Game(name="s! | Lunatic", type=3)
    await client.change_presence(status=discord.Status.DnD, activity=activity)
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
