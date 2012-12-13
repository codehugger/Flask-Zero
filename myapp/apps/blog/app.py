# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from flask.ext.assets import Bundle

from myapp.extensions import assets
from myapp.decorators import requires_login

app = Blueprint("blog", __name__, template_folder="templates", static_folder="static")
js = Bundle("blog/blog.js", filters="jsmin", output="dist/blog.js")
css = Bundle(
    "less/base.less",
    "blog/blog.less",
    filters="less", output="dist/blog.css")
assets.register("js_blog", js)
assets.register("css_blog", css)


@app.route("/")
@requires_login
def index():
    return render_template("blog/index.html")
