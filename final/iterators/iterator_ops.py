import json
import sys
root_dir = sys.path[1]
resource_dir = root_dir+'\\WKPython\\final\\resources'

# with open(f'{resource_dir}\\patient_data.json') as json_file:
#     json_data = json.load(json_file)
#     p_iterable = json_data["patients_list"]
#     p_itr = iter(p_iterable)
#     print(p_itr)
#
# while True:
#     try:
#         print(next(p_itr))
#     except StopIteration:
#         print("Finished printing all patient records.")
#         break



def get_patient_iterator():
    with open(f'{resource_dir}\\patient_data.json') as json_file:
        json_data = json.load(json_file)
        return iter(json_data["patients_list"])

def print_patients(p_itr):
    while True:
        try:
            print(next(p_itr))
        except StopIteration:
            break

print_patients(get_patient_iterator())


