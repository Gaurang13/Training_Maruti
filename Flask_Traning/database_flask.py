import pymysql.cursors
from flask import Flask, request, render_template
from config import Config


app = Flask(__name__, template_folder='template')
app.config.from_object(Config)

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Mtech@12345',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

@app.route('/', methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        fname = request.form['firstname']
        lname = request.form['lastname']
        age = request.form['age']
        try:
            with connection.cursor() as cursor:
                sql = "insert into user(first_name, last_name, age) values(%s, %s, %s)"
                cursor.execute(sql,(fname, lname, age))
                connection.commit()
        finally:
            pass
        return "Done" + "<a href='http://127.0.0.1:5000/show'>Click Here To See It<a>"
    return render_template('login_db.html')

@app.route('/show', methods = ['POST', 'GET'])
def show():
    try:
        with connection.cursor() as cursor:
            cursor.execute('select * from user')
            showdata = cursor.fetchone()
            return showdata

    finally:
        pass
if __name__ == "__main__":
    app.run(debug=True)