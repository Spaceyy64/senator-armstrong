import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import os
import logging
from keep_alive import keep_alive

#making the bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='?', help_command=None, intents=intents)

#Making console-logs
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        em = discord.Embed(title="Sorry 😥", color = 65841)
        em.add_field(name="No such command!", value="Get a list of commands by `help`")
        await ctx.send(embed = em)

#checking for bot's connection
@bot.event
async def on_ready():
    print(f'Successfull Connection! Logged in as:\n{bot.get_user(1235601420141592707)}')
    #bot status
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Theअखण्ड भारत Discord Server!", url="https://dsc.gg/theakhandbharat", state="Active", details="Right for the Might💪", assets="maurya_flag", large_image="https://i.imgur.com/a/5Jr68r2", large_image_text="WARNING: EXTREMELY RIGHTIST"))
    
    #cogs
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

keep_alive()
bot.run(os.getenv('TOKEN'))