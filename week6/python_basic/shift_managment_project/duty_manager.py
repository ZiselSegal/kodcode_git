from utils import *
from data import soldiers_data
from soldier_manager import show_soldiers_details
def add_duty() -> None:
    id = get_valid_id()
    if not id:
        return print('redirecting to menu...')
    task_name = get_valid_task_name()
    if not task_name:
        return print('redirecting to menu...')
    day = get_valid_day()
    if not day:
        return print('redirecting to menu...')
    status = get_valid_status()
    if not status:
        return print('redirecting to menu...')
    task = {'name': task_name, 'day' : day, 'status' : status}
    if id and task_name and day and status:
        exists = check_soldier_existence(id)
        if exists:
            task_exists = check_task_existence(id, task_name)
            if not task_exists:
                for soldier in soldiers_data:
                    if soldier['id'] == id:
                        soldier['duties'].append(task)
    print('redirecting to menu...')


def chnage_duty_status() -> None:
    id = get_valid_id()
    if not id:
        return print('redirecting to menu...')
    task_name = get_valid_task_name()
    if not task_name:
        return print('redirecting to menu...')
    new_status = get_valid_status()
    if not new_status:
        return print('redirecting to menu...')
    if id and task_name and new_status:
        exists = check_soldier_existence(id)
        if exists:
            task_exists = check_task_existence(id, task_name)
            if task_exists:
                global soldiers_data
                soldiers_data[task_exists[0]]['duties'][task_exists[1]]['status'] = new_status
    print('redirecting to menu....')


def show_soldier_duties() -> None:
    id = get_valid_id()
    if not id:
        return print('redirecting to menu...')
    if id:
        for soldier in soldiers_data:
            if id == soldier['id']:
                print(f'name: {soldier['name']}, id: {soldier['id']}')
                for duty in soldier['duties']:
                    print('   duty: ',end='' )
                    print(*(val for val in duty.values()),sep=', ')
    else:
        print('reirecting to menu...')





