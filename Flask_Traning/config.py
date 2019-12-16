import os
from flask import Flask

app = Flask(__name__)

class Config(object):

    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY
