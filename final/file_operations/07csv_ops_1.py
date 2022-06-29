import csv

csv_cols = ["patient_id","firstName","lastName","gender","age","address__streetAddress","address__city","address__state","phoneNumbers__type","phoneNumbers__number"]
def csv_read():
    with open('../resources/patient_data.csv') as csv_file:
        csv_data = csv.reader(csv_file)
        for s in csv_data:
            print(s)

def csv_dict_read():
    patient_list = []
    with open('../resources/patient_data.csv') as csv_file:
        csv_data = csv.DictReader(csv_file)
        for item in csv_data:
            patient_list.append(item)
            # print(item)
        return patient_list

def csv_dict_write():
    plist = csv_dict_read()
    with open('../resources/patient_data_2.csv', 'w') as csv_file:
        csv_data = csv.DictWriter(csv_file, csv_cols)
        csv_data.writeheader()
        for item in plist:
            csv_data.writerow(item)

csv_dict_write()
