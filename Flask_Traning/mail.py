from flask import Flask, render_template
from flask_mail import Mail, Message
from config import Config


app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'delvadiya.gaurang2512@gmail.com'
app.config['MAIL_PASSWORD'] = '********'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
def index():
    msg = Message('Hey' , sender="delvadiya.gaurang2512@gmail.com", recipients=["gaurang.delvadiya2512@gmail.com"])
    msg.body = "This is just testing"
    mail.send(msg)
    return "sent"


if __name__ == '__main__':
    app.run(debug=True)
