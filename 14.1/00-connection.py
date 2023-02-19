"""
Подключение к SQLite 3
"""

import sqlite3

with sqlite3.connect("../14.1/netflix.db") as connection:
    cursor = connection.cursor()
    cursor.execute("ЗДЕСЬ БУДУТ НАШИ КОММАНДЫ")
