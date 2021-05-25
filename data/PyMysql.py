#import pymysql

#import charts
# 資料庫設定
def date(token):
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
            add = "INSERT INTO pytable(token) VALUES (%s)"
            up = "UPDATE pytable SET token = '111'"
            sel = "SELECT * FROM pytable"
        
            cursor.execute(add,token)
        
            conn.commit()

    except Exception as ex:
        print(ex)
