import sqlite3
# connection = sqlite3.connect(':memory:')
connection = sqlite3.connect('customer.db')

cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE customers(
        first_name text,
        last_name text,
        email text,
    )
''')


connection.commit()


connection.close()