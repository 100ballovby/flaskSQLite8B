import sqlite3

conn = sqlite3.connect('main.db')
print('Successfully created database')

conn.execute('''
CREATE TABLE students 
(name TEXT, addr TEXT,
city TEXT, pin INT);
''')
print('Table created!')
conn.close()