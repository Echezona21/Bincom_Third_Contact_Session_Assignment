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

#Create a list of tasks to add to the database
tasks = [
    "Learn Python",
    "Learn PostgreSQL",
    "Build Todo App",
    "Practice CRUD",
    "Learn Functions",
    "Study APIs",
    "Learn Git",
    "Create Portfolio",
    "Apply for Internship",
    "Finish Assignment"
]

for task in tasks:
    cursor.execute(
        "INSERT INTO tasks(task_name) VALUES(%s)",
        (task,)
    )

connection.commit()

print("10 Tasks Added Successfully")

#Read all tasks from the database
cursor.execute("SELECT * FROM tasks")
tasks = cursor.fetchall()
for task in tasks:
    print(task)

#Update a task in the database
cursor.execute("""
UPDATE tasks
SET completed = TRUE
WHERE id = %s
""", (1,))

connection.commit()

