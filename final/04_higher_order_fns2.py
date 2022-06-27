patient_dobs = ['21-02-1981', '03-02-2006', '12-01-1950']
curr_yr = 2022

def get_yob(dobs):
    yobs = []
    for dob in dobs:
        yobs.append(int(dob.split('-')[2]))
    return yobs

def get_ages(yobs):
    ages = []
    for yr in yobs:
        ages.append(curr_yr - yr)
    return ages

def get_patient_status(get_yob, get_ages, dobs):
    is_major = []
    # yobs = get_yob(dobs)
    ages = get_ages(get_yob(dobs))
    for age in ages:
        if age >= 18:
            is_major.append(age)
    return is_major

print(get_patient_status(get_yob, get_ages, patient_dobs))
