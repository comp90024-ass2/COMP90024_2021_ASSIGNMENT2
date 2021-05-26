import couchdb
import json

couch = couchdb.Server(url='http://172.26.131.86:5984/')
couch.resource.credentials = ('admin', 'admin')
db = couch['unemployment']

db_entry = {}

with open('unemployment.json') as jsonfile:
    jsondata = json.loads(jsonfile.read())
    db_entry = {}
    for data in jsondata['features']:
        db_entry = data['properties']
        print(db_entry)
        db.save(json.loads(json.dumps(db_entry)))

#with open('Income_S.json') as jsonfile2:
#    jsondata = json.loads(jsonfile2.read())
#    db_entry = {}
#    for data in jsondata['features']:
#        db_entry = data['properties']
#        db.save(json.loads(json.dumps(db_entry)))



