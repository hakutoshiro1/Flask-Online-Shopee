from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField

class RegisterForm(FlaskForm):
    username=StringField(label='User Name:')
    email=StringField(label='Email Address:')
    password1=StringField(label='Password:')
    password2=StringField(label='Confirm Password:')
    submit=SubmitField(label='Create Account')