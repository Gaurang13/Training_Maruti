from flask import Flask
from .Resources.data_validation import data_validation #get_data
from .config import configure_app


app = Flask(__name__)
configure_app(app)



@app.route('/<uid>')
def uid_object(uid):
    #get_data(uid)
    data_validation(uid)
    return "ok"

def run_server():
    """Eventlet Server"""
    app.run(port=app.config.get('PORT'))