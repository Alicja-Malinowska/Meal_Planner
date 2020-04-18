from wtforms import SubmitField, BooleanField, StringField, PasswordField, IntegerField, validators
from flask_wtf import Form


class RegistrationForm(Form):
    first_name = StringField('First Name',
                             [validators.DataRequired()])
    last_name = StringField('Last Name',
                            [validators.DataRequired()])
    email_address = StringField('Email Address', [validators.DataRequired(),
                                                  validators.Email(), validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm',
                           message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Submit')


class LoginForm(Form):
    email_address = StringField('Email Address', [validators.DataRequired(),
                                                  validators.Email(), validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(), ])
    submit = SubmitField('Submit')