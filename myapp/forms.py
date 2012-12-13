# -*- coding: utf-8 -*-
from flask.ext.wtf import (Form, TextField, PasswordField, HiddenField, Required)


class SigninForm(Form):
    email = TextField('Email', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    next = HiddenField('Next')
