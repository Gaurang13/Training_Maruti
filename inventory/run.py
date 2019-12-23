from flask import Flask
from flask_restful import Api
from Resources.Insert_I import insert_inventory
from Resources.search import search
from config import Config, Db_Config
import logging
#logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

app = Flask(__name__)
api = Api(app)

app.config.from_object(Config)
api.add_resource(insert_inventory, '/insert')
api.add_resource(search, '/search')

if __name__ == "__main__":
    app.run(debug=True)