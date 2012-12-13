# -*- coding: utf-8 -*-

from flask.ext.testing import TestCase

from myapp.config import Testing
from myapp.database import create_all, drop_all, seed_all, remove_session
from myapp.main import app_factory


class BaseTestCase(TestCase):

    def create_app(self):
        app = app_factory(Testing)
        return app

    def setUp(self):
        create_all()
        seed_all()

    def tearDown(self):
        drop_all()
        remove_session()

    def signIn(self, email="john.doe@example.com", password="secret"):
        return self.client.post('/signin',
            data=dict(email=email, password=password, remember=False))

    def signOut(self):
        return self.client.get('/signout')
