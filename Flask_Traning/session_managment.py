from flask import Flask, request, render_template, session
from config import Config
app  = Flask(__name__,template_folder='template')

app.config.from_object(Config)

@app.route('/')
def index():
    return render_template('session_sign_up.html')

@app.route('/loginn')
def loginn():
    return render_template('loginn.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    session['username'] = username
    return "<h2>user created</h2> <p>Click Here to sign In <a href='http://127.0.0.1:5000/loginn'>login</a></p>"

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    if username in session.get('username', None):
        username = session.get('username', None)
        return 'Hey ' + username + '<p><a href="http://127.0.0.1:5000/logout">Logout</a></p>'
    else:
        return 'please login first <a href="http://127.0.0.1:5000/">Sign Up</a>'

@app.route('/logout')
def logout():
    session.pop('username', None)
    return "Good Bye"
if __name__ == '__main__':
    app.run(debug=True)
