import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from db.connect_postgres import get_connection
connection = get_connection("todo_db")
                            
#Create a cursor object to interact with the database
cursor = connection.cursor()
#Create a table to store tasks
def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
    id SERIAL PRIMARY KEY,
    task_name VARCHAR(100),
    completed BOOLEAN DEFAULT FALSE)
""")
    connection.commit()
    print("Table Created Successfully")

#Add a task to the database
def add_task(task):
    cursor.execute(
        "INSERT INTO tasks(task_name) VALUES(%s)",
        (task,)
    )
    connection.commit()

#Read all tasks from the database
def view_tasks():
    cursor.execute("SELECT * FROM tasks")
    all_tasks = cursor.fetchall()
    return all_tasks

#Update a task in the database
def update_task(task_id):
    cursor.execute("""
    UPDATE tasks
    SET completed = TRUE
    WHERE id = %s
    """, (task_id,))
    connection.commit()

#Delete a task from the database
def delete_task(task_id):
    cursor.execute("""
    DELETE FROM tasks
    WHERE id = %s
    """, (task_id,))

    connection.commit()


def main():
    while True:
        print("\n===== MY TO-DO APPLICATION =====")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Mark task as completed")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("\nSelect an option: ")
    #Conditional statements to handle user input
        if choice == "1":
            task = input("Enter your task: ")
            add_task(task)
            print("Task added successfully!")
    #Conditional statements to handle user input
        elif choice == "2":
            tasks = view_tasks()
    
            for task in tasks:
                print(task)
    #Conditional statements to handle user input
        elif choice == "3":
            task_id = int(input("Enter task ID: "))
            update_task(task_id)
    #Conditional statements to handle user input
        elif choice == "4":
            task_id = int(input("Enter task ID: "))
            delete_task(task_id)
    #Conditional statements to handle user input
        elif choice == "5":
            print("Thank you for using the To-Do App!")
            break
    #Conditional statements to handle no user input
        else:
            print("Invalid selection. Try again.")


if __name__ == "__main__":
    create_table()
    main()


#Close the cursor and connection
cursor.close()
connection.close()