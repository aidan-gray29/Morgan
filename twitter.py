
import tweepy
import configparser

config = configparser.ConfigParser(interpolation=None)
file = 'confidential.ini'

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
if 'Twitter' not in config:
    config['Twitter'] = default
    with open(file, 'w') as configfile:
        config.write(configfile)
    
    raise ValueError("Twitter tokens not found in %s file. Please add them before running Morgan." % file)

client = tweepy.Client(
    # Twitter developer bearer tokens and consumer key/secret 
    bearer_token=config['Twitter']['bearer_token'],
    consumer_key=config['Twitter']['consumer_key'],
    consumer_secret=config['Twitter']['consumer_secret'],
    # Access token and secret from the database
    access_token=config['Twitter']['access_token'],
    access_token_secret=config['Twitter']['access_token_secret']
)

# checking most recent tweet from the bot's account
query = 'from:MorganbotDev'
tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)

for tweet in tweets.data:
    print(tweet.text)
    if len(tweet.context_annotations) > 0:
        print(tweet.context_annotations)

# Tweet Fields
response = client.search_recent_tweets(
    "Tweepy", tweet_fields=["created_at", "lang"]
)
tweets = response.data

# You can then access those fields as attributes of the Tweet objects
for tweet in tweets:
    print(tweet.id, tweet.lang)

# Alternatively, you can also access fields as keys, like a dictionary
for tweet in tweets:
    print(tweet["id"], tweet["lang"])

# There’s also a data attribute/key that provides the entire data dictionary
for tweet in tweets:
    print(tweet.data)
