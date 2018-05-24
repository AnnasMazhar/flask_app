from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class RegistrationForm(FlaskForm):

    name = StringField("What is Your name? ")
    email = StringField("Enter Your email: ")
    submit = SubmitField('Register')
