# command line to-do-list application

class todo_list:


    def __init__(self):
        self.tasks = []
        

    def add_task(self, task_name):
        task = {"task-name": task_name, "completed": False}
        self.tasks.append(task)
        print(f'Task "{task_name}" added.')
        

    def delete_task(self, task_name):
        for task in self.tasks:
            if task["task-name"] == task_name:
                self.tasks.remove(task)
                print(f'Task "{task_name}" deleted.')
                return
        print(f'Task "{task_name}" not found in list.')


    def mark_as_completed(self, task_name):
        for task in self.tasks:
            if task["task-name"] == task_name:
                task["completed"] = True
                print(f'Task "{task_name}" marked as completed.')
                return
        print(f'Task "{task_name}" not found in the list.')

        

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in to-do list.")
        else:
            print("To-Do List:")
            for task in self.tasks:
                status = "Completed" if task["completed"] else "Not Completed"
                print(f'- {task["task-name"]} ({status})')



def main():
    list = todo_list()


    while True:
        print("\n 1. Add Task \n 2. Delete Task \n 3. Mark as Completed \n 4. Display Tasks \n 5. Exit ")
        choice = input("Enter operation to perform b/w (1-5): ")

        if choice == "1":
            task_name = input("Enter task name: ")
            list.add_task(task_name)
        elif choice == "2":
            task_name = input("Enter task name to delete: ")
            list.delete_task(task_name)
        elif choice == "3":
            task_name = input("Enter task name to mark as completed: ")
            list.mark_as_completed(task_name)
        elif choice == "4":
            list.display_tasks()
        elif choice == "5":
            print("Exit completed")
            break
        else:
            print("Invalid Input, Enter number b/w 1 to 5.")


if __name__ == "__main__":
    main()



