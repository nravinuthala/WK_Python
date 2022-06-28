import csv

csv_cols = ["patient_id","firstName","lastName","gender","age","address__streetAddress","address__city","address__state","phoneNumbers__type","phoneNumbers__number"]
def load_data():
    pdata = {}
    pdata["patients_list"] = []
    with open('resources\patient_data.csv') as csv_file:
        csv_file = csv.DictReader(csv_file)
        for row in csv_file:
            # print(row)
            pdata["patients_list"].append(row)
        return pdata

def update_data(id, name, pdata):
    for patient in pdata["patients_list"]:
        # print(type(patient['patient_id']))
        if patient['patient_id'] == str(id):
            patient["firstName"] = name

def save_data(pdata, cols):
    with open("resources\patient_data_new.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=cols)
        writer.writeheader()
        for data in pdata["patients_list"]:
            writer.writerow(data)

patient_data = load_data()
print(patient_data)
update_data(2, "Jill", patient_data)
print(patient_data)
save_data(patient_data, csv_cols)