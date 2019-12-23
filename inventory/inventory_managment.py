from flask import render_template, request, Flask, Response
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

def output_html(data, code, headers=None):
    resp = Response(data, mimetype='text/html', headers=headers)
    resp.status_code = code
    return resp




api.add_resource(insert_inventory, '/insert')

if __name__ == "__main__":
    app.run(debug=True)