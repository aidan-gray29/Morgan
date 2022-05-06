#################
# Project Title – BitBerg Bot

# Description   – Twitter (discord) bot that simulates conversation 
#                 to your tweets		
# Tools & APIS  – Python (Coding)
#                 Cloud Natural Language API 
#                 Dialogflow API
#					TODO: GPT2 NLP response
#				  Twitter API

# Members       Aidan Gray
#				Joshua Decano
#				Scott Herron
#				Richard Huang
#################

#modules : sentiment analysis on users tweets
#					 gifs and sprites
#					 chat responses based on sentiment
#					 general comments based on sentiment over past N tweets

# from google.cloud import dialogflow
# from google.cloud import language
# from google.cloud import language_v1
# from google.cloud import
import discord
# import requests
# import io
# import os

client = discord.Client()
TOKEN = "BOT TOKEN GOES HERE"

from user import User
from dialogflow import discord_response
    
if __name__ == '__main__':
	@client.event
	async def on_ready():
		print('We have logged in as {0.user}'.format(client))

	@client.event
	async def on_message(message):
		if(client.user.mentioned_in(message)):
			print(message.content)
			print(message.author.id)
			user = str(message.author.id)
			poten_new_user = User(user)
			temp_tuple = discord_response(poten_new_user, message.content)
			await message.channel.send(temp_tuple[1], file=discord.File(temp_tuple[0]))
			poten_new_user.close()
	client.run(TOKEN)
#