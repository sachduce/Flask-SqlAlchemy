from flask_wtf import Form
from wtforms.fields import StringField, SelectField, RadioField
from wtforms.validators import DataRequired, Length


class TestForm(Form):

    answer = RadioField('Answer: ', validators=[DataRequired()], choices=[('option1', 'Option 1'),
                                                                       ('option2', 'Option 2'),
                                                                       ('option3', 'Option 3'),
                                                                       ('option4', 'Option 4')])
