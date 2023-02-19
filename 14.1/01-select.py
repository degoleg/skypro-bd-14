"""
Получение данных из таблицы
"""

import sqlite3

with sqlite3.connect("../14.1/netflix.db") as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM netflix")


for row in cursor.fetchall():
    print(row)
