from wtforms import Form
from wtforms import StringField,SelectField,RadioField,IntegerField, EmailField
from wtforms import validators

class UsersForm(Form):
    nombre=StringField('nombre', [
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=10,message='ingresa nombre valido')
    ])
    apaterno=StringField('apaterno', [
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=10,message='ingresa apaterno valido')
    ])
    amaterno=StringField('amaterno', [
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=10,message='ingresa amaterno valido')
    ])
    edad=IntegerField('edad', [
        validators.number_range(min=1, max=20,message='Valor no valido')
    ])
    correo=EmailField('correo', [
        #validators.email(message='Ingrese un correo valido')
    ])
    

class UsersForm2(Form):
    id=IntegerField(id)
    nombre=StringField('nombre', [
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=10,message='ingresa nombre valido')
    ])
    apaterno=StringField('apaterno', [
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=100,message='ingresa apaterno valido')
    ])

    email=EmailField('correo', [
        #validators.Email(message='Ingrese un correo valido')
    ])
    