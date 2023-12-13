import sqlite3

database_path = 'C:\Users\Andy\AppData\Roaming\Anki2'

connection = sqlite3.connect(database_path)
cursor = connection.cursor()
