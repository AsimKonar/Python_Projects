import json
import os

class TaskManager:
    def __init__(self, file_path = "JSON_files/task_manager.json"):
        self.filename = file_path
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        self.tasks = self.load_data()

    def load_data(self):
        if not os.path.exists(self.filename):
            return {}
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Json File corrupted. Resetting the File.")
            return {}

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self,name, priority):
        if name in self.tasks:
            return False
        else:
            self.tasks[name] = {'completion':False, 'priority':priority}
            self.save_tasks()
            return True
    def view_task(self,name):
        if name in self.tasks:
            return name.title() + " is " + self._format_status(self.tasks[name]['completion']) + " Priority: " + self._format_priority(self.tasks[name]['priority'])
        else:
            return "Task Doesn't Exist"
    def view_all(self):
        l = []
        for key, val in self.tasks.items():
            name = str(key)
            l.append(name.title() + " is " + self._format_status(val['completion']) + " Priority: " + self._format_priority(val['priority']))
        return l
    def mark_completed(self, name):
        if name in self.tasks:
            self.tasks[name]['completion'] = True
            self.save_tasks()
            return True
        else:
            return False
    def delete_task(self,name):
        if name in self.tasks:
            del self.tasks[name]
            self.save_tasks()
            return True
        else:
            return False

    def _format_status(self, status):
        return 'Completed' if status else 'Pending'

    def _format_priority(self, priority):
        if priority == '1':
            return 'High'
        elif priority == '2':
            return 'Moderate'
        else:
            return 'Low'

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
            priority = input("""Choose the priority of the task: 
            1. High
            2. Moderate
            3. Low
            :     """).strip()
            if priority not in (1,2,3):
                print("Please select a valid priority.")
            if manager.add_task(name, priority):
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