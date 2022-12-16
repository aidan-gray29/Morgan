import discord
import os
import aidialog
import configparser
import openai_hook

#run discord bot client
client = discord.Client(intents=discord.Intents.default())
config = configparser.ConfigParser(interpolation=None)
config.read('confidential.ini')
TOKEN = config['Discord']['token']

if __name__ == '__main__':
    #authenticate to openai API
    openai_hook.init()


    #login as bot to discord api
    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))

    #listen for messages mentioning the bot's username, and use the openai API to generate a response
    @client.event
    async def on_message(message):
        if client.user.mentioned_in(message):
            print(message.content)
            print(message.author.id)
            await message.channel.send(aidialog.getChatResponse(message.content))

    #run the client using the specified token
    client.run(TOKEN)