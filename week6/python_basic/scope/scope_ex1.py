import builtins
#1
counter = 0
def bump():
    global counter
    counter += 1


def value():
    return counter


#2
x = "global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)
    inner()
    print(x)
# outer()
# print(x)

# code will print local enclosing global 


#3
#----------old---------
list = [1, 2, 3]
# print(list(range(5)))
# code will retun type error since in local scope list stand for a list variable and not an oobject/function so you cant call it
#----------fix----------
lst = [1,2,3]
# print(list(range(5)))
#----------fix2---------
lst = [1,2,3]
# print(builtins.list(range(5)))


#4
#--------old-------
def add_item(item, bag=[]):
    bag.append(item)
    return bag
# bug will occur when calling the function multiple times since python tracks list default value by reference and so the default value wont reset itself bewtwwen function calls
#-------fix-----
def add_item(item, bag=None):
    if bag == None:
        bag = []
    bag.append(item)
    return bag
