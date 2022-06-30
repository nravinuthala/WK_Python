import csv


def get_emp_data():
    with open('emp_list.csv', 'r') as emp_file:
        emp_data = csv.DictReader(emp_file)
        for emp in emp_data:
            yield emp

# for i in get_emp_data():
#     print(i)

#
def process_pension(func):
    for item in func():
        print(f'Dear {item["emp_name"]}, your pension will be credited soon')


@process_pension
def get_pensioners():
    # pemp = {}
    for emp in get_emp_data():
        if int(emp["age"]) >= 60:
            # pemp["emp_name"] = emp["emp_name"]
            # pemp["age"] = emp["age"]
            # yield pemp
            yield emp

# process_pension(get_pensioners)