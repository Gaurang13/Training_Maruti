from flask import Flask, render_template, request
from werkzeug import secure_filename
from config import Config
import os


app = Flask(__name__,template_folder='template')
app.config.from_object(Config)
project_root = os.path.dirname(os.path.abspath(__file__))
mypath = os.path.join(project_root, 'template')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = mypath

def allowed_file(filename):
    return '.' in filename and filename.count(".")== 1 and\
           filename.rsplit('.', 1)[-1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload():
    return render_template('upload.html')

@app.route('/uploader', methods =['POST'])
def uploader():
    file = request.files['filename']
    if file.filename == '':
        return 'file not selected'
    if file and allowed_file(file.filename):
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        return "file uploaded successfully"
    else:
        return "please enter valid format"


if __name__ == '__main__':
    app.run(debug=True)

