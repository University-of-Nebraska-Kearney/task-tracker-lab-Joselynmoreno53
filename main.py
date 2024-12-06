# Import library of functions
from file_control import load_tasks, save_tasks
def main():
  # Get tasks from file
  tasks = []
  tasks = load_tasks(tasks)

  # Create loop for menu
  while True:
    print("---Task Tracker Menu---")
    print("1. Display tasks",
         "\n2. Add tasks",
         "\n3. Mark task as complete",
         "\n4. Save and exit")

    # Get user choice
    choice = input()

    # Navigate user based on choice
    if choice == "1":
      display_tasks(tasks)
    elif choice == "2":
      add_task(tasks)
    elif choice == "3":
      complete_tasks(tasks)
    elif choice == "4":
      save_tasks(tasks)
      print("Thank you for using Task Tracker.")
      break
    else:
      print("That is not a valid option.")



# Create a function called display_tasks that takes a list of taks and
# displays every task in the list.
def display_tasks(tasks):
  # check for tasks
  if not tasks: 
    print("No task available.")
  else:
    for i in range(len(tasks)):
      print(f"{i + 1}. {tasks[i]['title']} - {tasks[i]['description']} - Due: {tasks[i]['due_date']} - Status: {task[i]['status']}")




# Create a function called add_task that takes a list of tasks, prompts
# the user for another task, and then appends the new tasks to the 
# end of the list.
def add_task(tasks):
  title = input("Enter task title: ")
  description = input("Enter task description: ")
  due_date = input("Enter due date (YYYY-MM-DD): ")

  task = { "title": title, "description": description, "due_date": due_date, "status": "Not Completed"}
  tasks = tasks + [task]
  print("Task added successfully!") 
  return tasks



# Create a function called complete that takes a lists of tasks,
# displays them to the user, and then lets the user choose one
# to mark as complete. It will then update the status of the 
# task in the list and return the updated list.
def complete_tasks(tasks):
  if not tasks:
    print("No tasks to complete.")
    return

    display_tasks(tasks)

    try: 
      task_number = int(input("Enter the number of the task you've completed: "))
      if task_number > 0 and task_number <= len(tasks):
        tasks[task_number - 1]["status"] = "complete"
        print("Task has been marked as complete! ")
      else: 
        print("Invalid task number ")
    except ValueError:
      print("Please enter a valid number. ")
      
  



if __name__ == "__main__":
  main()
