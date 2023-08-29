import discord
import os
import requests
import json
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

url = "https://anime-recommender.p.rapidapi.com/get_titles"

headers = {
    "X-RapidAPI-Key": "8534d69e01msh13fa8b898230f5cp17f811jsn44b3c2cd4f49",
    "X-RapidAPI-Host": "anime-recommender.p.rapidapi.com"
}


def get_anime():
  response = requests.get(url, headers=headers)
  json_data = json.loads(response.text)
    
  if "data" in json_data and isinstance(json_data["data"], list) and json_data["data"]:
    anime_titles = json_data["data"]
    random_title = random.choice(anime_titles)
    return "You should watch " + random_title
  else:
    return "No anime titles available."


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$anime'):
    anime = get_anime()
    await message.channel.send(anime)


my_secret = os.environ['TOKEN']
client.run(my_secret)
