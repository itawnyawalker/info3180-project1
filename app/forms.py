from wsgiref.validate import validator
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class PropertyForm(FlaskForm):
    """Property data form"""
    title = StringField('Property Title', validators=[DataRequired()])
    num_bed = StringField('No.of bedrooms', validators=[DataRequired()])
    num_bath = StringField('No. of bathrooms', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    type = SelectField('Property Type', choices =["House", "Apartment"], validators=[DataRequired()])
    desc = TextAreaField('Description', validators=[DataRequired()])
    photo = FileField('Photo', validators=[FileRequired(),FileAllowed(['jpg','png', 'jpeg', 'Images only'])])