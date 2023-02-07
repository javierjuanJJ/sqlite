import sqlite3
# connection = sqlite3.connect(':memory:')
connection = sqlite3.connect('customer.db')

cursor = connection.cursor()

cursor.execute('''
    INSERT INTO customers VALUES (
        '1',
        '2',
        '3'
    )
''')


connection.commit()


connection.close()