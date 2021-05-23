import couchdb
from datetime import datetime
import re
import string
import json
import logging
import sys
import langdetect
import tw_cdb_credentials

couch = couchdb.Server(url=tw_cdb_credentials.url)
couch.resource.credentials = tw_cdb_credentials.login
db = couch['twitter_melbourne']
db2 = couch['twitter_re5']

logfile = "Restructure " + datetime.today().strftime("%d-%b-%Y(%H-%M-%S.%f)") + ".log"

logging.basicConfig(filename=logfile, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

def strip_ahref(text):
    y = re.sub("<a.*\">", "", text)
    x = re.sub("</a>", "", y)
    return x

def strip_links(text):
    link_regex = re.compile(
        r'((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
    links = re.findall(link_regex, text)
    for link in links:
        text = text.replace(link[0], ', ')
    return text

#remove punctuation characters
def strip_all_entities(text):
    entity_prefixes = ['!', '?', ',', '.', '"']
    for separator in string.punctuation:
        if separator in entity_prefixes:
            text = text.replace(separator, ' ')
    return text

def happiness_score(happinessdict,tweettext):
    tweettextsplit = tweettext.split()
    #wordcount = 0
    worddict = 0
    tweetscore = 0
    avgtweetscore = 0
    for wordtweet in tweettextsplit:
        #wordcount = wordcount + 1
        if(wordtweet.isupper()):
            wordtweet = wordtweet.lower().strip()
            if wordtweet in happinessdict.keys():
                dictscore = happinessdict[wordtweet]
                if(happinessdict[wordtweet]>0):
                    dictscore = dictscore + 1
                elif(happinessdict[wordtweet]<0):
                    dictscore = dictscore - 1
                tweetscore = tweetscore + dictscore
                worddict = worddict + 1
        else:
            wordtweet = wordtweet.lower().strip()
            if wordtweet in happinessdict.keys():
                dictscore = happinessdict[wordtweet]
                tweetscore = tweetscore + dictscore
                worddict = worddict + 1
    if(worddict > 0):
        avgtweetscore = tweetscore/worddict
    return avgtweetscore

def restructure_json_couchdb(dict_word, couchdbdoc):
    tweet_text_stripped = strip_links(couchdbdoc['text'])
    tweet_text_stripped = strip_all_entities(tweet_text_stripped)
    #tweet_text = tweet_text_stripped.split()

    lang = ""
    try:
        lang = langdetect.detect(tweet_text_stripped)
    except :
        lang = "Not recognized"

    happiness = happiness_score(dict_word,tweet_text_stripped)

    geotweet = []
    coortweet = []
    bounding_box = []
    place_name = ""
    place_full_name = ""
    place_country = ""

    if(couchdbdoc['geo']):
        geotweet = couchdbdoc['geo']['coordinates']
    else:
        geotweet = couchdbdoc['geo']

    if(couchdbdoc['coordinates']):
        coortweet = couchdbdoc['coordinates']['coordinates']
    else:
        coortweet = couchdbdoc['coordinates']
    
    if(couchdbdoc['place']):
        bounding_box = couchdbdoc['place']['bounding_box']['coordinates'][0]
        place_name= couchdbdoc['place']['name']
        place_full_name = couchdbdoc['place']['full_name']
        place_country = couchdbdoc['place']['country']
    else:
        bounding_box = couchdbdoc['place']
        place_name = couchdbdoc['place']
        place_full_name = couchdbdoc['place']
        place_country = couchdbdoc['place']
    
    y = re.sub(".*elbourne.*", "Melbourne", couchdbdoc['user']['location'])
    z = re.sub(".*risbane.*", "Brisbane", y)
    a = re.sub(".*erth.*", "Perth", z)
    b = re.sub(".*delaide.*", "Adelaide", a)
    c = re.sub(".*ydney.*", "Sydney", b)
    d = re.sub(".*ew South Wales.*", "New South Wales", c)
    e = re.sub(".*ueensland.*", "Queensland", d)
    f = re.sub(".*ictoria.*", "Victoria", e)
    g = re.sub(".*estern Australia.*", "Western Australia", f)
    loc = re.sub(".*outh Australia.*", "South Australia", g)

    text = {'_id': i,
            'created_at': couchdbdoc['created_at'],
            'text': couchdbdoc['text'],
            'source': strip_ahref(couchdbdoc['source']),
            'user_id': couchdbdoc['user']['id_str'],
            'user_screen_name': couchdbdoc['user']['screen_name'],
            'user_followers_count': couchdbdoc['user']['followers_count'],
            'user_friends_count': couchdbdoc['user']['friends_count'],
            'user_location': loc,
            'geo': geotweet,
            'coordinates': coortweet,
            'place_name': place_name,
            'place_full_name': place_full_name,
            'place_country': place_country,
            'place_bounding_box': bounding_box,
            'retweet_count': couchdbdoc['retweet_count'],
            'favorite_count': couchdbdoc['favorite_count'],
            'happines': happiness,
            'lang_detected': lang
            }
    return text

if __name__ == "__main__":
    list_word = open("AFINN.txt", "r")
    word = list_word.readlines()
    value = []
    key = []
    for kata in word:
        m = kata.split()
        if len(m) > 2:
            v = (' '.join((m[0:(len(m)-1)])))
            key.append(v.strip())
        else:
            key.append(m[0].strip())
        a = m[-1].strip()
        value.append(int(a))

    dict_words = dict(zip(key, value))

    list_word.close()
    count = 0

    for docid in db.view('_all_docs'):
        count = count + 1
        i = docid['id']
        doc = db[i]

        text = restructure_json_couchdb(dict_words,doc)
        try:
            db2.save(json.loads(json.dumps(text)))
        except couchdb.http.ResourceConflict:
            logging.info("duplicate tweet")

    #print(str(count) + " text=" + doc['text'] + "\n wordcount=" + str(wordcount) + " tweetscore=" + str(tweetscore) + " worddict=" + str(worddict) + " average=" + str(avgtweetscore))

