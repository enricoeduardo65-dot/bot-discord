import discord
import random
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def multiplies(ctx, left: int, right: int):
    """ multiplies two numbers together."""
    await ctx.send(left * right)

@bot.command()
async def divides(ctx, left: int, right: int):
    """ divides two numbers together."""
    await ctx.send(left / right)

@bot.command()
async def meme_aleatorio(ctx):
    imagens = os.listdir("images") 

    img_name = random.choice(imagens)
    with open(os.path.join("images", img_name), "rb") as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def subtrat(ctx, left: int, right: int):
    """ subtract  two numbers together."""
    await ctx.send(left - right)



bot.run("")


