from flask import Flask, render_template, request
from werkzeug import secure_filename
from config import Config
import os

app = Flask(__name__,template_folder='template')
app.config.from_object(Config)
upload_path = '/home/mtech/PycharmProjects/tmp/Flask_Traning/template'
app.config['UPLOAD_FOLDER'] = upload_path

@app.route('/')
def upload():
    return render_template('upload.html')

@app.route('/uploader', methods =['POST'])
def uploader():
    file = request.files['file']
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
    return "file uploaded successfully"


if __name__ == '__main__':
    app.run(debug=True)
