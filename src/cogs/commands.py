import discord


async def hello(ctx):
    message = '```c\nprintf("Hello, KUIT");```'
    if (type(ctx) == discord.Interaction):
        await ctx.response.send_message(message)
    else:
        await ctx.send(message)


async def ping(ctx, bot: discord.ext.commands.bot):
    if (type(ctx) == discord.Interaction):
        await ctx.response.send_message(f"퐁! 현재 latency: {bot.latency * 1000:.0f}ms")
    else:
        await ctx.send(f"퐁! 현재 latency: {bot.latency * 1000:.0f}ms")


async def join(interaction):
    if interaction.user.voice and interaction.user.voice.channel:
        channel = interaction.user.voice.channel
        await channel.connect()
        message = f"{channel} 연결됨"
    else:
        message = "음성채널 없음"
    await interaction.response.send_message(message)


async def birth(ctx):
    message = '쿠잇 생일? 23년 3월 14일! 🎉\n내 생일? 23년 5월 17일! 🥳'
    if (type(ctx) == discord.Interaction):
        await ctx.response.send_message(message)
    else:
        await ctx.send(message)


async def help(ctx):
    message = '빗금(/)를 입력해 명령어를 고르거나 느낌표(!) 뒤에 아래에 나오는 명령어를 붙여서 써주세요\n```[ hello ]: Hello KUIT!\n[ 핑, ping, p]: 봇 상태 확인\n[ birth, b, 생일 ]: 쿠잇 기념일\n[ h, 도움, 도움말 ]: 도움말```'
    if (type(ctx) == discord.Interaction):
        await ctx.response.send_message(message)
    else:
        await ctx.send(message)
