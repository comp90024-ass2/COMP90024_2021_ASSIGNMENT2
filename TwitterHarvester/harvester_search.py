
import tweepy
import couchdb
import time
import json
import logging
import datetime as DT
import tw_cdb_credentials

#twitter auth
consumer_key = tw_cdb_credentials.consumer_key
consumer_secret = tw_cdb_credentials.consumer_secret
access_token = tw_cdb_credentials.access_token
access_token_secret = tw_cdb_credentials.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

#any today's tweet (for example the most recent Scott Morrison tweet)
current_tweet_id = '1392339238188818437'

#couchdb connect
couch = couchdb.Server(url=tw_cdb_credentials.url)
couch.resource.credentials =tw_cdb_credentials.login
db = couch[tw_cdb_credentials.dbname]

#logfile configuration
logfile = DT.datetime.today().strftime("%d-%b-%Y(%H-%M-%S.%f)") + ".log"
logging.basicConfig(filename=logfile, level=logging.INFO)

def get_tweets_query(qword,geocodes,page,datetweet, current_id):
          
    # Authorization to consumer key and consumer secret
    # Calling api
    api = tweepy.API(auth)
    last_tweet_id = current_id
    search_tweets_inserted = 0
    timeline_tweets_inserted = 0
  
    pages = tweepy.Cursor(api.search, q=qword, geocode=geocodes, count=100, max_id = current_id, until=datetweet).pages(page)
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
            text = {'_id': json_load['id_str'],
                    'created_at': json_load['created_at'],
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
            last_tweet_id = tweet.id_str
            #anticipate duplicate tweets from the search result
            try:
                db.save(json.loads(json.dumps(text)))
                search_tweets_inserted = search_tweets_inserted + 1
                logging.info("save search tweet successful " + last_tweet_id)
                #go through user timeline of the tweet from search query result
                tweets_user = api.user_timeline(id=json_load['user']['id_str'],count=15,max_id=json_load['id_str'])
                for tweet_user in tweets_user:
                    tweetstr = json.dumps(tweet_user._json)
                    json_load = json.loads(tweetstr)
                    user = {'id_str': json_load['user']['id_str'],
                            'screen_name': json_load['user']['screen_name'],
                            'location': json_load['user']['location'],
                            'verified': json_load['user']['verified'],
                            'followers_count': json_load['user']['followers_count'],
                            'friends_count': json_load['user']['friends_count'],}
                    text = {'_id': json_load['id_str'],
                            'created_at': json_load['created_at'],
                            'text': json_load['text'],
                            'source': json_load['source'],
                            'user': user,
                            'geo': json_load['geo'],
                            'coordinates': json_load['coordinates'],
                            'place': json_load['place'],
                            'retweet_count': json_load['retweet_count'],
                            'favorite_count': json_load['favorite_count'],
                            'entities': json_load['entities'],
                            'lang': json_load['lang'],
                            }
                    #anticipate duplicate tweets from the user timeline
                    try:
                        db.save(json.loads(json.dumps(text)))
                        logging.info("save user timeline tweet")
                        timeline_tweets_inserted = timeline_tweets_inserted + 1
                    except couchdb.http.ResourceConflict:
                        logging.info("duplicate user timeline tweet")

            except couchdb.http.ResourceConflict:
                logging.info("duplicate search tweet")
                logging.info(last_tweet_id)
        logging.info('searching paused')
        logging.info("Search tweets:" + search_tweets_inserted + " timeline tweets:" + timeline_tweets_inserted)
    return (last_tweet_id,search_tweets_inserted)

if __name__ == "__main__":
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    #Melbourne
    #geocodes = "-37.8136,144.9631,10mi"

    #Sydney
    #geocodes = "-33.8136,151,10mi"

    #Brisbane
    #geocodes = "-27.48,153,10mi"

    #Perth
    geocodes = "-31.96,115.85,10mi"

    #Adelaide
    #geocodes = "-34.917,138.6,10mi"

    qword = ""
    page = 100 # maximum pages we can get within 15min
    datetweet = (DT.date.today() - DT.timedelta(days=7)).strftime("%Y-%m-%d")
    timer = 900
    
    # run for 999 times just in case you forgot to close it
    for i in range(0, 999):
        timer = 900
        
        logging.info('time to abstract from ' + datetweet + '. With tweets earlier than: ' + current_tweet_id)
        result = get_tweets_query(qword,geocodes,page,datetweet, current_tweet_id)
        current_tweet_id = result[0]
        logging.info(current_tweet_id)

        if(result[1]==0):
            sys.exit()
                    
        # make call after 15min
        while timer >= 0:
            time.sleep(1)
            timer -= 1
    logging.info('searching finished')
