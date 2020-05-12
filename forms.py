from wtforms import SubmitField, BooleanField, StringField, PasswordField, IntegerField, TextAreaField, validators
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired



class RegistrationForm(FlaskForm):
    first_name = StringField('First Name',
                             [validators.DataRequired()])
    last_name = StringField('Last Name',
                            [validators.DataRequired()])
    email_address = StringField('Email Address', [validators.DataRequired(),
                                                  validators.Email(), validators.Length(min=6, max=35, message="It looks like this is too long or too short to be a valid email address!")])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm',
                           message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    email_address = StringField('Email Address', [validators.DataRequired(),
                                                  validators.Email()])
    password = PasswordField('New Password', [
        validators.DataRequired(), ])
    submit = SubmitField('Submit')

class AddRecipe(FlaskForm):

    def semicolon_check(form, field):
        if len(field.data) > 0 and not ';' in field.data:
            raise validators.ValidationError("Make sure that your tags are separated with semicolons!")

    name = StringField('Recipe Name', [validators.DataRequired()])
    ingredients = TextAreaField('Ingredients')
    servings = StringField('Servings')
    instructions = TextAreaField('Instructions')
    tags = StringField('Tags', [semicolon_check])
    image = FileField('Image', validators=[
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])