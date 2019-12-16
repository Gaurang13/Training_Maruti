from flask import Flask, render_template


app = Flask(__name__, template_folder="template")

@app.route('/')
@app.route('/index')
def index():
    user = {"username": "gaurang"}
    posts = [
        {
            'author': {"username": "Mahendra"},
            'body': 'I think i have to give some time to my family'
        },
        {
            'author': {"username": "Krupa"},
            'body': 'Time is money'
        }
    ]
    return render_template('index.html', user=user, title="name post", posts=posts)

if __name__ == '__main__':

    app.run(debug=True)
