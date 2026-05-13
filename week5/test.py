from math import inf

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
def count_vowels(s):
    vowels = 0
    for char in s:
        if char in 'aeoui':
            vowels += 1
    return vowels


#4
def reverse_string(s):
    return s[::-1]


#5
def find_max(lst):
    max_num  = lst[0]
    for num in lst:
        if type(num) == int:
            if num > max_num:
                max_num = num
    return max_num


#6
def celsius_to_fahrenheit(c):
    return (c * 1.8) + 32


#7
def is_palindrome(s):
    reversed = s[::-1]
    if s == reversed:
        return True
    return False


#8
def sort_even_lst(lst):
    sorted_lst = filter(lambda num : num % 2 == 0,lst)
    return list(sorted_lst)


#9
def check_anagram(s1,s2):
    s1 = ''.join(sorted(s1.lower()))
    s2 = ''.join(sorted(s2.lower()))
    return s1 == s2


#10
def word_count_dict(sentence):
    count_dict = {}
    for word in sentence.split():
        count_dict[word] = count_dict.get(word,0) + 1
    return count_dict


def push_0(arr):
    for val in arr:
        if val == 0:
            arr.remove(0)
            arr.append(0)
    return arr



# argyment passing exrocise

def f1(arg1,/,arg2,arg3):
    print(f'arg1: {arg1}, arg2: {arg2}, arg3: {arg3}')

def f2(*args):
    print(f'args: {args}')

def f3(arg1,/,*,arg2):
    print(f'arg1: {arg1}, arg2: {arg2}')


# while False or True and not not not False and 7 ^ 6 or 1 ^ 2 and set(tuple(list(str(float(int(min(max(sum(len(-inf) / 8))))))))) \
#     ** inf / 2 and True if __name__ == __name__ \
#     else not False and 8 if True else 5 if not False else 9 and not not boo([ivx for ivx in range(812)] + [jfk for jfk in len(((1,5,6,4,3)))]\
#      + {xbd:dbx for xdb,dbx in {1:1,2:2,3:3}.items()}):
#     print(1)

a = 'a'
print(len(a))