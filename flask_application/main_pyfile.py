from flask import Flask, request, render_template, flash, redirect, url_for, session
from werkzeug import secure_filename
from config import Config
import database as dbf
from flask_login import login_required, LoginManager
import os



app = Flask(__name__)
app.config.from_object(Config)
project_root = os.path.dirname(os.path.abspath(__file__))
mypath = os.path.join(project_root, 'static/image')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = mypath

def allowed_file(filename):
    return '.' in filename and filename.count(".")== 1 and\
           filename.rsplit('.', 1)[-1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        details = request.form
        username = details['username']
        age = details['age']
        gender = details['gender']
        email = details['email']
        password = details['password']
        image = request.files['filename']
        error = None

        if not username:
            error = "Please enter user name"
        elif not age:
            error = "Please enter age"
        elif not gender:
            error = "Please select the gender"
        elif not email:
            error = "please enter email id"
        elif not password:
            error = "please enter password"
        else:
            error = dbf.username_checking(username)

        if image.filename == '':
            error = 'file not selected'
        if image and allowed_file(image.filename):
            image_name = username + '-' + secure_filename(image.filename)
            pname = os.path.join(app.config['UPLOAD_FOLDER'], image_name)
            image.save(pname)
            sname = os.path.join('/static/image', image_name)
        else:
            error = "please enter valid format"

        if error is None:
            dbf.registration(username, age, gender, email, password, sname)
            return render_template('final1.html')
        else:
            flash(error)
            return redirect(url_for('signup'))
    else:
        return render_template('signup.html')

@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        error = None
        details = request.form
        username = details['username']
        password = details['password']
        error = dbf.signin(username, password)
        if error is None:
            session.clear()
            session['user_name'] = username
            return render_template('final2.html')
        else:
            flash(error)
            return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/myaccount')
def myaccount():
    try:
        username = session.get('user_name')
        data = dbf.myaccount(username)
        if data is None:
            raise
        return render_template('account.html', data=data)
    except:
        return "Login Required" + "<a href='http://127.0.0.1:5000/login'>Login</a>"


if __name__ == "__main__":
    app.run(debug=True)
