import pymysql.cursors




def login(user_id, user_password):
    connection = pymysql.connect(host='localhost',
                             user='root',
                             passwd='1234',
                             db='licenseviewsystem',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = "SELECT password FROM suser WHERE id=%s AND password=%s"
            cursor.execute(sql, (user_id, user_password))
            check_password = cursor.fetchone()
            if(check_password==None):
                state = False
            else:
                state = True
    finally:
        connection.close()
    return state

def view_user_all_info():
    user_info = {
    'id',
    'name',
    'phone',
    'email',
    }
    connection = pymysql.connect(host='localhost',
                             user='root',
                             passwd='1234',
                             db='licenseviewsystem',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = "SELECT id, name, phone, email FROM user"
            cursor.execute(sql, ())
            check_info = cursor.fetchall()
            user_info = check_info
    finally:
        connection.close()
    return user_info

def view_license_all_info():
    license_info = {
    'pname',
    'type',
    'period',
    'price',
    }
    connection = pymysql.connect(host='localhost',
                             user='root',
                             passwd='1234',
                             db='licenseviewsystem',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM license"
            cursor.execute(sql, ())
            check_info = cursor.fetchall()
            license_info = check_info
    finally:
        connection.close()
    return license_info

def view_buy_all_info():
    buy_info = {
    'id',
    'pname',
    'type',
    'period',
    'date',
    }
    connection = pymysql.connect(host='localhost',
                             user='root',
                             passwd='1234',
                             db='licenseviewsystem',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM buy"
            cursor.execute(sql, ())
            check_info = cursor.fetchall()
            buy_info = check_info
    finally:
        connection.close()
    return buy_info

def add_license(pname, type, period, price):
    connection = pymysql.connect(host='localhost',
                             user='root',
                             passwd='1234',
                             db='licenseviewsystem',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor,
                             autocommit=True)
    try:
        with connection.cursor() as cursor:
            #print(id)
            sql = "SELECT pname, type, period FROM license WHERE (pname=%s, type=%s, period=%d)"
            cursor.execute(sql, (id))
            check_id = cursor.fetchone()
            #print(check_id)
            if(check_id==None):
                print('license is overlapped')
            else
                sql_insert = "INSERT INTO license(pname, type, period, price) VALUES(%s, %s, %s, %d)"
    finally:
        connection.close()
    return