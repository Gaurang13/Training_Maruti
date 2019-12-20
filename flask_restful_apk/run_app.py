from flask import Flask
from flask_restful import Api
from flask_restful_apk.config.config import Config
from flask_restful_apk.main_pyfile import *


app = Flask(__name__)
api = Api(app)
app.config.from_object(Config)
api.add_resource(index, '/')
api.add_resource(signup, '/signup')
api.add_resource(logout, '/logout')
api.add_resource(myaacount,'/myaccount')
api.add_resource(login, '/login')

if __name__ == "__main__":
    app.run(debug=True)