import pymysql.cursors

from werkzeug.security import check_password_hash, generate_password_hash
import logging
from flask import current_app


def registration(connection, username, age, gender, email, password, pname):
    try:
        with connection.cursor() as cursor:
            sql = "insert into users(username, age, gender, email, password, img) values(%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (username, age, gender, email, generate_password_hash(password), pname))
            connection.commit()
    except:
        return "username Already exist"


def username_checking(connection, username):
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

def signin(connection, username1, password1):
    try:
        with connection.cursor() as cursor:
            sql = "select username, password, id from users where username = %s "
            cursor.execute(sql, (username1,))
            data= cursor.fetchone()
            error = None
            if data is None:
                error = "incorrect username"
                logging.info("tried with fake user name")
            elif not check_password_hash(data['password'], password1):
                error = "incorrect password"
                logging.warning("tried to enter fake password")

            return error
    finally:
        pass

def myaccount(connection, username):
    try:
        with connection.cursor() as cursor:
            sql = "select * from users where username = %s"
            cursor.execute(sql, (username,))
            data = cursor.fetchone()
            return data
    except:
        pass