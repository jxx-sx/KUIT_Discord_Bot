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
