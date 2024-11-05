#!/usr/bin/env python3
from flask import request, Flask, render_template, g
from flask_babel import Babel, format_datetime
import requests
import pytz
"""Basic app"""

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Login mock system"""
    id = request.args.get('login_as')
    return users.get(int(id)) if id else None


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
    if g.user and g.user["locale"] in app.config['LANGUAGES']:
        return g.user["locale"]
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_locale():
    """get time zone"""
    timezone = request.args.get('timezone')
    if not timezone and g.user and g.user["timezone"]:
        timezone = g.user["timezone"]
    try:
        if timezone:
            pytz.timezone(timezone)
            return timezone
    finally:
        return None


babel.init_app(app)


@app.before_request
def before_request():
    """Set user"""
    g.user = get_user()


@app.route("/")
def index():
    g.time = format_datetime()
    return render_template("7-index.html")


if __name__ == "__main__":
    app.run(debug=True)
