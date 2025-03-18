"""
 ===== TO-DO List =====
1. Add task:
2. show task:
3. Mark task as done:
4. Exit:
enter your choice: 1

how many task do you want to add: 2
Enter your task: breakup
task added!
Enter your task: move on
task added!

 ===== TO-DO List =====
1. Add task:
2. show task:
3. Mark task as done:
4. Exit:
enter your choice:

"""

def main():
    task = []

    while True:
        print("\n ===== TO-DO List =====")
        print("1. Add task: ")
        print("2. show task: ")
        print("3. Mark task as done: ")
        print("4. Exit: ")

        choice = input("enter your choice: ")

        if choice == "1":
            print()

            nTasks = int(input("how many task do you want to add: "))


            for i in range(nTasks):
                taskName = input("Enter your task: ")
                task.append({"task": taskName, "done": False})
                print("task added!")


        elif choice == "2":
            print("\nTasks: ")
            for index, t in enumerate(task):
                status = "done" if t["done"] else "Not done"
                print(f"{index +1}. {task['task']} - {status}")


        elif choice == "3":
            taskIndex = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= taskIndex < len(task):
                task[taskIndex]["done"] = True
                print("task marked as done!")

            else:
                print("Invalid task number.")


        elif choice == "4":
            print("Exiting the to do list.")
            break

        else:
            print("Invalid choice. please try again")


if __name__ == "__main__":
    main()