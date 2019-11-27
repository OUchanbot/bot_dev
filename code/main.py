# coding: utf_8
import discord
import random
client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')


@client.event
async def on_message(message):
	if client.user != message.author:
		user_name = str(message.author)
		pos = user_name.find('#')
		if user_name[pos:] == "#3334" and random.random() < 0.25:
			await message.channel.send("うるせえジジイ")

	if message.content[:int(len(message.content)/2)] == message.content[int(len(message.content)/2)] and int(len(message.content)/2) >= 3:
	#if message.content[:int(len(message.content)/2)] == message.content[int(len(message.content)/2)]:
		if client.user != message.author:
			m = "二回すなあ！"
			await message.channel.send(m)
		
	# 「おはよう」で始まるか調べる
	if message.content.startswith("おはよう"):
		# 送り主がBotだった場合反応したくないので
		if client.user != message.author:
			# メッセージを書きます
			m = "おはようございます" + message.author.name + "さん！"
			# メッセージが送られてきたチャンネルへメッセージを送ります
			await message.channel.send(m)

	if message.content.startswith("おやすみ"):
		# 送り主がBotだった場合反応したくないので
		if client.user != message.author:
			# メッセージを書きます
			m = "おやすみ" + message.author.name + "さん！"
			# メッセージが送られてきたチャンネルへメッセージを送ります
			await message.channel.send(m)

	if message.content.startswith("うさめるうは"):
		# 送り主がBotだった場合反応したくないので
		if client.user != message.author:
			# メッセージを書きます
			m = "クソジジイ"
			# メッセージが送られてきたチャンネルへメッセージを送ります
			await message.channel.send(m)

	if message.content.startswith("なっちゃん"):
		# 送り主がBotだった場合反応したくないので
		if client.user != message.author:
			# メッセージを書きます
			m = "ピータン"
			# メッセージが送られてきたチャンネルへメッセージを送ります
			await message.channel.send(m)
	if message.content.startswith("あず"):
		# 送り主がBotだった場合反応したくないので
		if client.user != message.author:
			# メッセージを書きます
			#m = "ねえ笑笑笑笑"
			m = "ねえwww"
			# メッセージが送られてきたチャンネルへメッセージを送ります
			await message.channel.send(m)


client.run("NjQ5MDI2NzE4MDI3NDgxMTQ2.Xd6jiw.8lXx71d5a3tMIc4rO7uhxkNOgMw")
