import sqlite3_ops

try:
    con = sqlite3.connect(r'dbs\patient_db.db')

    cursor = con.execute("select * from PatientData")
    for row in cursor:
        print(row)
except Exception as e:
    print(e)