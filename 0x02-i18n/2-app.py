#!/usr/bin/env python3
"""Basic flask web app"""
from flask import request, Flask, render_template
from flask_babel import Babel


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
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app)


@app.route("/")
def index():
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(debug=True)
