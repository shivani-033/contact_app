from flask import Flask
from flask_wtf import FlaskForm
from wtforms import TextAreaField , SubmitField
from wtforms.validators import Length , DataRequired

class ContactForm(FlaskForm):
    name = TextAreaField('enter name' , validators=[DataRequired() , Length(5)])
    phone = TextAreaField('enter phone no.' , validators=[DataRequired() , Length(5)])
    email = TextAreaField('enter email' , validators=[DataRequired() , Length(5)])
    submit = SubmitField('save info')