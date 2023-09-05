import sqlite3
from database.db_manager import initialize_database, store_to_db

def test_initialize_database():
    # Assuming that you have a function to check if the table exists
    assert initialize_database() == True

def test_store_and_retrieve_data():
    sample_data = [{
        'manufacturer': 'Test Manufacturer',
        'category': 'Test Category',
        'model': 'Test Model',
        'part_number': '12345',
        'part_category': 'Test Part Category'
    }]

    store_to_db(sample_data)

    # Logic to fetch data from DB to verify it's been inserted
    conn = sqlite3.connect('your_database_name.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM your_table_name WHERE manufacturer=?", ('Test Manufacturer',))
    data = cursor.fetchone()
    conn.close()

    assert data is not None
