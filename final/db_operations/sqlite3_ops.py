import sqlite3

def initialize_conn():
    try:
        con = sqlite3.connect(r'D:\temp\webhook_data\patient_db.db')
        return con
    except Exception as e:
        print(e)

def get_data(con):
    cursor = con.execute("select * from PatientData")
    for row in cursor:
        print(row)

def create_patient(con, name, age, address, mobile, status):
    query = f"INSERT INTO PatientData (pName, pAge, pAddress, pMobile, pStatus)" \
            f"values ('{name}', '{age}', '{address}', '{mobile}', '{status}'); "
    # print(query)
    con.execute(query)
    con.commit()

def update_patient(con, pid, age):
    con.execute(f"update PatientData set pAge={age} where pID={pid}")
    con.commit()
    # print(cursor)

def delete_patient(con, pid):
    del_status = 'Active'
    con.execute(f"update PatientData set pStatus='{del_status}' where pID={pid}")
    con.commit()

# connection = initialize_conn()
# get_data(connection)
# create_patient(connection, 'John Doe 2', 50, 'GA', '1234', 'Active')
# get_data(connection)
# # update_patient(connection, 2, 23)
# # get_data(connection)
# # delete_patient(connection, 1)
# # get_data(connection)
