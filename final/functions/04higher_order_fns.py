# functions as objects

def add(a, b):
    return a + b


plus = add

print(plus(2, 3))

# passing functions as arguments
def total(list_of_num):
    return sum(list_of_num, 0)

def divide(num1, num2):
    return num1 / num2

marks = [23, 56, 89, 45, 78]
avg = divide(291, 5)
# print(total(marks))
# print(avg)

def avg(mysum, mydiv, list_of_values):
    return mydiv(mysum(list_of_values), len(list_of_values))

print(avg(total, divide, marks))


# returning functions from other functions and lambda functions
def get_marks_and_avg_fn():
    marks = [34, 56, 78, 90, 54]
    return marks, lambda marks: sum(marks)/ len(marks)

marks_list, avg_fn = get_marks_and_avg_fn()
print(avg_fn(marks_list))
