import tweepy
from credentials import *

print(twitter_consumer_key)
print(twitter_consumer_secret)
print(twitter_access_token)
print(twitter_access_token_secret)

def postTweet(tweet):
    tw_auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
    tw_auth.set_access_token(twitter_access_token, twitter_access_token_secret)
    tw_api = tweepy.API(tw_auth)

    print(tw_api.update_status(tweet))