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

# == couchdb ==
'''
couch = couchdb.Server(url='http://localhost:5984/')
couch.resource.credentials = ('admin', 'admin')
db = couch['twitterdata2']
'''

# == OAuth Authentication ==
consumer_key="4SjHN39dXp4NRb015MTa4J6lu"
consumer_secret="c8h4UpuyVFrxpiil8Y7C1LcJ6E3hBKM7nK8Z3olbOCsqIbKuIC"

access_token="1385479485286338562-0wqEPnR2ONv9Ct15KSS9dWdgdLqGgZ"
access_token_secret="YjRNv4jlfPmUCLChgOpSyIYTuDEfZotEE8Ppv6tDl94p2"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

def get_tweets_query(qword,geocodes,page,date, current_id):
          
    # Authorization to consumer key and consumer secret
    # Calling api
    api = tweepy.API(auth)
  
    pages = tweepy.Cursor(api.search, q=qword, geocode=geocodes, count=100, max_id = current_id, until=date).pages(page)
    for tweets in pages:
        for tweet in tweets:
            tweetstr = json.dumps(tweet._json)
            tweetjson = json.loads(tweetstr)
            #db.save(tweetjson)
        current_id = tweet.id_str
    print('searching paused')
    
if __name__ == "__main__":
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    geocodes = "-37.8136,144.9631,10mi"
    qword = ""
    page = 100 # maximum pages we can get within 15min
    date = "2021-04-30"
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
