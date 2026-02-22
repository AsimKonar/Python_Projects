def checker(n):
    if n:
        return 'Completed'
    else:
        return 'Pending'
def create(tasks,n):
    x = ([i for i in tasks if i['task'] == n])
    if x:
        print("Task Already exist.")
    else:
        tasks.append({'task': n,'completion':False})
        print('Task Added Successfully')
def view(tasks,n):
    x = ([i for i in tasks if i['task'] == n])
    if not x:
        print("Task Doesn't Exist.")
    else:
        print(x[0]['task'] + ' ' + checker(x[0]['completion']))
def delete(tasks,n):
    try:
        index = [i for i, j in enumerate(tasks) if j['task'] == n]
        del tasks[index[0]]
        print('Task Deleted Successfully')
    except IndexError:
        print("Task not present.")
def mark_completed(tasks,n):
    try:
        index = [i for i, j in enumerate(tasks) if j['task'] == n]
        tasks[index[0]]['completion'] = True
        print('Task Updated Successfully')
    except ValueError:
        print("Task not present.")
def view_all(tasks):
    for i, j in enumerate(tasks):
        print(str(i + 1) + '. ' + j['task'] + ' ' + checker(j['completion']))
def main():
    tasks = []
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
            name = input("Enter the name of the task which needs to be added: ")
            create(tasks,name)
        elif action == '2':
            name = input("Enter the name of the task which needs to be views: ")
            view(tasks,name)
        elif action == '3':
            # name = input("Enter the name of the task: ")
            view_all(tasks)
        elif action == '4':
            name = input("Enter the name of the task: ")
            mark_completed(tasks,name)
        elif action == '5':
            name = input("Enter the name of the task which needs to be deleted: ")
            delete(tasks,name)
        elif action == '6':
            break
        else:
            print("Please Enter a valid Input.")
        # title = input("Enter the Task Title: ")
    print("Thank you for using our App.")

main()