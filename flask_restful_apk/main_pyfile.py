from flask import Flask, request, render_template, flash, redirect, url_for, session, Response
from flask_restful import  Resource, Api
from werkzeug import secure_filename
from flask_restful_apk.config.config import configure_app
from flask_restful_apk.database_sample.db_connector import connection_object
import flask_restful_apk.database_sample.database_sample as dbf
import os
import logging
import pymysql
from flask import current_app

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

connection = connection_object
app = Flask(__name__)
api = Api(app)
configure_app(app)

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')




project_root = os.path.dirname(os.path.abspath(__file__))
mypath = os.path.join(project_root, 'static/image')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = mypath


def allowed_file(filename):
    return '.' in filename and filename.count(".") == 1 and \
           filename.rsplit('.', 1)[-1].lower() in ALLOWED_EXTENSIONS


def output_html(data, code, headers=None):
    resp = Response(data, mimetype='text/html', headers=headers)
    resp.status_code = code
    return resp

class index(Resource):
    def get(self):
        return output_html(render_template('/index.html'),200)




class signup(Resource):
    def post(self):
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
        elif image.filename == '':
            error = 'file not selected'
        elif image and allowed_file(image.filename):
            image_name = username + '-' + secure_filename(image.filename)
            pname = os.path.join(app.config['UPLOAD_FOLDER'], image_name)
            image.save(pname)
            sname = os.path.join('/static/image', image_name)
        else:
            error = "please enter valid format"

        if error is None:
            al_error = dbf.registration(connection, username, age, gender, email, password, sname)
            if al_error is None:
                return output_html(render_template('final1.html'),200)
            else:
                flash(al_error)
                return redirect(url_for('signup'))
        else:
            flash(error)
            return redirect(url_for('signup'))

    def get(self):
        return output_html(render_template('signup.html'), 200)



class login(Resource):
    def post(self):
        error = None
        details = request.form
        username = details['username']
        password = details['password']
        error = dbf.signin(connection, username, password)
        if error is None:
            session.clear()
            session['user_name'] = username
            return output_html(render_template('final2.html'), 200)
        else:
            flash(error)
            return output_html(render_template('login.html'), 200)
    def get(self):
        return output_html(render_template('login.html'), 200)




class logout(Resource):
    def get(self):
        session.clear()
        return redirect(url_for('index'))





class myaacount(Resource):
    def get(self):
        try:
            username = session.get('user_name')
            data = dbf.myaccount(connection, username)
            if data is None:
                raise
            return output_html(render_template('account.html', data=data), 200)
        except:
            logging.warning("try to access page directly")
            return output_html(("Login Required" + "<a href='http://127.0.0.1:5000/login'>Login</a>"), 200)

api.add_resource(index, '/')
api.add_resource(signup, '/signup')
api.add_resource(logout, '/logout')
api.add_resource(myaacount, '/myaccount')
api.add_resource(login, '/login')

if __name__ == "__main__":
    app.run(debug=True)



