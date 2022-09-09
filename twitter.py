import tweepy

# Twitter keys and tokens
twitter_api_key= "Lsf9S3ias0zDLefFQ6TrsLSw3"
twitter_api_secret = "JaOzp4oYdytsRnoHBndquHdNUvNoF641gA2Gy6wdsO2aGMTiXd"
twitter_access_token = "1565937995517009921-X21d0CQiwyenBVsY27w7MvijV3KRyv"
twitter_access_secret = "ULG8gBYoxS9BKPxjIXPXlyAwSUw5lS5sI9yVfLbexTtUq" 

auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret)
auth.set_access_token(twitter_access_token, twitter_access_secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print('Successful Authentication')
except:
    print('Failed authentication')