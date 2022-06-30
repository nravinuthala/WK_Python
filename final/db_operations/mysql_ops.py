import pymysql.cursors

conn = pymysql.connect(host='localhost',
                user='root',
                password='root@123',
                database='sakila',
                cursorclass=pymysql.cursors.DictCursor)

# print(conn)

with conn:
    with conn.cursor() as cursor:
        sql = "select * from actor"
        cursor.execute(sql)
        result = cursor.fetchall()
    print(result)