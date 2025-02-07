from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired,Email, Length

class Persona(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        Length(min=3, max=10)     
        ])
    email = StringField('Email', validators=[
        DataRequired(),
        Length(min=5, max=12),
        Email()
    ])
    telefono = StringField('Telefono', validators=[
        DataRequired(),
        Length(min=9, max=14)
    ])
    password = StringField('Password', validators=[
        DataRequired(),
        Length(min=4, max=8)
    ])
    submit = SubmitField('Enviar')