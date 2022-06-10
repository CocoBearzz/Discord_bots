import discord
import os
my_secret = os.environ['TOKEN']
from random import randint
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

  @client.event
  async def on_message(message):
    x = randint(1,15)
    val = x
    
    if message.author == client.user:
      return
      
    if message.content.startswith("#_motivation"):
      if val == 1:
        await message.channel.send("Our greatest    glory is not in never falling, but in rising every time we fall - Confucius")

      elif val == 2:
        await message.channel.send("Start where you are. Use what you have. Do what you can - Arthur Ashe")

      elif val== 3:
        await message.channel.send("Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time - Thomas Edison")

      elif val== 4:
        await message.channel.send("If you can dream it, you can do it - Walt Disney")

      elif val == 5:
        await message.channel.send("With the new day comes new strength and new thoughts - Eleanor Roosevelt")

      elif val == 6:
        await message.channel.send("We cannot solve problems with the kind of thinking we employed when we came up with them. — Albert Einstein")

      elif val == 7:
        await message.channel.send("Learn as if you will live forever, live like you will die tomorrow. — Mahatma Gandhi")

      elif val == 8:
        await message.channel.send("Stay away from those people who try to disparage your ambitions. Small minds will always do that, but great minds will give you a feeling that you can become great too. — Mark Twain")

      elif val == 9:
        await message.channel.send("When you give joy to other people, you get more joy in return. You should give a good thought to happiness that you can give out. — Eleanor Roosevelt")

      elif val == 10:
        await message.channel.send("It is only when we take chances, when our lives improve. The initial and the most difficult risk that we need to take is to become honest. —Walter Anderson")
        
      elif val == 11:
        await message.channel.send("Success usually comes to those who are too busy looking for it. — Henry David Thoreau")

      elif val == 12:
        await message.channel.send("If you are working on something that you really care about, you don’t have to be pushed. The vision pulls you. — Steve Jobs")

      elif val == 13:
        await message.channel.send("You've got to get up every morning with determination if you're going to go to bed with satisfaction. — George Lorimer")

      elif val == 14:
        await message.channel.send("The most difficult thing is the decision to act, the rest is merely tenacity. —Amelia Earhart")

      elif val == 15:
        await message.channel.send("Opportunities don't happen, you create them. — Chris Grosser")


client.run(my_secret)