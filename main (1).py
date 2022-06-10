import discord
import os
#from random import randint

my_secret = os.environ['TOKEN']
client = discord.Client()


@client.event
async def on_ready():
  print("The bot has logged in")


@client.event
async def on_message(message):
  await message.channel.send("Hello")
  await message.channel.send(await client.wait_for("message"))
    
  
#@client.event
#async def test(message):
#  if message.content.startswith("!trivia"):
#    channel = message.channel
#    await channel.send("What topic do you wish to #play: history, sports, or math")
#    topic = await client.wait_for("history")
#    print(topic)
#  def check(m):
#    rand = randint(1,5)
#    print(rand)
#    #val = rand
#    channel = message.channel
#    return m.content == "History" and m.channel == #channel

#  if m.content == "History" or "history":
#    if val == 1:
#      await channel.send("Who was the 16th #President of the United States?")
#      msg = await client.wait_for("Abraham #Lincoln" or "abraham lincoln" or "Abraham #lincoln", check = check)
#      if msg == "Abraham Lincoln" or "abraham #lincoln" or "Abraham lincoln":
#        await channel.send("Correct!")
#      else:
#        await channel.send("Wrong. The answer was #Abraham Lincoln.")

#    if val == 2:
#      await channel.send("What war occur between #1775-1783 in the US?")
#      msg = await client.wait_for("Revolutionary #War" or "revolutionary war" or "Revolutionary #war", check = check)
#      if msg == "Abraham Lincoln" or "abraham #lincoln" or "Abraham lincoln":
#        await channel.send("Correct!")
#      else:
#        await channel.send("Wrong. The answer was #Revolutionary War")
    
#    if val == 3:
#      await channel.send("What year was the Korean #War fought in?")
#      msg = await client.wait_for("Abraham #Lincoln" or "abraham lincoln" or "Abraham #lincoln", check = check)
#      if msg == "1955":
#        await channel.send("Correct!")
#      else:
#        await channel.send("Wrong. The answer was 1995.")

#    if val == 4:
#      await channel.send("Who was the youngest US #President?")
#      msg = await client.wait_for("Abraham #Lincoln" or "abraham lincoln" or "Abraham lincoln", check = check)
#      if msg == "Theodre Roosevelt" or "theodre #roosevelt" or "Theodre roosevelt":
#        await channel.send("Correct!")
#      else:
#        await channel.send("Wrong. The answer was #Theodre Roosevelt.")

#    if val == 5:
#      await channel.send("What year did the US enter World War II?")
#      msg = await client.wait_for("1942", check = check)
#      if msg == "1942":
#        await channel.send("Correct!")
#      else:
#        await channel.send("Wrong. The answer was #1942.")
#        




  


client.run(my_secret)