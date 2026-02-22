def checker(n):
    return 'Completed' if n else 'Pending'
def add_task(tasks,name):
    if name in tasks:
        print('Present')
    else:
        tasks[name] = {'completion': False}
        print('Task Added Successfully')
def view(task,name):
    if name in task:
        print('1. ' + name+': ' + checker(task[name]['completion']))
    else:
        print('Task Does not present.')
def view_all(task):
    count = 1
    if task:
        for key, value in task.items():
            print(str(count) + '. ' + key + ' : ' + checker(value['completion']))
            count+= 1
    else:
        print("No Tasks is present at the moment.")
def mark_completed(task,name):
    if name in task:
        task[name]['completion'] = True
        print('task masked as Completed')
    else:
        print('Task Does not exist.')
def delete(task,name):
    if name in task:
        del task[name]
        print('Data has been deleted.')
    else:
        print('Task Does not exist.')

def main():
    tasks = {}
    while True:
        print("""Options:
                1. Add Task
                2. View one Tasks
                3. View All Tasks
                4. Mark Complete
                5. Delete
                6. Exit""")
        action = input("Choose: ")
        if action == '1':
            name = input("Enter the name of the task which needs to be added: ").strip()
            add_task(tasks, name)
        elif action == '2':
            name = input("Enter the name of the task which needs to be views: ")
            view(tasks, name)
        elif action == '3':
            # name = input("Enter the name of the task: ")
            view_all(tasks)
        elif action == '4':
            name = input("Enter the name of the task: ")
            mark_completed(tasks, name)
        elif action == '5':
            name = input("Enter the name of the task which needs to be deleted: ")
            delete(tasks, name)
        elif action == '6':
            break
        else:
            print("Please Enter a valid Input.")
        # title = input("Enter the Task Title: ")
    print("Thank you for using our App.")

main()
