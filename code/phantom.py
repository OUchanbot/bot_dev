# coding: utf_8
import discord

client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

client.run("NjQ5MDI2NzE4MDI3NDgxMTQ2.Xd6jiw.8lXx71d5a3tMIc4rO7uhxkNOgMw")
