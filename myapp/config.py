# -*- coding:utf-8 -*-

import os
from datetime import timedelta

project_name = "myapp"


class Config(object):
    DEBUG = False
    ASSETS_DEBUG = False
    TESTING = False
    USE_X_SENDFILE = False

    # DATABASE CONFIGURATION
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/%s_dev.sqlite" % project_name
    SQLALCHEMY_ECHO = False

    # FORMS CONFIGURATIOn
    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(24)
    LOGGER_NAME = "%s_log" % project_name
    PERMANENT_SESSION_LIFETIME = timedelta(days=1)
    BCRYPT_LEVEL = 12

    # EMAIL CONFIGURATION
    MAIL_SERVER = "localhost"
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_DEBUG = DEBUG
    MAIL_USERNAME = None
    MAIL_PASSWORD = None
    DEFAULT_MAIL_SENDER = "example@%s.com" % project_name

    # each as ("blog.views.app", {"url_prefix":"/blog"})
    BLUEPRINTS = [
        # FRONT
        ("myapp.apps.blog.app", {"url_prefix": "/blog"}),
    ]


class Dev(Config):
    DEBUG = True
    ASSETS_DEBUG = True
    LESS_RUN_IN_DEBUG = True


class Testing(Config):
    TESTING = True
    CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/%s_test.sqlite" % project_name
    BCRYPT_LEVEL = 0
