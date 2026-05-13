#1
def is_even(n):

    if type(n) != int:
        return print('please pass integer as argument')
    if n % 2 == 0:
        return True
    return False


#2
def  factorial(n):
    factor = 1
    for num in range(1,n+1):
        factor *= num
    return factor

#3
def find_digital_root(num):
    while num > 9:
        num = sum_digits(num)
    return num


def sum_digits(num):
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num //= 10
    return digit_sum


#4
def is_palindrome(s):
    reversed = s[::-1]
    if s == reversed:
        return True
    return False


#5
def count_digits(num):
    digits = 0
    while num > 0:
        num //= 10
        digits += 1
    return digits


#6
def reverse_number(num):
    reversed_num = 0
    sign = 1 if num > 0 else -1
    num = abs(num)
    while num:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num //= 10
    return reversed_num * sign


#7
def push_0_to_last1(arr):
    arr.sort(key=lambda num : num == 0)
    return arr

# without "pythonic functions" 
def push_0_to_last2(arr):
    count_0 = sum([1 for val in arr if val == 0])
    # for val in arr:
    #     if val == 0:
    #         count_0 += 1
    for num in range(count_0):
        arr.remove(0)
        arr.append(0)
    return arr

def push_0_to_last3(arr):
    last_non_zero = 0
    for num in range(len(arr)):
        if arr[num] != 0:
            arr[last_non_zero],arr[num] = arr[num],arr[last_non_zero]
            last_non_zero += 1
    return arr


#8
def get_arr_details(arr):
    print(f'sum: {sum(arr)}')
    print(f'max: {max(arr)}')
    print(f'min: {min(arr)}')
    print(f'average: {sum(arr) / len(arr)}')


#9
def reverse_lst1(arr):
    rot_position = len(arr)
    i = 0
    while i <= len(arr):
        arr.insert(rot_position,arr[0])
        del arr[0]
        rot_position -= 1
        i += 1
    return arr

# more efficient
def reverse_lst2(arr):
    left = 0
    right = len(arr) - 1
    while right > left:
        arr[left],arr[right] = arr[right],arr[left]
        right -= 1
        left += 1
    return arr


#10
def remove_dupes(arr):
    clean_lst = []
    for val in arr:
        if val not in clean_lst:
            clean_lst.append(val)
    return clean_lst

