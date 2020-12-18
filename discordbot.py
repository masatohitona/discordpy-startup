from discord.ext import commands
from googletrans import Translator
import os
import traceback

client = discord.Client()
translator = Translator()
token = os.environ['DISCORD_BOT_TOKEN']


@client.event
async def on_ready():
    print('--------------')
    print('ログインしました')
    print(client.user.name)
    print(client.user.id)
    print('--------------')

@client.event
async def on_ready():

    ch_name = "trans-start"

    for channel in client.get_all_channels():
        if channel.name == ch_name:
            await channel.send("起動しました\n使用方法は`tb!trans`で翻訳できます")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == "tb!trans":
        say = message.content
        say = say[8:]
        if say.find('-') == -1:
            str = say
            detact = translator.detect(str)
            befor_lang = detact.lang
            if befor_lang == 'ja':
                convert_string = translator.translate(str, src=befor_lang, dest='en')
                embed = discord.Embed(title='翻訳結果', color=0x42c2f5)
                embed.add_field(name='原文', value=str)
                embed.add_field(name='翻訳', value=convert_string.text, inline=False)
                await message.channel.send(embed=embed)
            else:
                convert_string = translator.translate(str, src=befor_lang, dest='ja')
                embed = discord.Embed(title='翻訳結果', color=0x42c2f5)
                embed.add_field(name='原文', value=str)
                embed.add_field(name='翻訳', value=convert_string.text, inline=False)
                await message.channel.send(embed=embed)
        else:
            trans, str = list(say.split('='))
            befor_lang, after_lang = list(trans.split('-'))
            convert_string = translator.translate(str, src=befor_lang, dest=after_lang)
            embed = discord.Embed(title='翻訳結果', color=0x42c2f5)
            embed.add_field(name='原文', value=str)
            embed.add_field(name='翻訳', value=convert_string.text, inline=False)
            await message.channel.send(embed=embed)

    if message.content.startswith('tb!detect'):
        say = message.content
        s = say[8:]
        detect = translator.detect(s)
        m = 'この文字列の言語は ' + detect.lang + ' です。'
        await message.channel.send(m)

    if message.content == "tb!restart":
     if message.author.id == 739702692393517076:
        await message.channel.send('再起動中')
        await message.add_reaction("✅")
        await client.logout()
   
    if message.content == "tb!restart":
     if message.author.id == 663196515384295425:
        await message.channel.send('再起動中')
        await message.add_reaction("✅")
        await client.logout()
        
    if message.content == "tb!help":
        dm = await message.author.create_dm()
        await dm.send("transbot使い方\n`tb!trans`で翻訳ができて\n`tb!detect`で言語を検索できます\n-----------------\n管理者コマンド\n`tb!restart`で再起動します")
        await message.add_reaction("✅")
   
@client.event
async def on_reaction_add(reaction, user):
    if reaction.count == 2:
        if str(reaction.emoji) == "✅":
         await reaction.channel.send("transbot使い方\n`tb!trans`で翻訳ができて\n`tb!detect`で言語を検索できます\n-----------------\n管理者コマンド\n`tb!restart`で再起動します")


client.run(TOKEN)
