# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 17:43:02 2021

@author: cheng
"""
  
import tweepy
from langdetect import detect
import couchdb
import time
import json
import tw_cdb_credentials

#twitter auth
consumer_key = tw_cdb_credentials.consumer_key
consumer_secret = tw_cdb_credentials.consumer_secret
access_token = tw_cdb_credentials.access_token
access_token_secret = tw_cdb_credentials.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

#couchdb connect
couch = couchdb.Server(url=tw_cdb_credentials.url)
couch.resource.credentials =tw_cdb_credentials.login
db = couch[tw_cdb_credentials.dbname]

def get_tweets_query(qword,geocodes,page,date, current_id):
          
    # Authorization to consumer key and consumer secret
    # Calling api
    api = tweepy.API(auth)
  
    #pages = tweepy.Cursor(api.search, q=qword, geocode=geocodes, count=100, max_id = current_id, until=date).pages(page)
    pages = tweepy.Cursor(api.search, q=qword, geocode=geocodes, count=100, until=date).pages(page)
    for tweets in pages:
        for tweet in tweets:
            tweetstr = json.dumps(tweet._json)
            json_load = json.loads(tweetstr)
            user = {'id_str': json_load['user']['id_str'],
                    'screen_name': json_load['user']['screen_name'],
                    'location': json_load['user']['location'],
                    'verified': json_load['user']['verified'],
                    'followers_count': json_load['user']['followers_count'],
                    'friends_count': json_load['user']['friends_count'],}
            text = {'created_at': json_load['created_at'],
                    'id_str': json_load['id_str'],
                     'text': json_load['text'],
                    'source': json_load['source'],
                    'user': user,
                    'geo': json_load['geo'],
                    'coordinates': json_load['coordinates'],
                    'place': json_load['place'],
                    #'quote_count': json_load['quote_count'],
                    #'reply_count': json_load['reply_count'],
                    'retweet_count': json_load['retweet_count'],
                    'favorite_count': json_load['favorite_count'],
                    'entities': json_load['entities'],
                    'lang': json_load['lang'],
                    }
            db.save(json.loads(json.dumps(text)))
            current_id = tweet.id_str
        print('searching paused')
    
if __name__ == "__main__":
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    #Melbourne
    #geocodes = "-37.8136,144.9631,10mi"

    #Sydney
    geocodes = "-33.8136,151,10mi"

    #Brisbane
    #geocodes = "-27.48,153,10mi"

    #Perth
    #geocodes = "-31.96,115.85,10mi"

    #Adelaide
    #geocodes = "-34.917,138.6,10mi"

    qword = ""
    page = 100 # maximum pages we can get within 15min
    date = "2021-05-02"
    current_id = '1387919449697579012'
    timer = 900
    
    # run for 20 times
    for i in range(0, 20):
        timer = 900
        
        print('time to abstract from ' + date + '. With tweets earlier than: ' + current_id)
        get_tweets_query(qword,geocodes,page,date, current_id)
        
        # make call after 15min
        while timer >= 0:
            time.sleep(1)
            timer -= 1
    print('searching finished')
