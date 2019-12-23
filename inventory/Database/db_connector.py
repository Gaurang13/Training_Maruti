import pymysql.cursors
from flask import current_app
from config import Db_Config

def connection_object():
    current_app.config.from_object(Db_Config())
    return pymysql.connect(host=current_app.config['HOST'],
                                 user=current_app.config['USER'],
                                 password=current_app.config['PASSWORD'],
                                 db=current_app.config['DB'],
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
