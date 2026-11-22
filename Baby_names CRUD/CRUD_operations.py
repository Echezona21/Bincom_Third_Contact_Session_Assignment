import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from db.connect_postgres import get_connection
connection = get_connection("baby_names_db")

#Create a cursor object to interact with the database
cursor = connection.cursor()
#Create a table to store baby names
cursor.execute("""
CREATE TABLE IF NOT EXISTS baby_names(
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
)
""")

connection.commit()

print("Table Created Successfully")
