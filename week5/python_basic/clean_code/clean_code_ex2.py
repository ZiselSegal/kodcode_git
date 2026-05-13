#1
def f(l):
    r = []
    for x in l:
        if x[1] >= 18 and x[2] == "active":
            r.append(x[0])
    return r

d = [
    ["Dan", 25, "active"],
    ["Noa", 16, "active"],
    ["Yael", 30, "inactive"],
]

# print(f(d))




def filter_active_adults(list):
    active_adults = []
    for val in list:
        if val[1] >= 18 and val[2] == "active":
            active_adults.append(val[0])
    return active_adults

users_data = [
    ["Dan", 25, "is_active"],
    ["Noa", 16, "is_active"],
    ["Yael", 30, "inactive"],
]

# print(filter_active_adults(users_data))

#2 -------------- old -----------------
def handle_purchase(user_email, product_name, product_price, stock, quantity):
    if not user_email:
        print("Invalid user")
        return None
    if quantity <= 0 or quantity > stock:
        print("Invalid quantity")
        return None

    price = product_price * quantity
    if quantity >= 10:
        price *= 0.9
    if quantity >= 50:
        price *= 0.85

    stock -= quantity

    order_user = user_email
    order_product = product_name
    order_quantity = quantity
    order_total = price
    order_status = "confirmed"
    print(f"Order {order_status}: {order_user} bought {order_quantity}x {order_product} for ${order_total}")
    return order_user, order_product, order_quantity, order_total, order_status



 #-----------new-----------
def calculate_price(product_price,quantity):
    price = product_price * quantity
    if quantity >= 10:
        price *= 0.9
    if quantity >= 50:
        price *= 0.85
    return price

def validate_order_details(quantity,stock,user_email):
    if not user_email:
        print("Invalid user")
        return None
    if quantity <= 0 or quantity > stock:
        print("Invalid quantity")
        return None
    

def handle_purchase(user_email, product_name, product_price, stock, quantity):
    price = calculate_price(product_price,quantity)

    stock -= quantity

    order_user = user_email
    order_product = product_name
    order_quantity = quantity
    order_total = price
    order_status = "confirmed"
    print(f"Order {order_status}: {order_user} bought {order_quantity}x {order_product} for ${order_total}")
    return order_user, order_product, order_quantity, order_total, order_status



#3
# ---------------- old -------------------------
def manage_students(names, grades, new_name, new_grade):
    # validation
    if not new_name or len(new_name) < 2:
        print("Error: invalid name")
        return students
    if new_grade < 0 or new_grade > 100:
        print("Error: grade must be 0-100")
        return students

    # add student
    grades.append(new_grade)

    # calculate stats
    total = sum(grades)
    average = total / len(grades)
    top_count = sum(1 for g in grades if g >= 90)
    failing_count = sum(1 for g in grades if g < 56)

    # print report
    print("=== Student Report ===")
    for i in range(len(names)):
        print(f"  {names[i]}: {grades[i]}")
    print(f"Average: {average:.1f}")
    print(f"Top students: {top_count}")
    print(f"Failing: {failing_count}")

    # save to file
    with open("students.txt", "w") as f:
        for i in range(len(names)):
            f.write(f"{names[i]},{grades[i]}\n")

#------------------new----------------

def validate_score_details(students,new_name,new_grade):
    if not new_name or len(new_name) < 2:
        print("Error: invalid name")
        return students
    if new_grade < 0 or new_grade > 100:
        print("Error: grade must be 0-100")
        return students
    
def add_student(students, grades, new_name, new_grade):
    grades.append(new_grade)
    students.append(new_name)
    return


def calculate_values(grades):
    total = sum(grades)
    average = total / len(grades)
    top_count = sum(1 for g in grades if g >= 90)
    failing_count = sum(1 for g in grades if g < 56)
    print("=== Student Report ===")
    return average, top_count, failing_count


def save_to_file(students,grades):
    with open("students.txt", "w") as f:
        for i in range(len(students)):
            f.write(f"{students[i]},{grades[i]}\n")

def print_data(students,grades,average,top_count,failing_count):
    for i in range(len(students)):
        print(f"  {students[i]}: {grades[i]}")
        print(f"Average: {average:.1f}")
        print(f"Top students: {top_count}")
        print(f"Failing: {failing_count}")


def get_student_report(students, grades, new_name, new_grade):
    validation = validate_score_details(students,new_name,new_grade)
    if validation == students:
        return
    else:
        add_student()
        average, top_count, failing_count = calculate_values
        print_data(students,grades,average,top_count,failing_count)
        save_to_file(students,grades)



#---------------------old------------------------

def create_admin_user(name, email):
    if not name or len(name) < 2:
        raise ValueError("Invalid name")
    if "@" not in email:
        raise ValueError("Invalid email")
    return name, email, "admin", "2024-01-01", True
    

def create_editor_user(name, email):
    if not name or len(name) < 2:
        raise ValueError("Invalid name")
    if "@" not in email:
        raise ValueError("Invalid email")
    return name, email, "editor", "2024-01-01", True
    

def create_viewer_user(name, email):
    if not name or len(name) < 2:
        raise ValueError("Invalid name")
    if "@" not in email:
        raise ValueError("Invalid email")
    return name, email, "viewer", "2024-01-01", True


#-----------new-----------

def create_user(username,email):
    validate_user(username,email)
    return username, email, "viewer", "2024-01-01", True

def validate_user(username,email):
    if not username or len(username) < 2:
        raise ValueError("Invalid name")
    if "@" not in email:
        raise ValueError("Invalid email")
    

#5
#---------------old--------------

def get_status(score):
    if score >= 90:
        status = "excellent"
    elif score >= 70 and score < 90:
        status = "good"
    elif score >= 55 and score < 70:
        status = "average"
    elif score < 55:
        status = "fail"
    else:
        status = "unknown"
    return status


def is_valid_age(age):
    if isinstance(age, int):
        if age > 0:
            if age < 120:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def get_greeting(hour):
    greeting = ''
    if hour >= 5 and hour < 12:
        greeting = "Good morning"
    if hour >= 12 and hour < 17:
        greeting = "Good afternoon"
    if hour >= 17 and hour < 21:
        greeting = "Good evening"
    if hour >= 21 or hour < 5:
        greeting = "Good night"
    return greeting

#----------new------------

def get_status(score):
    if score >= 90 and score <= 100:
        return "excellent"
    elif score >= 70:
        return "good"
    elif score >= 55:
        return "average"
    elif score >= 0:
        return "fail"
    else:
        return "unknown"


def is_valid_age(age):
    if isinstance(age, int):
        if 120 > age > 0:
            return True
    return False


def get_greeting(hour):
    if hour >= 5 and hour < 12:
        return "Good morning"
    elif hour >= 12 and hour < 17:
        return "Good afternoon"
    elif hour >= 17 and hour < 21:
        return "Good evening"
    else:
        return "Good night"
    

#6
#-------------old--------------

def process_grades(names, all_grades):
    result_names = []
    result_averages = []
    result_statuses = []
    result_highs = []
    result_lows = []
    for i in range(len(names)):
        name = names[i]
        grades = all_grades[i]

        if not name:
            print(f"Error: missing name")
            continue
        if not grades:
            print(f"Error: {name} has no grades")
            continue

        total = sum(grades)
        average = total / len(grades)
        status = "pass" if average >= 56 else "fail"
        highest = max(grades)
        lowest = min(grades)

        result_names.append(name)
        result_averages.append(round(average, 1))
        result_statuses.append(status)
        result_highs.append(highest)
        result_lows.append(lowest)
    
    
    print("=" * 40)
    print("Student Grade Report")
    print("=" * 40)
    for i in range(len(result_names)):
        print(f"Name: {result_names[i]}")
        print(f"  Average: {result_averages[i]}")
        print(f"  Status: {result_statuses[i]}")
        print(f"  Range: {result_lows[i]} - {result_highs[i]}")
        print()

    passing_count = sum(1 for s in result_statuses if s == "pass")
    print(f"Total passing: {passing_count}/{len(result_names)}")
    return result_names, result_averages, result_statuses


#-----------------------------new-----------------------

def validate_student(name,grades):
        if not name:
            return print(f"Error: missing name")
        if not grades:
            return print(f"Error: {name} has no grades")
        

def calculate_student_stats(grades):
        total = sum(grades)
        average = total / len(grades)
        status = "pass" if average >= 56 else "fail"
        highest = max(grades)
        lowest = min(grades)
        return average,status,highest,lowest


def print_report(result_names, result_averages,result_lows ,result_statuses,result_highs):
    print("=" * 40)
    print("Student Grade Report")
    print("=" * 40)
    for i in range(len(result_names)):
        print(f"Name: {result_names[i]}")
        print(f"  Average: {result_averages[i]}")
        print(f"  Status: {result_statuses[i]}")
        print(f"  Range: {result_lows[i]} - {result_highs[i]}")

    passing_count = sum(1 for s in result_statuses if s == "pass")
    print(f"Total passing: {passing_count}/{len(result_names)}")



def get_student_grade_report(names,all_grades):
    result_names = []
    result_averages = []
    result_statuses = []
    result_highs = []
    result_lows = []
    for i in range(len(names)):
        name = names[i]
        grades = all_grades[i]
        if validate_student(name,grades):
            average,status,highest,lowest = calculate_student_stats(grades)
            result_names.append(name)
            result_averages.append(round(average, 1))
            result_statuses.append(status)
            result_highs.append(highest)
            result_lows.append(lowest)
    print_report(result_names, result_averages,result_lows ,result_statuses,result_highs)
    return result_names, result_averages, result_statuses



#7
#--------------------old--------------------

TAX = 0.17
def ProcessCart(prices,quantities,UserType):
  t=0
  for i in range(len(prices)):
    p=prices[i]
    q=quantities[i]
    t=t+p*q
  # add tax
  t = t + t * TAX
  if UserType=='premium':
    t=t*0.9
  elif UserType=='vip':
    t = t * 0.8
  if t>500:
    shipping=0
  elif t > 200:
    shipping = 25
  else:
    shipping=50
  t=t+shipping
  return t

#-------------------new-------------------

def process_payment(prices,quantities,user_status):
    price = calculate_price(prices,quantities)
    price_after_discount = apply_super_user_discount(price,user_status)
    final_price = add_shipping_price(price_after_discount)
    return final_price
    


def calculate_price(prices,quantities):
    TAX = 0.17
    untaxed_final_price = 0
    purchases = len(prices)
    for current_purchase in range(purchases):
        price = prices[current_purchase]
        quantity = quantities[current_purchase]
        untaxed_final_price += price * quantity
    final_price += final_price * TAX
    return final_price

def apply_super_user_discount(final_price,user_status):
    premium_discount = 0.9
    VIP_discount = 0.8
    if user_status == 'premium':
        final_price *= premium_discount
    elif user_status == 'VIP':
        final_price *= VIP_discount
    return final_price

def add_shipping_price(final_price):
    shipping = 0
    if 200 < final_price < 500:
        shipping = 25
    elif final_price < 200:
        shipping = 50
    final_price += shipping
    return final_price
        

    


