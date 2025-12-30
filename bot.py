import os
import discord

TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("DISCORD_BOT_TOKEN no está definido (configúralo como GitHub Secret).")

intents = discord.Intents.default()
intents.message_content = True  # requiere Message Content Intent activado en el portal

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Conectado como {client.user} (id={client.user.id})")

@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    print(f"[{message.guild}#{message.channel}] {message.author}: {message.content}")

    txt = message.content.lower().strip()
    if txt == "hola":
        await message.channel.send("Hola, soy un bot básico (GitHub Actions).")
    elif txt == "!ping":
        await message.channel.send("pong")

client.run(TOKEN)
