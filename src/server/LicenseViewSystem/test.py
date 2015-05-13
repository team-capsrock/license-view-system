import pymysql.cursors

id = 'test'
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
        sql = "SELECT id, name, phone, email FROM user"
        #sql = "SELELCT id, name, phone, email FROM user WHERE id=%s"
        cursor.execute(sql, ())
        check_id = cursor.fetchall()
        user_info = check_id
        #print(check_id)

finally:
        connection.close()