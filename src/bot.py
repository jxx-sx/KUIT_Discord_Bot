import discord
from discord import app_commands
from discord.ext import commands
from cogs.commands import *

from config import token

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')
    try:
        synced = await bot.tree.sync()
    except Exception as e:
        print(e)


# prefix commands

@bot.command(name='hello')
async def hello_command(ctx):
    await hello(ctx)


@bot.command(name='핑', aliases=['ping', 'p'])
async def ping_command(ctx):
    await ping(ctx, bot)


@bot.command(name='생일')
async def birth_command(ctx):
    await birth(ctx)

# slash commands


@bot.tree.command(name='hello', description='Hello, KUIT')
async def hello_slash_command(ctx):
    await hello(ctx)


@bot.tree.command(name='핑', description='핑? 퐁!')
async def ping_slash_command(ctx):
    await ping(ctx, bot)


@bot.tree.command(name='생일', description='내 생일이 궁금해?')
async def birth_slash_command(ctx):
    await birth(ctx)

# @bot.tree.command(name='voice', description='on Develop')
# async def join_command(ctx):
#     await join(ctx)


bot.run(token)
