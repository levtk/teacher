from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class UserForm(FlaskForm):
    first_name = StringField('Fist Name', validators=[DataRequired()])
    second_name = StringField('Second Name', validators=[DataRequired()])
    third_name = StringField('Third Name')
    email = StringField('Email', [DataRequired(), Email('you must enter a valid email address')])
    submit = SubmitField('Submit')