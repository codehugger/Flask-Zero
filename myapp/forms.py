# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import TextField, PasswordField, HiddenField
from wtforms.validators import Required


class SigninForm(Form):
    email = TextField('Email', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    next = HiddenField('Next')
