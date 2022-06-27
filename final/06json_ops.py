import json

with open('resources\patient_data.json') as patient_data_file:
    pdata = patient_data_file.read()

print(pdata)