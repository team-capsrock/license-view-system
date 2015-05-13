import pymysql.cursors
import datetime
#test id : test     password : 1234

#user_id='test'
#user_password='1234'



def login(user_id, user_password):
    connection = pymysql.connect(host='localhost',
                             user='root',
                             passwd='1234',
                             db='licenseviewsystem',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = "SELECT password FROM user WHERE id=%s AND password=%s"
            cursor.execute(sql, (user_id, user_password))
            check_password = cursor.fetchone()
            if(check_password==None):
                state = False
            else:
                state = True
    finally:
        connection.close()
    return state



def registration(username, id, password, password2, email, phone):
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
            sql = "SELECT id FROM user WHERE id=%s"
            cursor.execute(sql, (id))
            check_id = cursor.fetchone()
            #print(check_id)
            if(check_id==None):
                if(password!=password2):
                    state = 2 # 2 : password not matched
                else:
                    sql_reg = "INSERT INTO user(id, password, name, phone, email) VALUES(%s, %s, %s, %s, %s)"
                    cursor.execute(sql_reg, (id, password, username, phone, email))
                    state = 0 # 0 : success registration
            else:
                state = 1 # 1 : id is matched
    finally:
        connection.close()
    return state

def view_user_info(username, auth):
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
                             cursorclass=pymysql.cursors.DictCursor,
                             autocommit=True)
    try:
        with connection.cursor() as cursor:
            sql = "SELECT id, name, phone, email FROM user WHERE id=%s"
            cursor.execute(sql, (id))
            check_id = cursor.fetchone()
            user_info = check_id
            print(check_id)
            print(user_info)
    finally:
            connection.close()
    return user_info

def view_user_buy_info(username, auth):
    user_buy_info = {
    'id',
    'pname',
    'period',
    'date',
    }
    connection = pymysql.connect(host='localhost',
                             user='root',
                             passwd='1234',
                             db='licenseviewsystem',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor,
                             autocommit=True)
    try:
        with connection.cursor() as cursor:
            sql = "SELECT id, pname, period, date FROM buy WHERE id=%s"
            cursor.execute(sql, (id))
            check_license = cursor.fetchone()
            user_buy_info = check_license
            print(check_license)
            print(user_buy_info)
    finally:
            connection.close()
    return user_buy_info


def buy(id, pname, type, period):
    connection = pymysql.connect(host='localhost',
                             user='root',
                             passwd='1234',
                             db='licenseviewsystem',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor,
                             autocommit=True)
    try:
        with connection.cursor() as cursor:
            sql = "SELECT id, pname, type FROM buy WHERE (id=%s, pname=%s, type=%s)"
            cursor.execute(sql, (id, pname, type))
            check_license = cursor.fetchone()
            #print(check_id)
            if(check_license==None):
                sql_buy = "UPDATE buy SET period=%d WHERE(id=%s, pname=%s, type=%s)"
                cursor.execute(sql_buy, (period, id, pname, type))
            else
                date = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
                sql_buy = "INSERT INTO buy(id, panme, type, period, date) VALUES(%s, %s, %s, %s, %s)"
                cursor.execute(sql_buy, (id, pname, period, date))

    finally:
        connection.close()
    return


