import discord
from discord.ext import commands
from discord import app_commands
from .send_message import *


class info(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    async def hello(self, ctx):
        message = '```c\nprintf("Hello, KUIT");```'
        await send_message(ctx, message)

    async def ping(self, ctx, bot: discord.ext.commands.bot):
        message = f"퐁! 현재 latency: {self.client.latency * 1000:.0f}ms"
        await send_message(ctx, message)

    # async def join(self, interaction):
    #     if interaction.user.voice and interaction.user.voice.channel:
    #         channel = interaction.user.voice.channel
    #         await channel.connect()
    #         message = f"{channel} 연결됨"
    #     else:
    #         message = "음성채널 없음"
    #     await interaction.response.send_message(message)

    async def birth(self, ctx):
        message = '쿠잇 생일? 23년 3월 14일! 🎉\n내 생일? 23년 5월 17일! 🥳'
        await send_message(ctx, message)

    async def help(self, ctx):
        message = '빗금(/)를 입력해 명령어를 고르거나 느낌표(!) 뒤에 아래에 나오는 명령어를 붙여서 써주세요\n```[ hello ]: Hello KUIT!\n[ 핑, ping, p]: 봇 상태 확인\n[ birth, b, 생일 ]: 쿠잇 기념일\n[ h, 도움, 도움말 ]: 도움말```\n\n또... 여러 이스터에그가 있습니다(소근)'
        await send_message(ctx, message)

    @commands.command(name='hello')
    async def hello_command(self, ctx):
        await self.hello(ctx)

    @commands.command(name='핑', aliases=['ping', 'p'])
    async def ping_command(self, ctx):
        await self.ping(ctx, self.client)

    @commands.command(name='생일', aliases=['birth', 'b'])
    async def birth_command(self, ctx):
        await self.birth(ctx)

    @commands.command(name='도움', aliases=['도움말', 'h'])
    async def help_command(self, ctx):
        await self.help(ctx)

    @app_commands.command(name='hello', description='Hello, KUIT')
    async def hello_slash_command(self, ctx):
        await self.hello(ctx)

    @app_commands.command(name='핑', description='핑? 퐁!')
    async def ping_slash_command(self, ctx):
        await self.ping(ctx, self.client)

    @app_commands.command(name='생일', description='내 생일이 궁금해?')
    async def birth_slash_command(self, ctx):
        await self.birth(ctx)

    @app_commands.command(name='도움', description='도움말!')
    async def help_slash_command(self, ctx):
        await self.help(ctx)

    @commands.Cog.listener()
    async def on_message(self, message):
        """
        message.author : 메시지를 보낸 사람
        message.guild : 메시지를 보낸 서버
        message.channel : 메시지를 보낸 채널
        """
        if message.author.bot:  # 봇이 보낸 메시지이면 반응하지 않게 합니다
            return

        if message.content == "@안녕":
            print(message.channel)
            await message.channel.send(message.author.name + "님 안녕하세요!")

        if message.content == "집에 보내줘...":
            print(message.channel)
            await message.channel.send("어딜가... 공부해야지...")

        if message.content == 'T':
            file = discord.File("./assets/T.jpg")
            await message.channel.send(file=file)

        if message.channel.category.name == 'Notice':
            await message.add_reaction("✅")

    # @app_commands.command(name='voice', description='on Develop')
    # async def join_command(self, ctx):
    #     await join(ctx)


async def setup(client: commands.Bot) -> None:
    await client.add_cog(info(client))
