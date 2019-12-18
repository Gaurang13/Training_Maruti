import pymysql.cursors
from werkzeug.security import check_password_hash, generate_password_hash

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Mtech@12345',
                             db='apps',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def registration(username, age, gender, email, password, pname):
    try:
        with connection.cursor() as cursor:
            sql = "insert into users(username, age, gender, email, password, img) values(%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (username, age, gender, email, generate_password_hash(password), pname))
            connection.commit()
    finally:
        pass

def username_checking(username):
    try:

        with connection.cursor() as cursor:
            sql = "select id from users where username = %s"
            cursor.execute(sql, (username,))
            data = cursor.fetchone()
            error = None
            print(data)
            if data is not None:
                error = "username {} Already exist".format(username)
                return error
            else:
                pass
    finally:
        pass

def signin(username1, password1):
    try:
        with connection.cursor() as cursor:
            sql = "select username, password, id from users where username = %s "
            cursor.execute(sql, (username1,))
            data= cursor.fetchone()
            error = None
            if data is None:
                error = "incorrect username"
            elif not check_password_hash(data['password'], password1):
                error = "incorrect password"

            return error
    finally:
        pass

def myaccount(username):
    try:
        with connection.cursor() as cursor:
            sql = "select * from users where username = %s"
            cursor.execute(sql, (username,))
            data = cursor.fetchone()
            return data
    finally:
        pass