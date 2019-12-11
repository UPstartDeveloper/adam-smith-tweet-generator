import os
import dotenv
import requests
import tweepy


# load API tokens in from environment variables
dotenv.load_dotenv('.env')

consumer_key = (
    os.environ.get('TWITTER_CONSUMER_KEY'))
consumer_secret = (
    os.environ.get('TWITTER_CONSUMER_SECRET'))
access_token = (
    os.environ.get('TWITTER_ACCESS_TOKEN'))
access_token_secret = (
    os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
    )

# create a new authorized session

# using OAuth2
session = tweepy.OAuthHandler(consumer_key, consumer_secret)
session.set_access_token(access_token, access_token_secret)
authenticated = tweepy.API(session, wait_on_rate_limit=True)

# The URL endpoint to update a status (i.e. tweet)
url = 'https://api.twitter.com/1.1/statuses/update.json'

# The contents of status (i.e. tweet text)
status = 'Woohoo!'

authenticated.update_status(status=status)

# Show the text from the response
