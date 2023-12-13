import sqlite3
from unidecode import unidecode

# function for unicase
def unicase_compare(x, y):
    x_ = unidecode(x).lower()
    y_ = unidecode(y).lower()
    return 1 if x_ > y_ else -1 if x_ < y_ else 0

# database information and deck info
database_path = 'C:\\Users\\Andy\\AppData\\Roaming\\Anki2\\Andy\\collection.anki2'
deck_name = 'Chinese  Food'


connection = sqlite3.connect(database_path)
connection.create_collation("unicase", unicase_compare)
cursor = connection.cursor()

# get deck id
cursor.execute("SELECT id FROM decks WHERE name=? COLLATE unicase", (deck_name,))
deck_id = cursor.fetchall()[0][0]
print(deck_id)

# get cards in deck
cursor.execute("SELECT nid, flds FROM cards JOIN notes ON cards.nid = notes.id WHERE did = ? COLLATE unicase", (deck_id,))
query = cursor.fetchall()
first_card = query[0]
nid, fields = first_card[0], first_card[1]
print(f"Card ID: {nid}, flds content: {fields}")
print(f"third field item {fields[0]}")


for id, flds in query:
    
    # Adjust the split based on HTML line break <br>
    fields = flds.split("<br>")
    
    # Assuming front is the first field and back is the second
    front, mid, back = fields[0], fields[1], fields[2]
    
    cursor.execute("UPDATE notes SET flds=? WHERE id=? COLLATE unicase", (f"{back}<br>{front}", id))

cursor.execute("SELECT nid, flds FROM cards JOIN notes ON cards.nid = notes.id WHERE did = ? COLLATE unicase", (deck_id,))
query = cursor.fetchall()
first_card = query[0]
nid, fields = first_card[0], first_card[1]
print(f"Card ID: {nid}, flds content: {fields}")

#connection.commit()
#connection.close()

"1670479438455"