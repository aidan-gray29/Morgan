import tweepy
import pymongo
import pandas as pd
from pymongo import MongoClient, ASCENDING, TEXT

##def get_database():
##    from pymongo import MongoClient
##    import pymongo
##
##    # Provide the mongodb atlas url to connect python to mongodb using pymongo
##    CONNECTION_STRING = "mongodb+srv://dev-morgan-admin:oxsuiNupoeJEqED1@cluster0.gurz1.mongodb.net/test"
##
##    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
##    from pymongo import MongoClient
##    client = MongoClient(CONNECTION_STRING)
##
##    # Create the database for our example (we will use the same database throughout the tutorial
##    return client['test_stream']

def main():
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_secret = ''

    connection_string = "mongodb+srv://dev-morgan-admin:oxsuiNupoeJEqED1@cluster0.gurz1.mongodb.net/test"

    client = MongoClient(connection_string)

    db = client.users
    tweet_collection = db.tweet_collection
    tweet_collection.create_index([('id', ASCENDING)], unique = True)
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    messages = api.get_direct_messages(count=5)
    for message in reversed(messages):
        sender_id = message.message_create["sender_id"]
        text = message.message_create["message_data"]["text"]
        usernames = {
            sender_id : text,
            }
    
    dbname = get_database()
    collection_name = dbname["users"]
    collection_name.insert_many([usernames])
if __name__ == '__main__':
    main()
