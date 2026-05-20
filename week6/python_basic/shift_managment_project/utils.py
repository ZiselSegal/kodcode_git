from data import soldiers_data
VALID_STATUSES = {"pending", "completed", "missed"}
VALID_DAYS = {"sunday", "monday", "tuesday", "wednesday", "thursday"}
def get_valid_id() -> int:
    id  = input('please enter id or exit: ')
    while id != 'exit' and not id.isdigit():
        print('invalid id please enter numbers only')
        id  = input('please enter id or exit: ')
    if id == 'exit':
        return
    return int(id)


def get_valid_task_name() -> str:
    task_name  = input('please enter task name or exit: ')
    if task_name == 'exit':
        return
    return task_name


def get_valid_status() -> str:
    status  = input('please enter status or exit: ')
    while status != 'exit' and status not in VALID_STATUSES:
        print(f'invalid status please enter status from the following: {' '.join(VALID_STATUSES)}')
        status  = input('please enter status or exit: ')
    if status == 'exit':
        return
    return status


def get_valid_day() -> str:
    day  = input('please enter day or exit: ')
    while day != 'exit' and day not in VALID_DAYS:
        print('invalid day please enter numbers only')
        day  = input('please enter day or exit: ')
    if day == 'exit':
        return
    return day


def get_valid_name() -> str:
    name  = input('please enter name or exit: ')
    while name != 'exit' and not name.isalpha():
        print('invalid name please enter name cotaining only letters')
        name  = input('please enter name or exit: ')
    if name == 'exit':
        return
    return name


def check_soldier_existence(id:int) -> bool:
    for soldier in soldiers_data:
        if soldier['id'] == id:
            return True
    return False


def check_task_existence(id:int,task_name:str) -> bool:
    for i_soldier, soldier in enumerate(soldiers_data):
        if soldier['id'] == id:
            for i_duty, duty in enumerate(soldier['duties']):
                if duty['name'] == task_name:
                    return i_soldier, i_duty
            return