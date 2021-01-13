import csv
import discord
import random

users = []

token = TOKEN
client = discord.Client()

def resetUsers():
    global users
    users = []

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('+help'):
        channel = message.channel
        await channel.send("Bot commands:")
        await channel.send("1) +team: Start matchmaking")
        await channel.send("2) +me: Enter matchmaking")
        await channel.send("3) +clear: Clear matchmaking team")

    if message.content.startswith('+team'):
        channel = message.channel
        await channel.send("Matchmaking initiated! Type +me to join")
        resetUsers()

    if message.content.startswith('+clear'):
        resetUsers()

    if message.content.startswith('+me'):
        channel = message.channel
        user = message.author
        if user not in users:
            users.append(user.mention)
            await channel.send("Registered {}".format(message.author.mention))
        else:
            await channel.send("You are already registered {}".format(message.author.mention))

        if len(users) == 10:
            random.shuffle(users)
            team1 = users[:1]
            team2 = users[1:]


            await channel.send("Team 1:")
            await channel.send('\n'.join(team1))
            await channel.send("Team 2:")
            await channel.send('\n'.join(team2))
            resetUsers()

client.run(token)