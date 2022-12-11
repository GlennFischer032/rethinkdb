from rethinkdb import RethinkDB

r = RethinkDB()
r.connect("localhost", 49157).repl()
print(r.table('countries').run())
