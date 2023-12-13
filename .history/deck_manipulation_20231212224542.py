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


# Loop through the cards
# Loop through the cards
for nid, flds in query:
    string = str(flds)
    
    # Split the string at ▼ and strip the parts
    parts = string.split("▼")
    front = parts[0].strip("'").strip()
    back = parts[1].strip()

    # Print the extracted front and back for debugging
    print(f"Front: {front}")
    print(f"Back (Chinese and Pinyin): {back}")

    # Update the notes with the rearranged content
    cursor.execute("UPDATE notes SET flds=? WHERE id=? COLLATE unicase", (f"{back}▼{front}", nid))


# Print all cards after the update for debugging
cursor.execute("SELECT nid, flds FROM cards JOIN notes ON cards.nid = notes.id WHERE did = ? COLLATE unicase", (deck_id,))
updated_query = cursor.fetchall()
for nid, fields in updated_query:
    print(f"Card ID: {nid}, flds content: {fields}")

# connection.commit()
# connection.close()

"1670479438455"