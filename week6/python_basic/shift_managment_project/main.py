from soldier_manager import *
from duty_manager import *


def menu() -> None:
    print('choose action form the action below\n')
    print('1.add solider\n' \
          '2.delete solider\n' \
          '3.assign duty\n' \
          '4.update duty status\n' \
          '5.show soldier duties\n' \
          '6.show soldiers details\n' \
          '7.exit\n')
    

def mangae_soldier_duties() -> None:
    while True:
        menu()
        action = input('please enter action number: ')
        match action:
            case '1':
                add_solider()
            case '2':
                remove_soldier()
            case '3':
                add_duty()
            case '4':
                chnage_duty_status()
            case '5':
                show_soldier_duties()
            case '6':
                show_soldiers_details()
            case '7':
                exit()
            case _:
                print('invalid action please try again')

if __name__ == '__main__':
    mangae_soldier_duties()

