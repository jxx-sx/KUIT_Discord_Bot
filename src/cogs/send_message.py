import discord


async def send_message(ctx, message):
    if isinstance(ctx, discord.Interaction):
        await ctx.response.send_message(message)
    else:
        await ctx.send(message)
