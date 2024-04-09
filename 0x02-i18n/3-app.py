#!/usr/bin/env python3
""" doc doc doc """
from flask import Flask, render_template, request
from flask_babel import Babel
from flask_babel import _


class Config(object):
    """Configurations for Babel module."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    '''Get locale from request URL.'''
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def message():
    """Displaying the welcoming message """
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
