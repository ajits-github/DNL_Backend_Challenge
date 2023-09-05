import sqlite3
from database.db_manager import initialize_database, store_to_db

from config_util import config

DB_PATH = config['database']['path']

# def test_initialize_database():
#     # Function to check if the table exists
#     assert initialize_database() == True

def test_store_and_retrieve_data():
    sample_data = [{
        'manufacturer': 'Ammann',
        'category': 'Ammann',
        'model': 'Roller Parts',
        'part_number': 'ND011710',
        'part_category': 'LEFT COVER'
    }]

    store_to_db(sample_data)

    # Logic to fetch data from DB to verify it's been inserted
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM parts_data WHERE manufacturer=?", ('Ammann',))
    data = cursor.fetchone()
    conn.close()

    assert data is not None
