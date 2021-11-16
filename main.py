import discord
import rpoems
import randfacts
import datetime
from datetime import datetime as dt


##pip install rpoems
##pip install randfacts



before = dt(2018, 8, 22)
after = dt(2018, 8, 20)
corpus = rpoems.build_corpus( before=before, after=after, limit=3000)
poem = rpoems.couplet_rhyming_poem(corpus)

client = discord.Client()
 

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    print(message.author)
    print(message.content)
    if 'tomahawk' in message.content.lower():
        await message.channel.send("i smell an argument")
        print("toma is arguing grab your popcorn")
    if 'prolik' in message.content.lower():
        await message.channel.send("prolicon is a chad trolololo")
        print("prolikon is a chad B  )")
    if '30303030' in message.content.lower():
        await message.channel.send("nick is cool and so is his doggo")
    if 'redditpoem' in message.content.lower():
        poem = rpoems.couplet_rhyming_poem(corpus)
        await message.channel.send(poem)
    if 'randomfact' in message.content.lower():
        randomfact = randfacts.get_fact()
        await message.channel.send(randomfact)
    if 'Randomfact' in message.content.lower():
        randomfact = randfacts.get_fact()
        await message.channel.send(randomfact)
    if 'Redditpoem' in message.content.lower():
        poem = rpoems.couplet_rhyming_poem(corpus)
        await message.channel.send(poem)


client.run('OTA5ODQ3MzY2MTc2MjE1MDYx.YZKPZA.TaAUw1QScJ7VVMLQo2swQczuD98')
