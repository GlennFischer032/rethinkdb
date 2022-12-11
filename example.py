from rethinkdb import RethinkDB

r = RethinkDB()
r.connect("localhost", 49154).repl()

db = r.db('fakt')
# JOIN
# db.table('neviem_alkohol').index_create('Entity').run()
# db.table('neviem').index_create('country').run()
# print(db.table('neviem').eq_join('country', db.table('neviem_alkohol'), index="Entity").run())


# GEO QUERY
# res = db.table('neviem').run()
# for item in res:
#     if 'latitude' not in item or 'longitude' not in item:
#         continue
#     db.table('neviem').get(item['id']).update({'location': r.point(float(item["latitude"]), float(item["longitude"]))}).run()

# db.table('neviem').index_create('location', geo=True).run()
# print(db.table('neviem').get('eb73be08-02d7-4aad-aa3d-4acb4aa43d21')['location'].distance(db.table('neviem').get('ddc5c8de-8f1e-4ec3-adbf-2411078c7bb6')['location']).run())
