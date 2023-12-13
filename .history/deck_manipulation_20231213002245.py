import sqlite3
from unidecode import unidecode
import re

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

# get cards in deck
cursor.execute("SELECT nid, flds FROM cards JOIN notes ON cards.nid = notes.id WHERE did = ? COLLATE unicase", (deck_id,))
query = cursor.fetchall()
first_card = query[0]



nid, fields = first_card[0], first_card[1]
print(f"Card ID: {nid}, flds content: {fields}")


for id, flds in query:
    
    string = str(flds)
    # Adjust the split based on HTML line break <br>
    fields = string.split("\x1f")
    
    # Assuming front is the first field and back is the second
    front, back = fields[0], fields[1]
    cleaned_front = re.sub(r"[']", "", front)
    cleaned_back = re.sub(r"['<br>]+", "", back)
    

    print(cleaned_front, cleaned_back)
    
    cursor.execute("UPDATE notes SET flds=? WHERE id=? COLLATE unicase", (f"{cleaned_back}\x1f{cleaned_front}", id))

cursor.execute("SELECT nid, flds FROM cards JOIN notes ON cards.nid = notes.id WHERE did = ? COLLATE unicase", (deck_id,))
query = cursor.fetchall()
first_card = query[0]
nid, fields = first_card[0], first_card[1]
print('after swap')
print(f"Card ID: {nid}, flds content: {fields}")

connection.commit()
connection.close()

"1670479438455"