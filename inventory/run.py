from flask import Flask, render_template
from flask_restful import Api
from Resources.Insert_I import insert_inventory
from Resources.search import item_search
from Resources.item_update import update_item
from Resources.i_delete import delete_item
from config import Config
import logging
logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

app = Flask(__name__)
api = Api(app)

app.config.from_object(Config)
api.add_resource(insert_inventory, '/insert')
api.add_resource(item_search, '/search')
api.add_resource(update_item, '/update')
api.add_resource(delete_item, '/delete')
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)