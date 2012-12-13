# -*- coding: utf-8 -*-

from flask.ext.script import Command

from database import create_all, drop_all, seed_all


class CreateDB(Command):
    """Creates sqlalchemy database"""

    def run(self):
        create_all()


class DropDB(Command):
    """Drops sqlalchemy database"""

    def run(self):
        drop_all()


class SeedDB(Command):
    """Seeds sqlalchemy database"""

    def run(self):
        drop_all()
        create_all()
        seed_all()
