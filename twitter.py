import tweepy, configparser, sys
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
def tweet_reaction(api, emotion):
    if emotion == "angry":
        filename = "./ReactionGIFs/dino_angry.gif"
        status = "Testing Angry GIF Post"
    elif emotion == "happy":
        filename = "./ReactionGIFs/dino_happy.gif"
        status = "Testing Happy GIF Post"
    elif emotion == "bored":
        filename = "./ReactionGIFs/dino_bored.gif"
        status = "Testing Bored GIF Post"
    elif emotion == "sad":
        filename = "./ReactionGIFs/dino_sad.gif"
        status = "Testing Sad GIF Post"
    elif emotion == "confused":
        filename = "./ReactionGIFs/dino_confused.gif"
        status = "Testing Confused GIF Post"
    try:
        api.update_status_with_media(filename=filename,status=status)
        print("Tweeted!")
        sleep(900)
    except Exception as e:
        print("Encountered error! Error details: %s"%str(e))

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

    tweet_reaction(tweepy_cred())