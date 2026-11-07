# To-Do List Mini Project

tasks = []

while True:

    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task Added Successfully!")

    # View Task
    elif choice == "2":
        print("\nYour Tasks:")

        if len(tasks) == 0:
            print("No Tasks Found")
        else:
            for i in range(len(tasks)):
                print(i + 1, tasks[i])

    # Delete Task
    elif choice == "3":
        task_no = int(input("Enter task number: "))

        if task_no > 0 and task_no <= len(tasks):
            tasks.pop(task_no - 1)
            print("Task Deleted Successfully!")
        else:
            print("Invalid Task Number!")

    # Exit
    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")