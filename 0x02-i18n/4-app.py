#!/usr/bin/env python3
from flask import request, Flask, render_template
from flask_babel import Babel
import requests
"""Basic app"""


class Config:
    """Languages config class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = LANGUAGES[0]
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel()


@babel.localeselector
def get_locale():
    """get locale"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app)


@app.route("/")
def index():
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(debug=True)
