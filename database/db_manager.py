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

# =============================== AZURE ==========================================

# import os
# import sqlite3
# from azure.storage.blob import BlobServiceClient
# from config_util import config

# # Load environment variables from .env file
# from dotenv import load_dotenv
# load_dotenv()

# DB_PATH = config['database']['path']
# # BLOB_CONNECTION_STRING = os.getenv('BLOB_CONNECTION_STRING')
# BLOB_CONNECTION_STRING = os.getenv('DATABASE_CONNECTION_STRING')
# BLOB_CONTAINER_NAME = os.getenv('BLOB_CONTAINER_NAME', 'mycontainer')  # default container name as 'mycontainer'
# DB_BLOB_NAME = 'scraped_data.db'

# blob_service_client = BlobServiceClient.from_connection_string(BLOB_CONNECTION_STRING)
# blob_client = blob_service_client.get_blob_client(container=BLOB_CONTAINER_NAME, blob=DB_BLOB_NAME)

# def initialize_database():
#     if not blob_client.exists():
#         # Create an in-memory database
#         con = sqlite3.connect(':memory:')
#         cursor = con.cursor()

#         # Create tables
#         cursor.execute('''
#         CREATE TABLE IF NOT EXISTS parts_data (
#             id INTEGER PRIMARY KEY,
#             manufacturer TEXT,
#             category TEXT,
#             model TEXT,
#             part_number TEXT,
#             part_category TEXT
#         )
#         ''')

#         con.commit()

#         # Convert the in-memory database into bytes and upload to Azure Blob storage
#         # db_bytes = con.iterdump().encode('utf-8')
#         db_string = '\n'.join(con.iterdump())
#         db_bytes = db_string.encode('utf-8')
#         blob_client.upload_blob(db_bytes)
        
#         con.close()

# def get_connection():
#     # db_stream = blob_client.open_query()
#     # Download the blob content
#     blob_data = blob_client.download_blob()
#     content = blob_data.readall()

#     # write it to a temporary file and then use sqlite3 to connect
#     temp_filename = "/tmp/scraped_data.db"
#     with open(temp_filename, 'wb') as f:
#         f.write(content)

#     # Return the sqlite connection
#     return sqlite3.connect(temp_filename)
#     # return sqlite3.connect(db_stream)

# def data_exists():
#     conn = None
#     try:
#         conn = get_connection()

#         cursor = conn.cursor()
#         cursor.execute('''SELECT * FROM parts_data LIMIT 10''')

#         if cursor.fetchone():
#             return True
#         return False
#     except sqlite3.Error as e:
#         print(e)
#         return False
#     finally:
#         if conn:
#             conn.close()

# def store_to_db(data):
#     conn = get_connection()
#     cursor = conn.cursor()

#     # Insert data
#     for entry in data:
#         cursor.execute("""
#         INSERT INTO parts_data (manufacturer, category, model, part_number, part_category)
#         VALUES (?, ?, ?, ?, ?)
#         """, (entry['manufacturer'], entry['category'], entry['model'], entry['part_number'], entry['part_category']))

#     conn.commit()
#     conn.close()

