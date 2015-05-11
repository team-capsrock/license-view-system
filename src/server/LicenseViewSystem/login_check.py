import pymysql.cursors

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