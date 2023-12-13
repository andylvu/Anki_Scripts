import sqlite3

database_path = 'C:\\Users\\Andy\\AppData\\Roaming\\Anki2\\Andy\\collection.anki2'
deck_name = 'Data Science'

connection = sqlite3.connect(database_path)
cursor = connection.cursor()
cursor.execute("SELECT id FROM decks WHERE name=? COLLATE unicase", (deck_name,))
deck_id = cursor.fetchall()
print(deck_id)