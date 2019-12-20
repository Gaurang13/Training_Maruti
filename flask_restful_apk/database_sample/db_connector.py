import pymysql
from flask import current_app



def connection_object():
    return pymysql.connect(host=current_app.config['HOST'],
                             user=current_app.config['USER'],
                             password=current_app.config['PASSWORD'],
                             db=current_app.config['DB'],
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
