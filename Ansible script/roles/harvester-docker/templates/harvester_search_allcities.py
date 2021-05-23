
import tweepy
import couchdb
import time
import json
import logging
import datetime as DT
import tw_cdb_credentials
import sys
from http.client import IncompleteRead

#twitter auth
consumer_key = tw_cdb_credentials.consumer_key
consumer_secret = tw_cdb_credentials.consumer_secret
access_token = tw_cdb_credentials.access_token
access_token_secret = tw_cdb_credentials.access_token_secret

#1:melbourne, 2:brisbane, 3:sydney, 4:adelaide, 5:perth
citycode = 1

# == couchdb ==
couch = couchdb.Server(url=tw_cdb_credentials.url)
couch.resource.credentials = tw_cdb_credentials.login
db = couch['twitter_raw']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

todaytweets = api.search(q="",geocode="-27.48,153,10mi",count=2,until=DT.date.today().strftime("%Y-%m-%d"))
current_tweet_id = ""
begin_tweet_id = ""

for todaytweet in todaytweets:
    tweetstr = json.dumps(todaytweet._json)
    json_load = json.loads(tweetstr)
    current_tweet_id = json_load['id_str']
    begin_tweet_id = json_load['id_str']

logfile = DT.datetime.today().strftime("%d-%b-%Y(%H-%M-%S.%f)") + ".log"

logging.basicConfig(filename=logfile, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

def get_tweets_query(qword,geocodes,page,datetweet, current_id):
          
    # Authorization to consumer key and consumer secret
    # Calling api
    api = tweepy.API(auth)
    last_tweet_id = current_id
    search_tweets_inserted = 0
    timeline_tweets_inserted = 0
  
    try:
        pages = tweepy.Cursor(api.search, q=qword, geocode=geocodes, count=100, max_id = current_id, until=datetweet).pages(page)

    except IncompleteRead:
        logging.warning("Incomplete Read")

    page = 0
    tweetnumber = 0

    for tweets in pages:
        page = page + 1
        for tweet in tweets:
            tweetnumber = tweetnumber + 1
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
                    'retweet_count': json_load['retweet_count'],
                    'favorite_count': json_load['favorite_count'],
                    'entities': json_load['entities'],
                    'lang': json_load['lang'],
                    }
            last_tweet_id = tweet.id_str
            try:
                db.save(json.loads(json.dumps(text)))
                search_tweets_inserted = search_tweets_inserted + 1
                logging.info("save search tweet successful " + last_tweet_id)
                #go through user timeline of the tweet from search query result
                tweets_user = api.user_timeline(id=json_load['user']['id_str'],count=2,max_id=json_load['id_str'])
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
                    try:
                        db.save(json.loads(json.dumps(text)))
                        logging.info("save user timeline tweet")
                        timeline_tweets_inserted = timeline_tweets_inserted + 1
                    except couchdb.http.ResourceConflict:
                        logging.info("duplicate user timeline tweet")
            except couchdb.http.ResourceConflict:
                logging.info("duplicate search tweet")
                logging.info(last_tweet_id)
        logging.info('Page:' + str(page) + " Tweet number:" + str(tweetnumber))
    currenttime = time.time()
    logging.info("Search tweets:" + str(search_tweets_inserted) + " timeline tweets:" + str(timeline_tweets_inserted) + " Runtime of the program is: " + str(DT.timedelta(seconds=currenttime-starttime)))
    return (last_tweet_id,search_tweets_inserted)

if __name__ == "__main__":
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    starttime = time.time()

    #Melbourne
    geocodes = "-27.48,153,10mi"
    logging.info("MELBOURNE")

    qword = ""
    page = 50 # half maximum pages we can get within 15min
    datetweet = (DT.date.today() - DT.timedelta(days=6)).strftime("%Y-%m-%d")
    timer = 900
    
    # run for 999 times just in case you forgot to close it
    for i in range(0, 999):
        cityname = ""

        if citycode % 5 == 0:
            cityname = "Perth"
        elif citycode % 5 == 4:
            cityname = "Adelaide"
        elif citycode % 5 == 3:
            cityname = "Sydney"
        elif citycode % 5 == 1:
            cityname = "Melbourne"
        elif citycode % 5 == 2:
            cityname = "Brisbane"
        
        zeroresultcountm = 0
        zeroresultcountb = 0
        zeroresultcounts = 0
        zeroresultcounta = 0
        zeroresultcountp = 0

        lasttweetidm = ""
        lasttweetidb = ""
        lasttweetids = ""
        lasttweetida = ""
        lasttweetidp = ""

        logging.info("query number:" + str(i) + ' time to abstract ' + cityname + ' tweets from ' + datetweet + '. With tweets earlier than: ' + current_tweet_id)
        result = get_tweets_query(qword,geocodes,page,datetweet, current_tweet_id)
        current_tweet_id = result[0]
        logging.info("Tweet #" + current_tweet_id + " Tweets inserted:" + str(result[1]))
        
        citycode = citycode + 1
        if citycode % 5 == 0:
            geocodes = "-31.96,115.85,10mi"
            logging.info("PERTH")
            lasttweetidp = current_tweet_id
            if citycode < 6:
                current_tweet_id = begin_tweet_id
            else:
                current_tweet_id = lasttweetidm
            if(result[1]==0):
                zeroresultcounta = zeroresultcounta + 1
                logging.info("Zero search result Adelaide")
        elif citycode % 5 == 2:
            geocodes = "-27.48,153,10mi"
            logging.info("BRISBANE")
            lasttweetidb = current_tweet_id
            if citycode < 6:
                current_tweet_id = begin_tweet_id
            else:
                current_tweet_id = lasttweetids
            if(result[1]==0):
                zeroresultcountm = zeroresultcountm + 1
                logging.info("Zero search result Melbourne")
        elif citycode % 5 == 3:
            geocodes = "-33.8136,151,10mi"
            logging.info("SYDNEY")
            lasttweetids = current_tweet_id
            if citycode < 6:
                current_tweet_id = begin_tweet_id
            else:
                current_tweet_id = lasttweetida
            if(result[1]==0):
                zeroresultcountb = zeroresultcountb + 1
                logging.info("Zero search result Brisbane")
        elif citycode % 5 == 4:
            geocodes = "-34.917,138.6,10mi"
            logging.info("ADELAIDE")
            lasttweetida = current_tweet_id
            if citycode < 6:
                current_tweet_id = begin_tweet_id
            else:
                current_tweet_id = lasttweetidp
            if(result[1]==0):
                zeroresultcounts = zeroresultcounts + 1
                logging.info("Zero search result Sydney")
        elif citycode % 5 == 1:
            geocodes = "-37.8136,144.9631,10mi"
            logging.info("MELBOURNE")
            lasttweetidm = current_tweet_id
            if citycode < 6:
                current_tweet_id = begin_tweet_id
            else:
                current_tweet_id = lasttweetidb
            if(result[1]==0):
                zeroresultcountp = zeroresultcountp + 1
                logging.info("Zero search result Perth")


        if(zeroresultcountm > 0 and zeroresultcountb > 0 and zeroresultcounts > 0 and zeroresultcounta > 0 and zeroresultcountp > 0):
            sys.exit()

        if citycode % 2 == 1:
            logging.info('searching paused 15 minutes')
            # make call after 15min
            while timer >= 0:
                time.sleep(1)
                timer -= 1
        else:
            logging.info('No pause')

    logging.info('searching finished')
