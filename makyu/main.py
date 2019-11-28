# coding: utf_8
import discord
import random
import time
import os

client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')


message_cnt = 0
start = time.time()
old_id = ""
@client.event
async def on_message(message):
	if client.user != message.author:
		user_name = str(message.author)
		pos = user_name.find('#')
		user_id = user_name[pos:]
		message_size = len(message.content)

		
		if user_id == "#1362" and "レジェンド" in message.content:
			await message.channel.send("やったじゃん")
			
				
	
		if message.content == "バイバイ":
			await message.channel.send("おう、またな")
		if user_id == "#3334" and random.random() < 0.15:
			await message.channel.send("うるせえジジイ")
		if user_id == "#3882" and random.random() < 0.15:
			await message.channel.send("お、またナンパしとるんか？？")

		if message.content == "!LVUP":
			m = "/nick おーちゃんLV30"
			await message.channel.send(m)

		if message.content[:int(message_size/2)] == message.content[int(message_size/2):] and int(message_size/2) >= 3:
			m = "二回すなあ！"
			await message.channel.send(m)
		elif message.content.startswith("おはよう"): #「おはよう」で始まるか調べる
			m = "おはようございます" + message.author.name + "さん！" # メッセージを書きます
			await message.channel.send(m) # メッセージが送られてきたチャンネルへメッセージを送ります
		elif message.content.startswith("おやすみ"):
			m = "おやすみ" + message.author.name + "さん！"
			await message.channel.send(m)
		elif message.content.startswith("うさめるうは"):
			m = "クソジジイ"
			await message.channel.send(m)
		elif message.content.startswith("なっちゃん"):
			m = "ピータン"
			await message.channel.send(m)
		elif message.content.startswith("あず"):
			m = "ねえ笑笑笑笑"
			await message.channel.send(m)
	
#cur_dir = os.getcwd()
#path = os.path.join(cur_dir,'../..',"token/token.txt")
#token = ""
#with open(path) as f:
#	token = f.read().rstrip('\n')
#client.run(token)
client.run("NjQ5NjI5OTYxMTM2NjM1OTA1.Xd_oDA.DphwrowTJ5lrYyLPIRhlvzoVge4")
