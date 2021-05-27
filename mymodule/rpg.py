import sqlite3
import pandas as pd
import mymodule.queries as queries

conn = sqlite3.connect("../rpg_db.sqlite3")

curs = conn.cursor()

"""select * from armory_weapon
                        left join armory_item on armory_weapon.item_ptr_id = armory_item.item_id
                        """

select_weapon_query = """
SELECT char_id, count(aw.item_ptr_id)
FROM (SELECT cc.character_id char_id, cci.item_id item_id
        FROM charactercreator_character cc
        LEFT JOIN charactercreator_character_inventory cci
        on cc.character_id = cci.character_id) AS char_item
LEFT JOIN armory_weapon aw
    ON char_item.item_id = aw.item_ptr_id
GROUP BY char_id
LIMIT 20
"""

weapon_results = curs.execute(queries.CHARACTER_WEAPONS).fetchall()

weapon_df = pd.DataFrame(weapon_results)

conn.close()

print(weapon_df.head())

