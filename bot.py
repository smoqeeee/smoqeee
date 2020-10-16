import discord
from discord.ext import commands
import asyncio
import os
import requests

client = commands.Bot(command_prefix='l!')


@client.event
async def on_ready():
    print('logged in as smoqeee')
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



client.run(str(os.environ.get('BOT_TOKEN')))
