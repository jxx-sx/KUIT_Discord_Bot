import discord
from discord import app_commands
from discord.ext import commands
from config import token

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')
    try:
        synced = await bot.tree.sync()
    except Exception as e:
        print(e)


@bot.tree.command(name='hello', description='Hello, KUIT')
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message('```printf("Hello, KUIT");```')


@bot.tree.command(name='핑', description='퐁')
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"퐁! 현재 latency: {bot.latency * 1000:.0f}ms")


@bot.tree.command(name='voice', description='test')
async def join(interaction: discord.Interaction):
    if interaction.user.voice and interaction.user.voice.channel:
        channel = interaction.user.voice.channel
        await channel.connect()
        message = f"{channel} 연결됨"
    else:
        message = "음성채널 없음"
    await interaction.response.send_message(message)


bot.run(token)
