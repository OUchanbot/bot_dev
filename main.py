import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
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
            m = "ねえ笑笑笑笑"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)

client.run("NjQ5MDI2NzE4MDI3NDgxMTQ2.Xd6DQw.bS19D3YGrzRfn9f86NXvMyd8gdA")
