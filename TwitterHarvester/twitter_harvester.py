import tweepy

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import twitter_credentials

consumer_key = twitter_credentials.consumer_key
consumer_secret = twitter_credentials.consumer_secret
access_token = twitter_credentials.access_token
access_token_secret = twitter_credentials.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

class StdOutListener(StreamListener):
    def __init__(self):
        super().__init__()
        self.max_tweets = 10
        self.tweet_count = 0
    
    def on_data(self, data):
        try:
         data
        except TypeError:
            print(completed)
        else:
         self.tweet_count+=1
         if(self.tweet_count==self.max_tweets):
           print("completed")
           return(False)
         else:
          decoded = json.loads(data)
          with open('harvested_tweets.json','a') as tf:
            json_load = json.loads(data)
            #text = {'text': json_load['text']}
            tf.write(json.dumps(json_load))
    
    def on_error(self,status):
        print(status)
        
if __name__ == "__main__":
    
    listener = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    stream = Stream(auth,listener)
    stream.filter(locations=[144.717,-37.633,145.367,38.2])