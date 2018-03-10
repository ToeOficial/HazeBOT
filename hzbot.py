# HZBot desenvolvido por T0E

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

client = discord.Client()

description = '''Oi sou o HZBot!'''

client = commands.Bot(command_prefix='#', description=description)

@client.event
async def on_ready():
    print ("Iniciando...")
    print ("Estou pronto!" + client.user.name)
    print ("Meu ID é:" + client.user.id)
    await client.change_presence(game=discord.Game(name='www.HazeForum.com'))

@client.event
async def on_member_join(member):
    await client.send_message(member.server, "Seja bem-vindo {0.mention}, espero que você tenha uma ótima estadia!".format(member))


@client.command(pass_context=True)
async def ping(ctx):
    await client.say(":ping_pong: Pong!!! x222")
    print ("Histórico: O comando PING foi utilizado")

@client.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="Stalkeando {}".format(user.name), description="Uuhh! Nudes???.", color=0x00ff00)
    embed.add_field(name="Nome", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Estado", value=user.status, inline=True)
    embed.add_field(name="Cargo", value=user.top_role)
    embed.add_field(name="Juntou-se em", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def servidor(ctx):
    embed = discord.Embed(title="Nosso servidor",name="Haze Fórum".format(ctx.message.server.name), description="Saiba mais sobre nosso servidor.", color=0x00ff00)
    embed.add_field(name="Nome", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Cargos", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Membros", value=len(ctx.message.server.members))
    embed.add_field(name="Nosso site", value="www.hazeforum.com")
    embed.add_field(name="Facebook", value="www.fb.com/HazeOFC")
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def embed(ctx):
    embed = discord.Embed(title="text", description="Jhefin Gay", color=0x00ff00)
    embed.set_footer(text="rodapé teste")
    embed.set_author(name="T0E")
    embed.add_field(name="Hello darkness my old friend...", value="I've come to talk with you again...", inline=True)
    await client.say(embed=embed)
client.run("NDA1NzY5NTU3NDQyMTY2Nzg0.DYV-Pw.1a9BWnyQOdmjpyBuL6eat5BEHCs")
