import discord
from discord.ext import commands
import datetime

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# カレンダーに予定を追加するコマンド
@bot.command()
async def add_event(ctx, date_str, *, event):
    date = datetime.datetime.strptime(date_str, '%Y/%m/%d')
    calendar_channel = bot.get_channel(1234567890) # カレンダーを表示するチャンネルのIDを入力
    await calendar_channel.send(f'{date.date()}: {event}')

# 今日の予定を表示するコマンド
@bot.command()
async def today_events(ctx):
    today = datetime.datetime.now().date()
    calendar_channel = bot.get_channel(1234567890) # カレンダーを表示するチャンネルのIDを入力
    async for message in calendar_channel.history(limit=None):
        if today == datetime.datetime.strptime(message.content.split(':')[0], '%Y-%m-%d').date():
            await ctx.send(message.content.split(':')[1])

bot.run('your_bot_token_here')
