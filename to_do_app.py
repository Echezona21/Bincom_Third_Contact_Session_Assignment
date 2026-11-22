from connect_postgres import get_connection
connection = get_connection()

#Create a cursor object to interact with the database
cursor = connection.cursor()
#Create a table to store tasks
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
    id SERIAL PRIMARY KEY,
    task_name VARCHAR(100),
    completed BOOLEAN DEFAULT FALSE
)
""")

connection.commit()

print("Table Created Successfully")
