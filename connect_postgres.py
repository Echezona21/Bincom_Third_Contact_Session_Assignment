import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="todo_db",
    user="postgres",
    password="Nnaemezie21.",
    port="5432"
)

print("Connected Successfully!")