from functools import reduce
patient_dobs = ['21-02-1981', '03-02-2006', '12-01-1950']
curr_yr = 2022

def get_yob(dob):
    return int(dob.split('-')[2])

patient_yobs = list(map(get_yob, patient_dobs))
print(patient_yobs)

def get_age(yob):
    return curr_yr - yob

patient_ages = list(map(get_age, patient_yobs))
print(patient_ages)

def get_adult_age(age):
    return age >= 18

# nameless or anonymous functions
# also known as lambda functions
# lambda <arguments> : <expression>
status = lambda age: age >= 18
print(status(36))

# adult_patient_ages = list(filter(get_adult_age, patient_ages))
adult_patient_ages = list(filter(lambda age: age >= 18, patient_ages))
print(adult_patient_ages)

# find average age of patient using reduce
# def add(age1, age2):
#     return age1 + age2

avg_patient_age = reduce(lambda age1, age2 : age1 + age2, patient_ages) / len(patient_ages)
print(avg_patient_age)