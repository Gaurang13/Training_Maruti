from flask import Flask, render_template
from flask_restful import Api
from Resources.Insert_I import insert_inventory
from Resources.search import item_search
from Resources.item_update import update_item
from Resources.i_delete import delete_item
from flask_swagger_ui import get_swaggerui_blueprint
from config import Config
import logging
logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

app = Flask(__name__)
api = Api(app)


SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


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