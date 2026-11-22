import psycopg2

#Connect to To-do database
def get_connection(db_name):
    connection = psycopg2.connect(
        host="localhost",
        database=db_name,
        user="postgres",
        password="Nnaemezie21.",
        port="5432"
)
    return connection
print("Connected Successfully!")


