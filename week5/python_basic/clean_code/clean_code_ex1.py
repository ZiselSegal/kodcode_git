def task_manegment():
    tasks = []
    while True:
        menu()
        action = input('please enter action number: ')
        match action:
            case '1':
                tasks.append(create_task())
            case '2':
                number_of_tasks = get_valid_int()
                for times in range(number_of_tasks):
                    tasks.append(create_task())
            case '3':
                print('\n')
                show_task_data(tasks)
            case '4':
                print('\n')
                show_tasks_data(tasks)
            case '5':
                active_tasks_count = count_active_tasks(tasks)
                print(f'\ncurrent active tasks: {active_tasks_count}\n')
            case '6':
                completed_tasks_count = count_completed_tasks(tasks)
                print(f'\ncurrent completed tasks: {completed_tasks_count}\n')
            case '7':
                urget_tasks_count = count_urgent_tasks(tasks)
                print(f'\ncurrent urgent tasks: {urget_tasks_count}\n')
            case '8':
                task_count, active_count, completed_count, urgent_count = get_daily_report(tasks)
                print(f'\n tasks today: {task_count}\n active tasks: {active_count}\n completed tasks: {completed_count}\n urgent tasks: {urgent_count}\n')
            case '9':
                exit()
            case _:
                print('invalid action please try again')


def get_valid_int():
    number_of_tasks = input('enter number of tasks you want to create: ')
    while not number_of_tasks or not number_of_tasks.isdigit():
        print('error please enter a number')
        number_of_tasks = input('enter number of tasks you want to create: ')
    return int(number_of_tasks)


def create_task():
    task_name = input('please enter task name: ')
    task_status = input('please enter task status:  ')
    priority_level = input('please enter task priority level: ')
    task = {'task name' : task_name, 'task status' : task_status, 'priority level' : priority_level}
    return task


def show_task_data(tasks):
    task_name = input('please enter task name: ')
    for task in tasks:
        try:
            if task['task name'] == task_name:
                for key,val in task.items():
                    print(key, val)
            print('\n')
            return
        except KeyError:
            continue
    print(f'no task matches this name: {task_name}')


def count_active_tasks(tasks):
    active_tasks_count = 0
    for task in tasks:
        if task['task status'] != 'done':
            active_tasks_count += 1
    if active_tasks_count:
        return active_tasks_count
    return 'no active tasks available\n'

def count_completed_tasks(tasks):
    completed_tasks_count = 0
    for task in tasks:
        if task['task status'] == 'done':
            completed_tasks_count += 1
    if completed_tasks_count:
        return completed_tasks_count
    return 'no completed tasks available\n'

def count_urgent_tasks(tasks):
    urgent_tasks_count = 0
    for task in tasks:
        if task['priority level'] == 'urgent' and task['task status'] != 'done':
            urgent_tasks_count += 1
    if urgent_tasks_count:
        return urgent_tasks_count
    return 'no urgent tasks avilable\n'

def show_tasks_data(tasks):
    if not tasks:
        return print('\nno tasks found please use create task feature to create tasks\n')
    for task in tasks:
        for key,val in task.items():
            print(key, val, '\n')


def get_daily_report(tasks):
    task_count = len(tasks)
    active_count = count_active_tasks(tasks)
    completed_count = count_completed_tasks(tasks)
    urgent_count = count_urgent_tasks(tasks)
    return task_count, active_count, completed_count, urgent_count




def menu():
    print('choose action from the actions below \n \n' \
    '1.add task \n' \
    '2.add multiple tasks \n' \
    '3.see task data \n' \
    '4.see all tasks data \n' \
    '5.see number of unfinished taks\n' \
    '6.see number of completed tasks\n' \
    '7.see number of urgent tasks\n' \
    '8.see full daily report\n' \
    '9.exit')

task_manegment()