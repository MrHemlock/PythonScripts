import sqlite3

with sqlite3.connect('example.db') as conn:
    c = conn.cursor()
    c.execute('''CREATE TABLE stocks
    (date text, trans text, symbol text, qty real, price real)''')
    c.execute("INSERT INTO stocks VALUES ('2006-01-05', 'BUY', 'RHAT',100,35.14)")
    conn.commit()

'''
An idea just struck me.  When I'm going to be using the SQLite db,
I can instantiate the various monsters into an enemy party list,
and just generate the rest of the information from the row queries and the like
'''
