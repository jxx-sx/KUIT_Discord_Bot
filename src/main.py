import discord
from discord import app_commands
from discord.ext import commands
from config import token

bot = commands.Bot(command_prefix='#', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')
    try:
        synced = await bot.tree.sync()
    except Exception as e:
        print(e)


@bot.tree.command(name='hello', description='Hello, KUIT')
async def hello(interaction):
    await interaction.response.send_message('```printf("Hello, KUIT");```')
    # await interaction.channel.send('```printf("Hello, KUIT");```')


@bot.tree.command(name='핑', description='퐁')
async def ping(interaction):
    await interaction.response.send_message(f"퐁! 현재 latency: {bot.latency * 1000:.0f}ms")


bot.run(token)
