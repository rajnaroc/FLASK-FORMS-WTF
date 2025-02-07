from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired,Email, Length, EqualTo

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
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=4, max=8),
        EqualTo('confirm', message='Password must match inutl')
    ])
    confirm = PasswordField('Repeat password', validators=[
        DataRequired(),
        Length(min=4, max=8)
    ])
    submit = SubmitField('Enviar')