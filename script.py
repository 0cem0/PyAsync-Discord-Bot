import asyncio
import discord
from discord.ext import commands
import aiohttp
import requests
import json

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"[+] Bot connecté en tant que {bot.user.name} (ID: {bot.user.id})")
    print("--------------------------------------------------")


@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    if "bonjour" in message.content.lower():
        await message.channel.send(f"Salut {message.author.mention} ! 👋")

    await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    latence = round(bot.latency * 1000)
    await ctx.send(f"Latence : **{latence}ms**")

@bot.command()
async def timer(ctx, secondes : int):
     await ctx.send(f"Minuteur lancé pour {secondes} secondes...")
     
     await asyncio.sleep(secondes)

     await ctx.send(f"🔔 {ctx.author.mention}, ton minuteur de {secondes}s est terminé !")

@bot.command()
async def crypto(ctx, nom_crypto: str):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={nom_crypto.lower()}&vs_currencies=eur"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as reponse:

            data = await reponse.json()

            prix = data.get(nom_crypto.lower(), {}).get("eur")

            if prix:
                await ctx.send(
                    f"Le prix de {nom_crypto} est de **{prix} €**"
                )
            else:
                await ctx.send(f"Crypto {nom_crypto} introuvable.")

if __name__ == "__main__":
    TOKEN = "PLACEHOLDER"
    bot.run(TOKEN)


