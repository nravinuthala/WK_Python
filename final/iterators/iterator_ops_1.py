import json
import sys
root_dir = sys.path[1]
resource_dir = root_dir+'\\WKPython\\final\\resources'

def get_patient_iterator():
    with open(f'{resource_dir}\\patient_data.json') as json_file:
        json_data = json.load(json_file)
        return iter(json_data["patients_list"])

# making print_patients as a higher order fucntion
def print_patients(func):
    p_itr = func()
    while True:
        try:
            print(next(p_itr))
        except StopIteration:
            break

print_patients(get_patient_iterator)


