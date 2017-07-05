import sqlite3

conn = sqlite3.connect('player_comps.db')
c = conn.cursor()

def create_tables():

    c.execute('CREATE TABLE IF NOT EXISTS per40_comps(name TEXT, ppg REAL)')
    c.execute('CREATE TABLE IF NOT EXISTS advanced_comps(name TEXT, per REAL)')

def data_entry():
    c.execute('INSERT INTO per40_comps VALUES("Andrew Bogut", 19.3)')
    conn.commit()
    c.execute('INSERT INTO advanced_comps VALUES("Andrew Bogut", 7.1)')
    conn.commit()
    c.close()
    conn.close()

create_tables()
data_entry()