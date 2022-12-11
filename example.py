from rethinkdb import RethinkDB

r = RethinkDB()
r.connect("localhost", 49154).repl()


# JOIN
# r.db('fakt').table('neviem_alkohol').index_create('Entity').run()
# r.db('fakt').table('neviem').index_create('country').run()
# print(r.db('fakt').table('neviem').eq_join('country', r.db('fakt').table('neviem_alkohol'), index="Entity").run())

res = r.db('fakt').table('neviem').run()
for item in res:
    print(item)

