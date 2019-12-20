import os
from flask import Flask

app = Flask(__name__)


def configure_app(app):
    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['HOST'] = 'localhost'
    app.config['USER'] = 'root'
    app.config['PASSWORD'] = 'Mtech@12345'
    app.config['DB'] = 'apps'
    app.config['CHARSET'] = 'utf8mb4'
    app.config['CURSORCLASS'] = 'pymysql.cursors.DictCursor'
