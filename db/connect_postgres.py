import psycopg2

#Connect to To-do database
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

#Connect to Baby_names database
def get_connection():
    connection = psycopg2.connect(
        host="localhost",
        database="baby_names_db",
        user="postgres",
        password="Nnaemezie21.",
        port="5432"
)
    return connection
print("Connected Successfully!")
