import sqlite3
# connection = sqlite3.connect(':memory:')
connection = sqlite3.connect('customer.db')

cursor = connection.cursor()

many_customers=[
    ('1','2','3'),
('4','5','6'),
('7','8','9'),
]

cursor.executemany('''
    INSERT INTO customers VALUES (
        ?,
        ?,
        ?
    )
''',many_customers)


connection.commit()


connection.close()