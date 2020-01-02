import pymysql.cursors
from flask import current_app
from app import app


def connection_object():
    with app.app_context():
        return pymysql.connect(host=current_app.config['HOST'],
                               user=current_app.config['USER'],
                               password=current_app.config['PASSWORD'],
                               db=current_app.config['DB'],
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
