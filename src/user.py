from dataclasses import dataclass
from datetime import date
from enum import Enum
from uuid import UUID, uuid4
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
import phonenumbers
from typing import Type

class UserRegisterForm(FlaskForm):
    first_name = StringField('Fist Name', validators=[DataRequired()])
    second_name = StringField('Second Name', validators=[DataRequired()])
    third_name = StringField('Third Name (optional)')
    fourth_name = StringField('Fourth Name (optional)')
    email = StringField('Email', [DataRequired(), Email('you must enter a valid email address')])
    phone = StringField("Phone Number with +country code", [DataRequired()])
    whatsapp = StringField("Whatsapp username")
    invite_code = StringField("The invite code provided by your teacher", [DataRequired()])
    submit = SubmitField('Submit')

class Address:
    """The address holds the users address information"""

    def __init__(self, line_one, line_two, line_three, city, province, state, country, post_code):
        self.line_one = line_one
        self.line_two = line_two
        self.line_three = line_three
        self.city = city
        self.province = province
        self.state = state
        self.country = country
        self.post_code = post_code

class UserType(Enum):
    ADMIN = 1
    INSTRUCTOR = 2 
    STUDENT = 3
    INSTRUCTOR_STUDENT = 4

@dataclass
class User:
    """The user is the user model for the database table user"""
    def __init__(self, first_name: str, second_name: str, third_name: None, fourth_name: None, 
                 user_type: UserType, email: str, phone: str, whatsapp: str, instructor_name: str, id: str,
                 instructor_id: str):
        self.first_name = first_name
        self.second_name = second_name
        self.third_name = third_name
        self.fourth_name = fourth_name
        self.user_type = user_type
        self.email = email
        self.phone = phone
        self.whatsapp = whatsapp
        self.instructor_name = instructor_name
        self.id = id
        self.created = None
        self.updated = None
        self.instructor_id = instructor_id
    
    @property
    def test_phone(self) -> bool:
        try:
            pn = phonenumbers.parse(self.phone)
            if pn:
                return True
        except phonenumbers.NumberParseException:
            return False

