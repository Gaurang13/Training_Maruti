import os
from flask import Response, current_app
def output_html(data, code, headers=None):
    resp = Response(data, mimetype='text/html', headers=headers)
    resp.status_code = code
    return resp


project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
mypath = os.path.join(project_root, 'static/image')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.count(".") == 1 and \
           filename.rsplit('.', 1)[-1].lower() in ALLOWED_EXTENSIONS


