from flask_wtf import FlaskForm
from  wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Email,EqualTo
from ..models import  User
from wtforms import ValidationError

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators =[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class RegistartionForm(FlaskForm):
    email = StringField("Your Email Address",validators=[DataRequired(),Email()])
    username = StringField("Enter your Username",validators=[DataRequired()])
    password = PasswordField("password",validators=[DataRequired(),EqualTo('password_confirm',message="passwords must match")])
    password_confirm = PasswordField("Confirm Passwords",validators=[DataRequired()])
    submit = SubmitField("Sign up")

    def validate_email(self, data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self, data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('That username is taken')
