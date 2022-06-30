import json
import sys
root_dir = sys.path[1]
resource_dir = root_dir+'\\WKPython\\final\\resources'

def patient_generator():
    with open(f'{resource_dir}\\patient_data.json') as json_file:
        json_data = json.load(json_file)
        for patient in json_data["patients_list"]:
            yield patient

# print(patient_generator())
# print(next(patient_generator()))
# print(next(patient_generator()))

for i in patient_generator():
    print(i)
