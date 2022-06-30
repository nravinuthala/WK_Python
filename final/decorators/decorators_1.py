import csv

def get_emp_data():
    with open('emp_list.csv', 'r') as emp_file:
        emp_data = csv.DictReader(emp_file)
        for emp in emp_data:
            # print(emp)
            yield emp
        # return emp_data

def get_pensioners(edata):
    pemp = {}
    if int(edata["age"]) >= 60:
        pemp["emp_name"] = edata["emp_name"]
        pemp["age"] = edata["age"]
        yield pemp

def process_pension(get_data, process_data):
    # data = get_data()
    all_employees = {"employees": []}
    all_pensioners = {"pensioners": []}
    all_pensioners = {"pensioners": []}
    for item in get_data():
        # print(item)
        all_employees["employees"].append(item)
        for pensioner in process_data(item):
            # print(pensioner)
            all_pensioners["pensioners"].append(pensioner)
    print("All empoyees:")
    print(all_employees)
    print("All pensioners:")
    print(all_pensioners)

# process_pension(get_emp_data, get_pensioners)