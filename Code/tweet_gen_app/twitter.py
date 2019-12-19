def tweet(status_update):
    """Send a status update to @AdamChain on Twitter.

       Parameters:
       status_update(str): the text in the post to be Tweeted

       Returns:
       None
    """
    # make required imports
    import os
    import dotenv
    import requests
    import tweepy

    # load API tokens in from environment variables
    dotenv.load_dotenv('.env')

    consumer_key = (
        os.environ.get('TWITTER_CONSUMER_KEY')).encode()
    consumer_secret = (
        os.environ.get('TWITTER_CONSUMER_SECRET'))
    access_token = (
        os.environ.get('TWITTER_ACCESS_TOKEN'))
    access_token_secret = (
        os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
        )

    # create a new authorized session using OAuth2
    session = tweepy.OAuthHandler(consumer_key, consumer_secret)
    session.set_access_token(access_token, access_token_secret)
    authenticated = tweepy.API(session, wait_on_rate_limit=True)

    # send the request to Twitter API
    authenticated.update_status(status=status_update)


if __name__ == "__main__":
    tweet("Capitalism... it still works?")
    print('did it work?')
