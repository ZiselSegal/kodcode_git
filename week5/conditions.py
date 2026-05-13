#1
def get_age_settings():
    age = input('please enter an age: ')
    age = number_validation(age)
    if age > 120 or age < 0:
        print('invalid')
    elif age > 0 and age <= 12:
        print('child')
    elif age > 12 and age <= 17:
        print('teen')
    else:
        print('adult')


def number_validation(number):
    while not number or not number.strip('-').isdigit():
        print('invlaid number please try again')
        number  = input('please enter an number: ')
    return float(number)


#2
def check_charecter_data():
    charecter  = input('please enter a single charecter: ')
    charecter = charecter_validation(charecter)
    if charecter.isalpha():
        if charecter in 'aeoui':
            print('vowel')
        else:
            print('consonant')
    else:
        print('invalid')



def charecter_validation(charecter):
    while not charecter or len(charecter) > 1:
        print('invalid input please try again')
        charecter = input('please enter a single charecter: ')
    return charecter


#3
def has_access_check():
    age = input('please enter your age: ')
    age = number_validation(age)
    vip = input('has vip? please enter y/n: ')
    vip = confirmation_validation(vip)
    free_entry_lst = [19,20,21]
    if age in free_entry_lst:
        print('allowed')
    elif age == 18 or age > 21:
        if vip == 'y':
            print('allowed')
        else:
            print('rejected')
    else:
        print('rejected')


def confirmation_validation(vip):
    confirmation = ['n','y']
    while vip not in confirmation:
        print('invalid confirmation please try again')
        vip = input('has vip? please enter y/n: ')
    return vip


#4
def authenticate():
    PASSWORD = 'zisel1234'
    password = input('enter your password: ')
    if password == PASSWORD:
        print('access granted')
    elif len(password) < 8:
        print('too short')
    else:
        print('access denied')


#5
def check_coordinates():
    x = input('enter x coordinates: ')
    x = number_validation(x)
    y = input('enter y coordinates: ')
    y = number_validation(y)
    x_edges = [20,50]
    y_edges = [20,80]
    if 20 < x < 50 and 20 < y < 80:
        print('inside the ractangle')
    elif x in x_edges and y in y_edges or x in x_edges and 20 < y < 80 or y in y_edges and 20 < x < 50:
        print('on the edge')
    else:
        print('outside of ractangle')


#6
def greet_user():
    name = input('enter your name: ')
    print(f'greetings from function: {name or 'anonymus'}')


#7
def sum_positive_nums():
    positive_nums = 0
    for num in range(3):
        num = input('please enter a number: ')
        num = number_validation(num)
        positive_nums += num > 0
    print(f'the number of positive inputs is: {positive_nums}')


#8
def score_evaluation():
    score = input('please enter a score: ')
    score = number_validation(score)
    score = score_validation(score)
    print('A' if score > 89 else 'B' if score > 79 else 'C' if score > 69 else 'F')


def score_validation(score):
    while score > 100 or score < 0:
        print('invalid score please try again')
        score = input('please enter a score: ')
        score = number_validation(score)
    return score