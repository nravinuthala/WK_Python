from functools import reduce
list_names = ['Nagaraj', 'Yash', 'Vikram', 'Jayesh']
some_list = [23, 6, 90, 45]

# [23, 6, 90, 45]
# sum(23 + 6) --> 29
# [29, 90, 45]
# sum(29, 90) --> 119
# [119, 45]
# sum(119, 45) --> 164
# 164 returned


def sum(a, b):
    return a + b


# patient_data = {
#     'name': "John",
#     'age': 60,
#     'address': 'Kentucky'
# }

def display_names(name):
    return len(name)

print(list(map(display_names, list_names)))

def short_name(name):
    return len(name) <= 5

print(short_name("Nagaraj"))
print(list(filter(short_name, list_names)))



print(reduce(sum, some_list))






