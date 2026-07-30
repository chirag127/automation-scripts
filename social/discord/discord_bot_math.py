#  make a discord bot that can do math problems and send the answer to a channel

# for example, if someone types in 2+2, the bot will send 4 to the channel

import re

import discord

client = discord.Client(intents=discord.Intents.default())
math_pattern = re.compile(r"(\d+)([+-/*])(\d+)")


@client.event
async def on_message(message):
    if message.author == client.user:
        print("Message from bot")
        return

    if message.content.startswith("h"):
        print("Message from user")
        await message.channel.send("Hello!")

    if math_pattern.match(message.content):
        print("Message from user")
        await message.channel.send(eval(message.content))


import os

client.run(os.environ.get("DISCORD_BOT_TOKEN"))
