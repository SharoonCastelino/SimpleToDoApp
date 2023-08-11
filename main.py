from todo import ToDoList

def main():
    todo_list = ToDoList()

    while True:
        print("\nSimple To-Do App")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            task = input("Enter task description: ")
            todo_list.add_task(task)
            print("Task added!")
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            index = int(input("Enter task index to remove: "))
            if todo_list.remove_task(index):
                print("Task removed!")
            else:
                print("Invalid index.")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
