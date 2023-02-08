import sqlite3
# connection = sqlite3.connect(':memory:')
connection = sqlite3.connect('customer.db')

cursor = connection.cursor()

many_customers=[
    ('1','2','3'),
('4','5','6'),
('7','8','9'),
]

cursor.execute('''
   SELECT rowid,* FROM customers
''')

print(cursor.fetchall())

connection.commit()


connection.close()