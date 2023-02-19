"""
Фильтрация данных
Условия - совпадение, диапазоны, вхождения, пустые значения
Комбинации - логические операторы
"""

import sqlite3

with sqlite3.connect("../14.1/netflix.db") as connection:
    cursor = connection.cursor()
    query = """
            SELECT release_year, title, director
            FROM netflix
            WHERE director != '' AND director IS NOT NULL
            
    """
    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

