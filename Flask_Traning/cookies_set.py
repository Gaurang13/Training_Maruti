from flask import Flask, render_template, request, make_response

app = Flask(__name__,template_folder='template')

@app.route('/')
def index():
    return render_template('cookies_index.html')

@app.route('/setcookies', methods = ['POST'])
def setcookies():
        user = request.form['name']
        resp = make_response(render_template('read_cookies.html'))
        resp.set_cookie('Name', user)
        return resp

@app.route('/getcookies')
def getcookies():
    name = request.cookies.get('Name')
    return '<h1>Welcome ' + name + '</h1><p>Delete:<a href="http://127.0.0.1:5000/delete_cookies">Delete</a></p>'

@app.route('/delete_cookies')
def delete():
    if request.cookies.get('Name'):
        res = make_response("<h1>Cookies removed</h1>")
        res.set_cookie('Name', '')
        return res
    else:
        return '<h1>There is no cookies found</h1>'

if __name__ == '__main__':
    app.run(debug=True)