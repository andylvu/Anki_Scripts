import sqlite3
from unidecode import unidecode

def unicase_compare(x, y):
    x_ = unidecode(x).lower()
    y_ = unidecode(y).lower()
    return 1 if x_ > y_ else -1 if x_ < y_ else 0

database_path = 'C:\\Users\\Andy\\AppData\\Roaming\\Anki2\\Andy\\collection.anki2'
deck_name = 'Chinese Food'

connection = sqlite3.connect(database_path)
connection.create_collation("unicase", unicase_compare)
cursor = connection.cursor()
cursor.execute("SELECT id FROM decks WHERE name=? COLLATE unicase", (deck_name,))
deck_id = cursor.fetchall()[0]
print(deck_id[0])
cursor.execute("SELECT id, flds FROM decks WHERE name=? COLLATE unicase", (deck_id,))
cards = cursor.fetchall()
print(cards)