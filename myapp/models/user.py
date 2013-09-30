# -*- coding: utf-8 -*-
import bcrypt
from flask import current_app
from flask.ext.login import UserMixin
from ..database import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    _password = db.Column('password', db.String(128), nullable=False)

    def __init__(self, email="", password=""):
        self.email = email
        self.password = password

    def _get_password(self):
        """Return the password field and not the actual password"""
        return self._password

    def _set_password(self, password):
        """Hash the password with bcrypt using BCRYPT_LEVEL in config"""
        self._password = bcrypt.hashpw(password,
            bcrypt.gensalt(current_app.config['BCRYPT_LEVEL']))

    # Hide the password encryption by exposing password field only
    password = db.synonym('_password',
        descriptor=property(_get_password, _set_password))

    def check_password(self, password):
        if bcrypt.hashpw(password.encode('utf-8'), self.password.encode('utf-8')) == self.password:
            return True
        return False

    def is_active(self):
        return True

    @classmethod
    def authenticate(cls, email, password):
        """Authenticate with `email` and `password`"""
        user = cls.query.filter(User.email == email).first()

        if user:
            authenticated = user.check_password(password)
        else:
            authenticated = False

        return user, authenticated
