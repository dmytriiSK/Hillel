import sqlite3
def execute_query(query, args=()):
    with sqlite3.connect('HW4//chinook.db') as connection:
        cursor = connection.cursor()
        cursor.execute(query, args)
        connection.commit()
        result = cursor.fetchall()
    return result

