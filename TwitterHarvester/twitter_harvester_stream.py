import tweepy

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import tw_cdb_credentials
import time
from http.client import IncompleteRead
import logging
import datetime as DT
import couchdb
import sys

consumer_key = tw_cdb_credentials.consumer_key
consumer_secret = tw_cdb_credentials.consumer_secret
access_token = tw_cdb_credentials.access_token
access_token_secret = tw_cdb_credentials.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

# == couchdb ==
couch = couchdb.Server(url=tw_cdb_credentials.url)
couch.resource.credentials = tw_cdb_credentials.login

dbtwitter = couch['twitter_raw']

logfile = "Stream " + DT.datetime.today().strftime("%d-%b-%Y(%H-%M-%S.%f)") + ".log"

logging.basicConfig(filename=logfile, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

class Point:

    def __init__(self, xcoord=0, ycoord=0):
        self.x = xcoord
        self.y = ycoord

class Rectangle:
    def __init__(self, bottom_left, top_right):
        self.bottom_left = bottom_left
        self.top_right = top_right

    def intersects(self, other):
        return not (self.top_right.x < other.bottom_left.x or self.bottom_left.x > other.top_right.x or self.top_right.y < other.bottom_left.y or self.bottom_left.y > other.top_right.y)

class StdOutListener(StreamListener):
    def __init__(self):
        super().__init__()
        self.max_tweets = 1001 
        self.tweet_count = 0
        self.mcount = 0
        self.scount = 0
        self.bcount = 0
        self.pcount = 0
        self.acount = 0
        self.timeline_tweets_inserted = 0
    
    def on_data(self, data):
        try:
         data
        except TypeError:
            print(completed)
        else:
         self.tweet_count+=1
         if(self.tweet_count==self.max_tweets):
            logging.info("completed")
            endtime = time.time()
            logging.info("Runtime of the program is: "+ str(DT.timedelta(seconds=endtime-starttime)))
            logging.info("Stream tweets from Melbourne is " + str(self.mcount*100/(self.max_tweets-1)))
            logging.info("Stream tweets from Sydney is " + str(self.scount*100/(self.max_tweets-1)))
            logging.info("Stream tweets from Brisbane is " + str(self.bcount*100/(self.max_tweets-1)))
            logging.info("Stream tweets from Perth is " + str(self.pcount*100/(self.max_tweets-1)))
            logging.info("Stream tweets from Adelaide is " + str(self.acount*100/(self.max_tweets-1)))
            logging.info("Stream tweets from other regions is " + str((self.max_tweets-1-self.mcount-self.scount-self.bcount-self.pcount-self.acount)*100/(self.max_tweets-1)), "%")
            logging.info("User timeline tweets is " + str(self.timeline_tweets_inserted))
            return(False)
         else:
            decoded = json.loads(data)
            logging.info("Tweet " + str(self.tweet_count) + " of " + str(self.max_tweets-1))
            if(self.tweet_count % 50 == 49):
                endtime = time.time()
                logging.info("Runtime of the program is: " + str(DT.timedelta(seconds=endtime-starttime)))
                logging.info("Stream tweets is " + str(self.mcount+self.scount+self.bcount+self.pcount+self.acount))
                logging.info("User timeline tweets is " + str(self.timeline_tweets_inserted))
            json_load = json.loads(data)
            tbl = json_load['place']['bounding_box']['coordinates'][0][0]
            tur = json_load['place']['bounding_box']['coordinates'][0][3]

            mcount = 0
            scount = 0
            bcount = 0
            pcount = 0
            acount = 0

            #rectangle tweet
            rtw = Rectangle(Point(tbl[0],tbl[1]),Point(tur[0],tur[1]))

            #rectangle Melbourne
            #rme = Rectangle(Point(144.717,-38.2),Point(145.367,-37.633))
            rme = Rectangle(Point(144.217,-38.7),Point(145.867,-37.133))
            #rme = Rectangle(Point(143.717,-39.2),Point(146.367,-36.633))

            #rectangle Sydney
            #rsy = Rectangle(Point(150.633,-35),Point(151.367,-33.533))
            rsy = Rectangle(Point(150.133,-35.5),Point(151.867,-33.033))
            #rsy = Rectangle(Point(149.633,-36),Point(152.367,-32.533))

            #rectangle Brisbane
            #rbr = Rectangle(Point(152.633,-27.783),Point(153.333,-27))
            rbr = Rectangle(Point(152.133,-28.283),Point(153.833,-26.5))
            #rbr = Rectangle(Point(151.633,-28.783),Point(154.333,-26))

            #rectangle Perth
            #rpe = Rectangle(Point(115.633,-32.217),Point(116.217,-31.667))
            rpe = Rectangle(Point(115.133,-32.717),Point(116.717,-31.167))
            #rpe = Rectangle(Point(114.633,-33.217),Point(117.217,-30.667))

            #rectangle Adelaide
            #rad = Rectangle(Point(138.458,-35.02),Point(138.75,-34.55))
            rad = Rectangle(Point(137.958,-35.52),Point(139.25,-34.05))
            #rad = Rectangle(Point(137.458,-36.02),Point(139.75,-33.55))

            if(rtw.intersects(rme)):
                self.mcount = self.mcount + 1
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
                    dbtwitter.save(json.loads(json.dumps(text)))
                    logging.info("save tweet into Melbourne database")
                    tweets_user = api.user_timeline(id=json_load['user']['id_str'],count=21,max_id=json_load['id_str'])
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
                            dbtwitter.save(json.loads(json.dumps(text)))
                            logging.info("save user timeline tweet")
                            self.timeline_tweets_inserted = self.timeline_tweets_inserted + 1
                        except couchdb.http.ResourceConflict:
                            logging.info("duplicate user timeline tweet")
                except couchdb.http.ResourceConflict:
                    logging.info("duplicate stream tweet")
            elif(rtw.intersects(rsy)):
                self.scount = self.scount + 1
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
                    dbtwitter.save(json.loads(json.dumps(text)))
                    logging.info("save tweet into Sydney database")
                    tweets_user = api.user_timeline(id=json_load['user']['id_str'],count=21,max_id=json_load['id_str'])
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
                            dbtwitter.save(json.loads(json.dumps(text)))
                            logging.info("save user timeline tweet")
                            self.timeline_tweets_inserted = self.timeline_tweets_inserted + 1
                        except couchdb.http.ResourceConflict:
                            logging.info("duplicate user timeline tweet")
                except couchdb.http.ResourceConflict:
                    logging.info("duplicate stream tweet")
            if(rtw.intersects(rbr)):
                self.bcount = self.bcount + 1
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
                    dbtwitter.save(json.loads(json.dumps(text)))
                    logging.info("save tweet into Brisbane database")
                    tweets_user = api.user_timeline(id=json_load['user']['id_str'],count=21,max_id=json_load['id_str'])
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
                            dbtwitter.save(json.loads(json.dumps(text)))
                            logging.info("save user timeline tweet")
                            self.timeline_tweets_inserted = self.timeline_tweets_inserted + 1
                        except couchdb.http.ResourceConflict:
                            logging.info("duplicate user timeline tweet")
                except couchdb.http.ResourceConflict:
                    logging.info("duplicate stream tweet")
            if(rtw.intersects(rpe)):
                self.pcount = self.pcount + 1
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
                    dbtwitter.save(json.loads(json.dumps(text)))
                    logging.info("save tweet into Perth database")
                    tweets_user = api.user_timeline(id=json_load['user']['id_str'],count=21,max_id=json_load['id_str'])
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
                            dbtwitter.save(json.loads(json.dumps(text)))
                            logging.info("save user timeline tweet")
                            self.timeline_tweets_inserted = self.timeline_tweets_inserted + 1
                        except couchdb.http.ResourceConflict:
                            logging.info("duplicate user timeline tweet")
                except couchdb.http.ResourceConflict:
                    logging.info("duplicate stream tweet")
            if(rtw.intersects(rad)):
                self.acount = self.acount + 1
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
                    dbtwitter.save(json.loads(json.dumps(text)))
                    logging.info("save tweet into Adelaide database")
                    tweets_user = api.user_timeline(id=json_load['user']['id_str'],count=21,max_id=json_load['id_str'])
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
                            dbtwitter.save(json.loads(json.dumps(text)))
                            logging.info("save user timeline tweet")
                            self.timeline_tweets_inserted = self.timeline_tweets_inserted + 1
                        except couchdb.http.ResourceConflict:
                            logging.info("duplicate user timeline tweet")
                except couchdb.http.ResourceConflict:
                    logging.info("duplicate stream tweet")
    
    def on_error(self,status):
        logging.info(status)
        
if __name__ == "__main__":
    starttime = time.time()
    listener = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    try:
        stream = Stream(auth,listener)
        stream.filter(locations=[113.338953078,-43.6345972634,153.569469029,-10.6681857235])
    except IncompleteRead:
        logging.warning("Incomplete read")
