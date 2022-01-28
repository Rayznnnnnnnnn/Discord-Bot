import discord
import os
from discord.ext import commands
from discord.ext.commands import bot
from discord import FFmpegPCMAudio

client = commands.Bot(command_prefix="?")

@client.event
async def on_message(message):
    if message.content.startswith('?ER'):
        await message.channel.send("As u say master")
        channel = message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio("song.  mp3")
        player = voice.play(source)
        voice.play(discord.FFmpegPCMAudio(source="song.mp3"))
        await message.channel.send("As u say master")






    elif message.content.startswith("?dc"):
        channel = message.author.voice.channel
        voice = await channel.connect()
        voice.play(discord.FFmpegPCMAudio(source="audio.wav"))
        await voice.disconnect
        await message.channel.send("Disconnected")






    elif message.content.startswith("fuck you"):
        await message.channel.send(file=discord.File("violation.mp4"))

    elif message.content.startswith("sure bro"):
        await message.channel.send(file=discord.File("opinion.jpg"))

    elif message.content.startswith("?commands"):
        await message.channel.send(" ```  Here's a list of my commands- "
                                   "                                    ?help "
                                   "                                         ?!ER"
                                   "                                    fuck you"
                                   "                                    sauce"
                                   "                                    violation"
                                   "                                   sure bro"
                                   "                                    fuck off"
                                   "                                    🤡"
                                   "                                    caught in 4k"
                                   "                                down bad    ``` ")

    elif message.content.startswith("sauce"):
        await message.channel.send(file=discord.File("bonk2.jpg"))

    elif message.content.startswith("Fuck you"):
        await message.channel.send(file=discord.File("violation.mp4"))

    elif message.content.startswith("that was a violation"):
        await message.channel.send(file=discord.File("violation.mp4"))

    elif message.content.startswith("Fuck off"):
        await message.channel.send(file=discord.File("violation.mp4"))

    elif message.content.startswith("fuck off"):
        await message.channel.send(file=discord.File("violation.mp4"))

    elif message.content.startswith("🤡"):
        await message.channel.send(file=discord.File("koimidi_king.jpg"))


    elif message.content.startswith("caught in 4k"):
        await message.channel.send(file=discord.File("caught.jpg"))


    elif message.content.startswith("down bad"):
        await message.channel.send("yes im down bad")
        await message.channel.send(file=discord.File("preview.jpg"))

    elif message.content.startswith("violation"):
        await message.channel.send(file=discord.File("violation.mp4"))

    




    elif message.author == client.user:
        return

    elif message.content.startswith('?help'):
        await message.channel.send('Hi ┌(ಠ‿ಠ)┘ , want to troll your friends? use me! use !ER to get started!,type ?commands to get the list of the other commands.')







client.run(";-;")