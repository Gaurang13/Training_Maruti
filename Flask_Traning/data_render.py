from flask import Flask, render_template, request
app = Flask(__name__, template_folder='template')

@app.route('/')
def student():
    return render_template('student.html')
@app.route('/result', methods= ['POST'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template('result.html', result = result)

if __name__ == '__main__':
    app.run(debug=True)
