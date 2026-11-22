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

#Extract names from the HTML file and insert them into the database using code from assignment.py in previous assignment
file = open("Baby_names CRUD/baby2008.html", "r")
values = file.read()
file.close()
#Extraction using regex
import re
pattern = r'<td>\d+</td><td>([A-Za-z]+)</td><td>([A-Za-z]+)</td>'
matches = re.findall(pattern, values)
print("Extracted Names: ", matches[:5])
names = []
for boy, girl in matches:
    names.append(boy)
    names.append(girl)
print(names[:5])

#Sort the names in alphabetical order
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

sorted_names = bubble_sort(names)
print("Sorted Names: ", sorted_names[:20])

for name in sorted_names:
    cursor.execute(
        """
        INSERT INTO baby_names(name)
        VALUES(%s)
        ON CONFLICT DO NOTHING
        """,
        (name,)
    )

connection.commit()

print("Names inserted successfully")

#CRUD functions examples for baby names table
def create_baby_name(name):
    cursor.execute(
        """
        INSERT INTO baby_names(name)
        VALUES(%s)
        ON CONFLICT DO NOTHING
        """,
        (name,)
    )
    connection.commit()
    print(f"Baby name '{name}' added successfully.")
    
def read_baby_names():
    cursor.execute("SELECT name FROM baby_names ORDER BY name")
    return cursor.fetchall()

def update_baby_name(old_name, new_name):
    cursor.execute(
        """
        UPDATE baby_names
        SET name = %s
        WHERE name = %s
        """,
        (new_name, old_name)
    )
    connection.commit()
    print(f"Baby name updated from '{old_name}' to '{new_name}'.")

def delete_baby_name(name):
    cursor.execute(
        """
        DELETE FROM baby_names
        WHERE name = %s
        """,
        (name,)
    )
    connection.commit()
    print(f"Baby name '{name}' deleted successfully.")