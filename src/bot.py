import discord
import os
from discord import app_commands
from discord.ext import commands
from config import token


class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!', intents=discord.Intents.all())

    async def on_ready(self):
        print(f'Login bot: {self.user}')
        try:
            await self.tree.sync()
        except Exception as e:
            print(e)

    async def setup_hook(self):
        ext_list = ['cogs.info']
        for ext in ext_list:
            await self.load_extension(ext)


client = Client()

client.run(token)
    