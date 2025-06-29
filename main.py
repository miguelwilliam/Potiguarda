import discord
import json
from discord.ext import commands

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Bot está online!') 

@bot.command()
async def oi(ctx):
    await ctx.send(f'Oi, {ctx.author.mention}!')

@bot.command(aliases=['bd', 'dia'])
async def bomdia(ctx):
    await ctx.send(f'Bom dia, {ctx.author.mention}!')

# Exemplo de Embed:
@bot.command()
async def sendembed(ctx):
    embedded_msg = discord.Embed(title="Título do Embed", description="Descrição do Embed", color=discord.Color.dark_theme())
    embedded_msg.set_thumbnail(url=ctx.author.avatar)
    embedded_msg.add_field(name="Nome do field", value="Valor do field", inline=False)
    embedded_msg.set_image(url=ctx.guild.icon)
    embedded_msg.set_footer(text="Texto do footer", icon_url=ctx.author.avatar)

    await ctx.send(embed=embedded_msg)

@bot.command()
async def fichas(ctx):
    embedded_msg = discord.Embed(title="Pesquisa de fichas", description="Pesquisando ficha...", color=discord.Color.random())

    embed_field_value = ''

    ficha1 = {"nome": "miguel William", "classe": "Ladino", "Vida atual": 10, "Vida máxima": 12}

    for valor in ficha1:
        embed_field_value += f'{valor}: {ficha1[valor]}\n \n'

        

    embedded_msg.set_thumbnail(url=ctx.author.avatar)
    embedded_msg.add_field(name="Ficha #1", value=embed_field_value, inline=False)
    embedded_msg.set_image(url=ctx.guild.icon)
    embedded_msg.set_footer(text=f"Solicitado por {ctx.author.name}", icon_url=ctx.author.avatar)

    await ctx.send(embed=embedded_msg)

@bot.command()
async def ping(ctx):
    ping_embed = discord.Embed(title="Ping", description="Latência em ms", color=discord.Color.green())
    ping_embed.add_field(name=f"Latência de {bot.user.name}: ", value=f"{round(bot.latency * 1000)}ms", inline=True)
    ping_embed.set_footer(text=f"Solicitado por {ctx.author.name}", icon_url=ctx.author.avatar)
    await ctx.send(embed=ping_embed)

# === bot.run ===
with open('config.json', 'r') as f:
    config = json.load(f) # Lendo json
    
    Token = config['token']

bot.run(token=Token)