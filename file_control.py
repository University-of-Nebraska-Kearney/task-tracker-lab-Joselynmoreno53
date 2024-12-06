import os
# Create a function called load_tasks that reads tasks from a file
# into a list and then returns the list.
def load_tasks(tasks):
    tasks = []
    if os.path.exists("tasks.txt"):
        file = open("tasks.txt", "r" )
        lines = file.readlines()
        file.close()

        for line in lines:
            line = line.strip()
            if line == " ":
                continue 

            parts = line.split(" , ")

            if len(parts) == 4: 
                title, description, due_date, status = parts
                tasks.append({"title": title, "description": description, "due_date": due_date, "status": status})
            else:
                print(f"Skipping invalid line: {line}")
    return tasks 




# Create a function called save_tasks that takes a list of tasks and 
# writes them to a file for long non-volatile storage.
def save_tasks(tasks):
    with open("task.txt", "w") as file:
        for task in tasks:
            file.write= f"{task['title']} | {task['description']} | {task['due_date']} | {task['status']}\n"
            
        