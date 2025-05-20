import discord
from discord.ext import commands, tasks
from currency_api import CurrencyAPI
from config import TOKEN, API_KEY, CHANNEL_ID
from datetime import datetime

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

bot = commands.Bot(command_prefix='!', intents=intents)
api = CurrencyAPI(API_KEY)

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} jest gotowy!')
    aktualizuj_kursy.start()

@tasks.loop(hours=1)
async def aktualizuj_kursy():
    channel = bot.get_channel(CHANNEL_ID)
    if not channel:
        return

    try:
        kursy = api.pobierz_kursy("USD", ["EUR", "PLN", "UAH"])
        embed = discord.Embed(
            title="Kursy walut",
            description=datetime.now().strftime("%d.%m.%Y %H:%M"),
            color=0x00ff00
        )
        
        for waluta, kurs in kursy.items():
            embed.add_field(name=f"1 USD → {waluta}", value=f"{kurs:.2f}")
            
        await channel.send(embed=embed)
    except Exception as e:
        print(f"Blad aktualizacji: {e}")

@bot.command()
async def przelicz(ctx, kwota: float, z_waluty: str, na_walute: str):
    try:
        wynik = api.konwertuj(kwota, z_waluty.upper(), na_walute.upper())
        await ctx.send(
            f"{kwota} {z_waluty.upper()} = "
            f"{wynik['przeliczona_kwota']:.2f} {na_walute.upper()}\n"
            f"Kurs: 1 {z_waluty.upper()} = {wynik['kurs']:.4f}"
        )
    except Exception as e:
        await ctx.send(f"Blad: {str(e)}")

bot.run(TOKEN)