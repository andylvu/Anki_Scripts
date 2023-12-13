import sqlite3

database_path = 'C:/Users/Andy/AppData/Roaming/Anki2'
deck_name = 'Chinese Food'

connection = sqlite3.connect(database_path)
cursor = connection.cursor()
cursor.execute("SELECT id FROM decks WHERE name=?", deck_name)
deck_info = cursor.fetchone()
print(deck_info)