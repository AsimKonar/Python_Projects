class TaskManager:

    def __init__(self):
        self.tasks = {}

    def _format_status(self, status):
        return 'Completed' if status else 'Pending'

    def add_task(self,name):
        if name in self.tasks:
            return False
        else:
            self.tasks[name] = {'completion':False}
            return True
    def view_task(self,name):
        if name in self.tasks:
            return name.title() + " is " + self._format_status(self.tasks[name]['completion'])
        else:
            return "Task Doesn't Exist"
    def view_all(self):
        l = []
        for key, val in self.tasks.items():
            l.append(key + " is " + self._format_status(val['completion']))
        return l
    def mark_completed(self, name):
        if name in self.tasks:
            self.tasks[name]['completion'] = True
            return True
        else:
            return False
    def delete_task(self,name):
        if name in self.tasks:
            del self.tasks[name]
            return True
        else:
            return False

def main():
    manager = TaskManager()
    while True:
        print("""Options:
                1. Add Task
                2. View one Tasks
                3. View All Tasks
                4. Mark Complete
                5. Delete
                6. Exit""")
        action = input("Choose: ")
        if action == '1': #Add Task
            name = input("Enter the name of the task which needs to be added: ").strip().lower()
            if manager.add_task(name):
                print(f"{name.title()} Marked added successfully")
            else:
                print(f"{name.title()} already exist.")
        elif action == '2': #View one Tasks
            name = input("Enter the name of the task which needs to be views: ").strip().lower()
            print(manager.view_task(name))
        elif action == '3': #View All Tasks
            task = manager.view_all()
            if task:
                for i in task:
                    print(i)
            else:
                print("No Tasks Available.")
        elif action == '4': #Mark Complete
            name = input("Enter the name of the task: ").strip().lower()
            if manager.mark_completed(name):
                print(f"{name.title()} Marked as Completed")
            else:
                print(f"{name.title()} Does not Exist.")
        elif action == '5': #Delete
            name = input("Enter the name of the task which needs to be deleted: ").strip().lower()
            if manager.delete_task(name):
                print(f"{name.title()} Deleted successfully")
            else:
                print(f"{name.title()} does not exist")
        elif action == '6': #exit
            print("Thank You For Using Our app.")
            break
        else:
            print("Please Enter a valid Input.")

main()