import psycopg2

def get_connection():
    connection = psycopg2.connect(
        host="localhost",
        database="todo_db",
        user="postgres",
        password="Nnaemezie21.",
        port="5432"
)
    return connection
print("Connected Successfully!")
