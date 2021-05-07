import tweepy
import couchdb

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

couch = couchdb.Server(url='http://localhost:5984/')
couch.resource.credentials = ('admin', 'admin')
db = couch['twitterdata2']
    
def get_tweets(username):
          
    # Authorization to consumer key and consumer secret
    # Calling api
    api = tweepy.API(auth)
  
    # 200 tweets to be extracted
    #number_of_tweets=200
    tweets = api.user_timeline(screen_name=username,count=2)

    for tweet in tweets:
        tweetstr = json.dumps(tweet._json)
        tweetjson = json.loads(tweetstr)
        #int(tweetstr["id"])
        db.save(tweetjson)


def get_tweets_query(qword,geocodes,maxtweet,date):
          
    # Authorization to consumer key and consumer secret
    # Calling api
    api = tweepy.API(auth)
  
    #tweets = api.search(q=qword,geocode=geocodes,count=2)
    tweets = tweepy.Cursor(api.search, q=qword, geocode=geocodes, until=date).items(maxtweet)
    #tweets = tweepy.Cursor(api.search, q=qword).items(10)

    print(geocodes + " " + qword)

    for tweet in tweets:
        tweetstr = json.dumps(tweet._json)
        tweetjson = json.loads(tweetstr)
        #db.save(tweetjson)
        print(tweetjson)

        
if __name__ == "__main__":
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    geocodes = "-37.8136,144.9631,10mi"
    qword = ""
    maxtweet = 50
    date = "2021-04-30"

    get_tweets_query(qword,geocodes,maxtweet,date)
    
    