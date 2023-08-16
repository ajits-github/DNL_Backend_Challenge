import sqlite3

from config_util import config

DB_PATH = config['database']['path']

def store_to_db(data):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    # Create the table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS parts_data (
        id INTEGER PRIMARY KEY,
        manufacturer TEXT,
        category TEXT,
        model TEXT,
        part_number TEXT,
        part_category TEXT
    )
    """)
    
    # Insert data
    for entry in data:
        cursor.execute("""
        INSERT INTO parts_data (manufacturer, category, model, part_number, part_category)
        VALUES (?, ?, ?, ?, ?)
        """, (entry['manufacturer'], entry['category'], entry['model'], entry['part_number'], entry['part_category']))
        
    connection.commit()
    connection.close()

