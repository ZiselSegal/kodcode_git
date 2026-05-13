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


def show_tasks_data(tasks):
    for task in tasks:
        for key,val in task.items():
            print(key, val)
        print('\n')


def menu():
    print('choose action from the actions below \n \n' \
    '1.add task \n' \
    '2.add multiple tasks \n' \
    '3.see task data \n' \
    '4.see all tasks data \n' \
    '5.exit')