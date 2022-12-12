from rethinkdb import RethinkDB

r = RethinkDB()
r.connect("localhost", 49157).repl()

db = r.db('fakt')

# JOIN
# db.table('neviem_alkohol').index_create('Entity').run()
# db.table('neviem').index_create('country').run()
#print(db.table('neviem').eq_join('country', db.table('neviem_alkohol'), index="Entity").run())


# GEO QUERY
# res = db.table('neviem').run()
# for item in res:
#     if 'latitude' not in item or 'longitude' not in item:
#         continue
#     db.table('neviem').get(item['id']).update({'location': r.point(float(item["longitude"]), float(item["latitude"]))}).run()

# print(db.table('neviem').run())
# print(db.table('neviem').get_nearest(r.point(8.981666, 17.00778), index='location', max_results=10, unit='km').run())
# print(db.table('neviem').get('11017e65-3fc7-44a7-b0f1-2062a662c30e')['location'].distance(db.table('neviem').get('0d4cbf7e-933c-43dc-9626-6571c5d99ce4')['location'], unit='km').run())

