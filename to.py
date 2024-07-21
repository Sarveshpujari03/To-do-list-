tasks = []

def newtask():
    tasks.append(input("Enter the task: "))
    print("Task added successfully!!!")

def listtask():
    if not tasks:
        print("You don't have any tasks currently.")
    else:
        print("Your tasks are:")
        for i, task in enumerate(tasks):
            print(f"{i}. {task}")

def deletetask():
    listtask()
    try:
        todelete = int(input("Enter the index of the task you want to delete: "))
        if 0 <= todelete < len(tasks):
            tasks.pop(todelete)
            print("Task deleted successfully!!!")
        else:
            print("Invalid index. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    print("Welcome to the task manager")
    while True:
        print("Welcome to the To-Do List!!!")
        print("-------------------------")
        print("Please select an option below")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List all the tasks")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            newtask()
        elif choice == "2":
            deletetask()
        elif choice == "3":
            listtask()
        elif choice == "4":
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
