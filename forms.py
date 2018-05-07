from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, BooleanField

from wtforms import validators, ValidationError
from wtforms.validators import DataRequired

from modules.slides import *

class PresentationList(FlaskForm):
    choice = listslides()
    presentation = SelectField(
                   'Choose',
                   choices=choice,
               )
    submit = SubmitField("Open")
