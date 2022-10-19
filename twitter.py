import tweepy, configparser, sys, pymongo
from time import sleep
from os import listdir
from os.path import isfile, join

# imports the Reaction GIFs folder to be used in the directory
def file_get():
    mypath = "./ReactionGIFs" 
    onlyfiles= []
    for file in listdir(mypath):
        if isfile(join(mypath,file)):
            onlyfiles.append(file)
    return onlyfiles

# Twitter API v2 authentication using OAuth 1.0a User Context 
def tweepy_cred():
    auth = tweepy.OAuthHandler(config['Twitter']['consumer_key'], config['Twitter']['consumer_secret'] )
    auth.set_access_token(config['Twitter']['access_token'], config['Twitter']['access_token_secret'])
    return tweepy.API(auth)

# Posts a GIF based on the emotion provided
def tweet_reaction(emotion):
    switch= {
        'angry': './ReactionGIFs/dino_angry.gif',
        'happy': './ReactionGIFs/dino_happy.gif',
        'bored': './ReactionGIFs/dino_bored.gif',
        'sad': './ReactionGIFs/dino_sad.gif',
        'confused': './ReactionGIFs/dino_confused.gif'
    }
    status = 'Testing GIF Post'
    try:
        auth = tweepy_cred()
        auth.update_status_with_media(filename=switch.get(emotion, "Invalid"),status=status)
        print("Tweeted!")
        sleep(900)
    except Exception as e:
        print("Encountered error! Error details: %s"%str(e))

# sends a direct message to user
def send_dm(user_id, message):
    auth = tweepy_cred()
    auth.send_direct_message(recipient_id=user_id, text=message)
    
# receives last 5 direct messages
# note: 5 can be changed to some arbitrary number
def receive_dm():
    auth = tweepy_cred()
    messages = auth.get_direct_messages(count=5)
    for message in reversed(messages):
        sender_id = message.message_create["sender_id"]
        text = message.message_create["message_data"]["text"]
        usernames = {
            sender_id : text,
            }
    return messages

if __name__ == "__main__":
    config = configparser.ConfigParser(interpolation=None)
    file = 'confidential.ini'
    section = 'Twitter'

    # Initialize blank default values
    # ONLY add them in the unshared .ini file
    default = {'bearer_token': '',
            'consumer_key': '',
            'consumer_secret': '',
            'access_token': '',
            'access_token_secret': ''}

    # Read the Twitter tokens from the file
    # If they don't exist, create a new section so they can be manually added
    config.read(file)
    if section not in config:
        config[section] = default
        with open(file, 'w') as configfile:
            config.write(configfile)
        raise ValueError(f"{section} tokens not found in {file} file. Please add them before running Morgan.")

    tweet_reaction('angry')
    # receive_texts()
