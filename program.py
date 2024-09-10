import discord
from bot_logic import gen_pass
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(commands_prifix = "$",intents=intents)


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
async def bye(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
