import pymongo
import sqlite3
import os

mongo_url = os.environ['MONGO_CLIENT']  # could not connect to my cluster

client = pymongo.MongoClient(
    "mongodb://localhost/myFirstDatabase?retryWrites=true&w=majority"
)  # used a docker instance provided by the tutor

db = client['my_db']  # create database
if 'rgb_data' not in db.list_collection_names():
    db.create_collection('rgb_data')  # create collection within the database

print("collections in 'my_db':", db.list_collection_names())
print("list of databases:", client.list_database_names())

# get column names from character table

sqlite_conn = sqlite3.connect('../rpg_db.sqlite3')
sqlite_cursor = sqlite_conn.cursor()

characters_cols = """
pragma table_info(charactercreator_character)
"""
result = sqlite_cursor.execute(characters_cols).fetchall()
print('table info:', result)
cols = []
for _ in result:
    cols.append(_[1])
print('col names: ', cols)

# extract from queries and then input to mongo

characters_query = """
select * from charactercreator_character
"""
db['rgb_data'].delete_many({})  # empty the collection
result = sqlite_cursor.execute(characters_query).fetchall()
for character in result:
    input_dic = {}
    for i, var in enumerate(character):
        input_dic.update({cols[i]: var})  # cols = table col names
    character_id = (input_dic['character_id'],) # create variable to use in queries as "?"
    # build items list
    items_query = """
    select name
    from charactercreator_character_inventory
    left join armory_item ai on charactercreator_character_inventory.item_id = ai.item_id
    where character_id = ? 
    """
    result = sqlite_cursor.execute(items_query, character_id).fetchall()
    items = []
    for _ in result:
        items.append(_[0])
    input_dic.update({'items': items})
    # build weapons list
    weapons_query = """
    select name
    from charactercreator_character_inventory
    left join armory_item ai on charactercreator_character_inventory.item_id = ai.item_id
    left join armory_weapon aw on ai.item_id = aw.item_ptr_id
    where character_id = ?
    and ai.item_id = aw.item_ptr_id
    """
    result = sqlite_cursor.execute(weapons_query, character_id).fetchall()
    weapons = []
    for _ in result:
        weapons.append(_[0])
    input_dic.update({'weapons': weapons})

    db['rgb_data'].insert_one(input_dic)

for _ in db.rgb_data.find({'character_id': 5}):
    print(_)
