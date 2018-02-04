import os
import tweepy

def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

def handle(tweet):
    cfg = { 
        "consumer_key"        : os.environ['consumer_key'],
        "consumer_secret"     : os.environ['consumer_secret'],
        "access_token"        : os.environ['access_token'],
        "access_token_secret" : os.environ['access_token_secret'] 
      }
    
    api = get_api(cfg)
    
    status = api.update_status(status=tweet)
    print('Tweet sent.')
    print(status)
