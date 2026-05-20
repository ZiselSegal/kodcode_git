from data import soldiers_data
from utils import *

def add_solider() -> None:
    name = get_valid_name()
    if not name:
         return print('redirecting to menu...')
    id = get_valid_id()
    if not id:
        return print('redirecting to menu...')
    duties = []
    if name and id:
        soldier = {'name' : name, 'id' : id, 'duties' : duties}
        soldiers_data.append(soldier)

def remove_soldier() -> None:
    id = get_valid_id()
    if not id:
        return print('redirecting to menu...')
    if check_soldier_existence(id):
        for soldier in soldiers_data:
            if soldier['id'] == id:
                soldiers_data.remove(soldier)
    else:
        print('soldier do not exist redirecting you back to menu...')


def show_soldiers_details() -> None:
    counter = 1
    for soldier in soldiers_data:
        print(f'{counter}. name: {soldier['name']}, id: {soldier['id']}\n')
        for duty in soldier['duties']:
            print('   duty: ',end='' )
            print(*(val for val in duty.values()),sep=', ')
            print()
        counter += 1