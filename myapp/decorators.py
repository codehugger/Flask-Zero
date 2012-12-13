from functools import wraps

from flask.ext.login import current_user
from flask import flash, redirect, url_for, request


def requires_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated():
            flash(u'You need to be signed in for this page.', 'error')
            return redirect(url_for('signin', next=request.path))
        return f(*args, **kwargs)
    return decorated_function
