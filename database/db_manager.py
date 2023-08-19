import os
import sqlite3
from config_util import config

DB_PATH = config['database']['path']

def ensure_directory_exists():
    db_dir = os.path.dirname(DB_PATH)
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)

def initialize_database():
    ensure_directory_exists()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create tables, if they don't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS parts_data (
        id INTEGER PRIMARY KEY,
        manufacturer TEXT,
        category TEXT,
        model TEXT,
        part_number TEXT,
        part_category TEXT
    )
    ''')
    
    conn.commit()
    conn.close()

def data_exists():
    
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM parts_data LIMIT 10''')
        
        if cursor.fetchone():
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

    # Insert data
    for entry in data:
        cursor.execute("""
        INSERT INTO parts_data (manufacturer, category, model, part_number, part_category)
        VALUES (?, ?, ?, ?, ?)
        """, (entry['manufacturer'], entry['category'], entry['model'], entry['part_number'], entry['part_category']))
        
    connection.commit()
    connection.close()

# initialize_database()