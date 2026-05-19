from datetime import datetime as dt
import geometry

def counter_factory(num):
    def counter():
        nonlocal num
        num += 1
        return num
    return counter


def get_datetime():
    return dt.now()


def get_regular_namespaces(module):
    public_names = [name for name in dir(module) if not name.startswith('_')]
    return public_names

print(geometry.circle.area(5))
print(geometry.rectangle.area(4, 6))