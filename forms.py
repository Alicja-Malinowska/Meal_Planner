from wtforms import SubmitField, BooleanField, StringField, PasswordField, IntegerField, TextAreaField, validators
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired


class RegistrationForm(FlaskForm):
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


class LoginForm(FlaskForm):
    email_address = StringField('Email Address', [validators.DataRequired(),
                                                  validators.Email(), validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(), ])
    submit = SubmitField('Submit')

class AddRecipe(FlaskForm):
    name = StringField('Recipe Name', [validators.DataRequired()])
    ingredients = TextAreaField('Ingredients')
    servings = StringField('Servings')
    instructions = TextAreaField('Instructions')
    tags = StringField('Tags')
    image = FileField('Image', validators=[
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])