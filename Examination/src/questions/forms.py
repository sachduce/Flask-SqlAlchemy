from flask_wtf import Form
from wtforms.fields import StringField, SelectField
from wtforms.validators import DataRequired, Length


class QuestionForm(Form):
    question = StringField('Question: ', validators=[DataRequired(), Length(4, 300)])
    option1 = StringField('Option 1: ', validators=[DataRequired(), Length(1, 300)])
    option2 = StringField('Option 2: ', validators=[DataRequired(), Length(1, 300)])
    option3 = StringField('Option 3: ', validators=[DataRequired(),  Length(1, 300)])
    option4 = StringField('Option 4: ', validators=[DataRequired(), Length(1, 300)])
    answer = SelectField('Answer: ', validators=[DataRequired()], choices=[('option1', 'Option 1'),
                                                                           ('option2', 'Option 2'),
                                                                           ('option3', 'Option 3'),
                                                                           ('option4', 'Option 4')])
