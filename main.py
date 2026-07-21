import discord, requests, pyttsx3, random
from discord.ext import commands

engine = pyttsx3.init()
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def start(ctx):
    await ctx.send("!Hola, soy un bot que anuncia datos aleatorios!")
def get_information():
    base_url = "https://newsapi.org/v2/everything?q=climate+change&language=es&apiKey=8ec8ad43ca8a4303a767412ceec20fd3"

    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()

        return data["articles"][random.randint(0, 17)]["description"]
    else:
        return "No se pudo obtener información <(＿　＿)>."


@bot.command()
async def fact(ctx):
    fact_info = get_information()
    print(fact_info)
    await ctx.send(f"¡Here is a fact: {fact_info}! ^_^")
    speak(fact_info)

def speak(text:str):
    engine.say(text)
    engine.runAndWait()

@bot.command()
async def meme(ctx):
    

bot.run("MTQzMjg3Njk4OTExNDYxNzk5MQ.GDhDSQ.r6IJn68_y2gmvhoA8q4BIf7jUxIxY9SoUrGTdI")
