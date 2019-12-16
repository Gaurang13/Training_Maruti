from flask import Flask,render_template, request, flash
from flask_wtf import Form
from wtforms import RadioField ,TextField, SubmitField, SelectField, validators, ValidationError
from config import Config

app = Flask(__name__,template_folder='template')
app.config.from_object(Config)
class ContactForm(Form):
    name = TextField("Name Of Student", [validators.Required("Please enter your name.")])
    gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
    email = TextField("Email", [validators.Required("Please enter your email address."),validators.Email("Please enter valide  email address.")])
    language = SelectField('Languages', choices=[('cpp','C++'),
                                                 ('py','Python')])
    submit = SubmitField("Send")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('wtf_contact.html', form=form)
        else:
            return 'SuccessFull'
    elif request.method == 'GET':
        return render_template('wtf_contact.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)