from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo, ValidationError
from ..models import User

class LoginForm(Form):
    username = StringField('Your Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')

class SignupForm(Form):
    username = StringField('Your Username', validators=[DataRequired(), Length(3, 80), Regexp(r'^[a-zA-Z0-9, ]*$',
                                                                                              message="Tags can only contain letters and numbers")])
    category = SelectField('Category', choices=[('student', 'Student'), ('teacher', 'Teacher')],
                           validators=[DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Length(3, 80), Email()])

    def validate_email(self, email_field):
        if (User.query.filter_by(email=email_field.data).first()):
            raise ValidationError('There already user with email address.')

    def validate_username(self, username_field):
        if (User.query.filter_by(username=username_field.data).first()):
            raise ValidationError('User name already exists.')