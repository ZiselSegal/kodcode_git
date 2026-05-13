from conditions import number_validation

#1
def iterate_over_10():
    for num in range(1,11):
        if num % 2 == 0:
            continue
        elif num == 7:
            break


#2
def guess_password():
    guess = input('enter a password: ')
    password = '1234'
    while guess != password:
        print('wrong guess please try again')
        guess = input('enter a password: ')
    print(f'you guessed correctly! the password is: {guess}')


#3
def get_product_list():
    product_list = []
    product = None
    while product != 'done':
        product = input('please enter a product name or exit by typing done: ')
        if product != 'done':
            product_list.append(product)
    print(' '.join(product_list))


#4
def sum_vowles():
    string = input('please enter a string: ')
    vowles = 'aeoui'
    sum_of_vowels = sum([1 for char in string if char in vowles])
    print(f'the sume of vowels in the string is: {sum_of_vowels}')


#5
def get_5_based_multitable():
    for row in range(1,6):
        for col in range(1,6):
            print(f'{row} * {col} = {row * col}')


#6
def reverse_string():
    string = input('please enter a string: ')
    reversed_string = ''
    for char in string:
        reversed_string = char + reversed_string
    print(f'the reversed string is: {reversed_string}')


#7
def count_even_digits(positive_num):
    sum = 0
    while len(str(positive_num)) > 1:
        digit = positive_num % 10
        if digit % 2 == 0:
            sum += 1
        positive_num //= 10
    print(f'the number of positive digits in the number is: {sum}')


#8
def repeat_string_chars():
    string = input('please enter a string: ')
    repeated_string = ''
    for char in string:
        repeated_string += char * 2
    print(repeated_string)


#9
def get_highest_input():
    number = input('please enter a positive number: ')
    number = number_validation(number)
    highest_num = 0
    while number != 0:
        if number < 0:
            number = input('please enter a positive number: ')
            number = number_validation(number)
        else:
            if number > highest_num:
                highest_num = number
                number = input('please enter a positive number: ')
                number = number_validation(number)
    print(f'the highest input was: {highest_num}')


#10
def check_for_special_chars():
    string = input('please enetr a string: ')
    flag = True
    for char in string:
        if char.isdigit() == False and char.isalpha() == False:
            flag = False
            break
    print(str(flag))


#11
def reverse_number(num):
    reversed_num = 0
    while num:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num //= 10
    print(reversed_num)