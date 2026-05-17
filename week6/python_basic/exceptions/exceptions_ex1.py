#1
def safe_int(s):
    try:
        s = int(s)
        return s
    except Exception as e:
        print(e)
        return None


#2
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'undefined'


#3
def get_value(d, key):
    try:
        return d[key]
    except KeyError:
        return 'missing'


#4
def parse_ints(values):
    parsed_lst = []
    for val in values:
        try:
            int_val = int(val)
            parsed_lst.append(int_val)
        except ValueError:
            continue
    return parsed_lst


#5
def set_age(age):
    if age > 150 or age < 0:
        raise ValueError('age outside defined values')
    return age


#6
def retry(func, n):
    error_count = 0
    for times in range(n):
        try:
            fun_result = func(-1)
            print(fun_result)
            return
        except Exception:
            error_count += 1
            if error_count == n:
                raise


#6.2
def retry_v2(func,n):
    exception = None
    for times in range(n):
        try:
            return print(func())
        except Exception as e:
            exception = e
    raise exception


#7
def count_errors(funcs):
    error_count = 0
    for func in funcs:
        try:
            func()
        except Exception:
            error_count += 1
    return error_count