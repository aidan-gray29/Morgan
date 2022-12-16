import tweepy
import pymongo
import pandas as pd
import time
from typing import Iterable
from pymongo import MongoClient, ASCENDING, TEXT
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer    # VADER used for sentiment analysis

def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING =                                                             "mongodb+srv://dev-morgan-admin:oxsuiNupoeJEqED1@cluster0.gurz1.mongodb.net/test"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database named messages
    return client['messages']

def sentiment_scores(tweet):
    vader = SentimentIntensityAnalyzer()
    sentiment = vader.polarity_scores(tweet)
    #print("The tweet '", tweet, "' has ", sentiment['neg']*100, " % Negative Sentiment")
    #print(sentiment['neu']*100, " Neutral Sentiment")
    #print(sentiment['pos']*100, " Positive Sentiment")
    return sentiment
    
def main():
    consumer_key =                                                          'x3ce9KoHySRYaB1nYgnXl1Vml'
    consumer_secret =                                                       'MRYBQc7pT0lTliyEbiUDDxdbVvkpuNqqOyOErLOB3sjJRZHB05'
    access_token =                                                          '1565937995517009921-BcHMrr558VbGGPwrKjJ8bb0WM94NqK'
    access_secret =                                                         'XPGK93Fowu1e1V4GvzAgIgJbYUpGu6cRAHS39bxCpCocA'
    connection_string =                                                     "mongodb+srv://dev-morgan-admin:oxsuiNupoeJEqED1@cluster0.gurz1.mongodb.net/test"

    # Authorization for Twitter API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    # Creates the database
    dbname = get_database()

    # Sets the collection name within the database
    collection_name = dbname["direct_messages"]
    
    while(True):
        # Collect 50 direct messages (DM)
        messages = api.get_direct_messages(count=50)
        
        # For each DM, we will process the message through VADER
        #   and add the sentiment scores to the database
        for message in reversed(messages):
            sender_id = message.message_create["sender_id"]
            text = message.message_create["message_data"]["text"]
            timestamp = message.created_timestamp
            processed_tweet = sentiment_scores(text)

            # Continue if the sender id of the current tweet we're reading is Morgan's
            if (sender_id == "1565937995517009921"):
                continue

            # This is the query to collect 
            query = { "identification" : sender_id }

                
            # Check if the user already exists in the database
            if (collection_name.find_one({"identification" : {"$eq" : sender_id}})):
                checker = collection_name.find_one(query)

                # Skips old messages
                if timestamp <= checker["timestamp"]:
                    continue
                print("new message found")
                # diction holds the dictionary for the current message sender
                # which has the sender's sentiment values to update
                diction = collection_name.find_one(query)

                # these below will hold the current average for
                # each sentiment value
                #neg_sent = diction["negative_sentiment"]
                #neu_sent = diction["neutral_sentiment"]
                #pos_sent = diction["positive_sentiment"]

                # this takes the previous sentiment value and
                # the new sentiment value and divides it by two
                # with this approach i'm hoping to affect
                # the sentiment score as well as the AI's
                # attitude immediately rather than gradually over many messages
                # that way the recent conversation sentiment stays relevant
                prev_sent = diction["comp_sentiment"]
                new_sent = processed_tweet['compound']
                final_sent = (prev_sent + new_sent) / 2

                arbitrary = {
                    "identification" : sender_id,
                    "timestamp" : timestamp,
                    "comp_sentiment" : final_sent
                    }

                # replaces the document 
                collection_name.replace_one( { "identification" : sender_id },
                                            arbitrary)
                                           
            # If the user is not yet in the database
            else:
                # Dictionary which we'll be adding to the Database (arbitrary name)
                arbitrary = {
                    "identification" : sender_id,
                    "timestamp" : timestamp,
                    "comp_sentiment" : processed_tweet['compound']
                    }
                collection_name.insert_one(arbitrary)
        time.sleep(60)
if __name__ == '__main__':
    main()
