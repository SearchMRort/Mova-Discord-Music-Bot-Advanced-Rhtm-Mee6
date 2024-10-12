from discord.ext import commands
import discord
import os


default_intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

@bot.event
async def on_ready():
  game = discord.Game('currently being updated, please wait around 30 mins.')
  await bot.change_presence(status=discord.Status.idle, activity=game)
  print("Bot is afk")


bot.run(os.environ['TOKEN'])
