import discord
from discord import *
from discord.ext import commands
from config import token

bot = commands.Bot(command_prefix='#', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')


@bot.command()
async def hello(message):
    await message.channel.send('```printf("Hello, KUIT");```')


@bot.command()
async def ping(message):
    await message.send(f"pong! latency: {bot.latency * 1000}ms")


bot.run(token)
