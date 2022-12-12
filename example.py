from rethinkdb import RethinkDB

r = RethinkDB()
r.connect("localhost", 49157).repl()

db = r.db('fakt')

# JOIN
#create secondary index on Entity field(country name)
db.table('country_alcohol_consumption').index_create('Entity').run()
#create secondary index on country field(country name)
db.table('country_locations').index_create('country').run()
#join tables and print result
print(db.table('country_locations').eq_join('country', db.table('country_alcohol_consumption'), index="Entity").run())


# GEO QUERY
res = db.table('country_locations').run()
# create location field
for item in res:
    if 'latitude' not in item or 'longitude' not in item:
        continue
    db.table('country_locations').get(item['id']).update({'location': r.point(float(item["longitude"]), float(item["latitude"]))}).run()

# create geosptaial index
db.table('country_locations').index_create('location', geo=True).run()

#find the nearest country to the coordinates
print(db.table('country_locations').get_nearest(r.point(8.981666, 17.00778), index='location').run())

#disctance between the United States and the Czech Republic =~ 8228 km
print(db.table('country_locations').get('11017e65-3fc7-44a7-b0f1-2062a662c30e')['location'].distance(db.table('neviem').get('0d4cbf7e-933c-43dc-9626-6571c5d99ce4')['location'], unit='km').run())

