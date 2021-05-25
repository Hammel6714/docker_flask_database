import pymysql

db_settings = {
    "host": "172.17.0.1",
    "port": 3306,
    "user": "root",
    "password": "my-password",
    "db": "test1",
    "charset": "utf8"
    }
try:
    # 建立Connection物件
    conn = pymysql.connect(**db_settings)
    
    with conn.cursor() as cursor:
        
        cursor.execute("create table pytable(token char(10))")
        
        conn.commit()

except Exception as ex:
    print(ex)
