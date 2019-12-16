from flask import Flask, render_template
from loging_form import LoginForm
from config import Config


app = Flask(__name__, template_folder='template')
app.config.from_object(Config)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('loging.html', title='Sign In', form=form)

if __name__ == '__main__':
    app.run(debug=True)