from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__, template_folder='template')
from config import Config


app.config.from_object(Config)

@app.route('/')
def index():
    return render_template('flash_index.html')

@app.route('/login')
def login_template():
    return render_template('flash_login.html')

@app.route('/flash_login', methods= ['POST'])
def login():
    error = None
    if request.form['username'] != 'admin' or request.form['password'] != 'admin':
        error = 'invalid username and password'
        return error
    else:
        flash("login successfull ")
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)