import sqlite3

from config_util import config

DB_PATH = config['database']['path']

def data_exists():
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM parts_data LIMIT 10''')
        
        if cursor.fetchone()[0] == 1:
            return True
        return False
    except sqlite3.Error as e:
        print(e)
        return False
    finally:
        if conn:
            conn.close()

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

