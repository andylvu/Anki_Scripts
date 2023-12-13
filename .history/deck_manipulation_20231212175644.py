import sqlite3
from unidecode import unidecode

# function for unicase
def unicase_compare(x, y):
    x_ = unidecode(x).lower()
    y_ = unidecode(y).lower()
    return 1 if x_ > y_ else -1 if x_ < y_ else 0

# database information and deck info
database_path = 'C:\\Users\\Andy\\AppData\\Roaming\\Anki2\\Andy\\collection.anki2'
deck_name = 'test'


connection = sqlite3.connect(database_path)
connection.create_collation("unicase", unicase_compare)
cursor = connection.cursor()

# get deck id
cursor.execute("SELECT id FROM decks WHERE name=? COLLATE unicase", (deck_name,))
deck_id = cursor.fetchall()[0][0]
print(deck_id)

# get cards in deck
cursor.execute("SELECT * FROM cards JOIN notes ON cards.nid = notes.id WHERE did = ? COLLATE unicase", (deck_id,))
query = cursor.fetchall()
print(query)

for nid, flds in query:
    front, back = flds.split("\xlf")
    cursor.execute("UPDATE cards SET flds=? WHERE nid=? COLLATE unicase", (f"{back}\x1f{front}", nid))

#connection.commit()
#connection.close()

"1670479438455"