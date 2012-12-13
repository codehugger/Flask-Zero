# -*- coding:utf-8 -*-

from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def drop_all():
    db.drop_all()


def create_all():
    db.create_all()


def seed_all():
    from database import db
    from myapp.models import User

    # Create a user
    db.session.add(User(email="john.doe@example.com", password="secret"))
    db.session.commit()


def remove_session():
    db.session.remove()
