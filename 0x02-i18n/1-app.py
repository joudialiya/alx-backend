#!/usr/bin/env python3
import flask
from flask_babel import Babel
"""Basic app"""


class Config:
    """Languages config class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = LANGUAGES[0]
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = flask.Flask(__name__)
babel = Babel()
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel.init_app(app)


@app.route("/")
def index():
    return flask.render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)
