import discord
import os
import json
import requests
import random

client=discord.Client()

@client.event
async def on_ready():
  print('{0.user} is ready to steal ur mummy'.format(client))
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith(';Oi'):
    await message.channel.send('Oi hoi!')
  if message.content.startswith(';oi'):
    await message.channel.send('Oi hoi!')
  if message.content.startswith(';bullch'):
    await message.channel.send('https://images.hindustantimes.com/auto/img/2020/05/15/600x338/royal-enfield-bullet-350-bs6-front-three-quarter-Ht_Auto_1585649129164_1589527371374.jpg')
client.run(os.getenv('token'))

