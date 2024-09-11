import discord
import random
import os
from bot_logic import gen_pass
from bot_logic import get_duck_image_url
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = "$",intents=intents)

@bot.event
async def on_ready():
    print(f'hemos iniciado sesion como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola!')

@bot.command()
async def bye(ctx):
    await ctx.send(f'Nos vemos :c')

@bot.command()
async def password(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def mem(ctx):
    with open('images/mem1.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def mem_ale(ctx):
    mem_alet = random.choice(os.listdir("images"))
    with open(f'images/{mem_alet}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)
