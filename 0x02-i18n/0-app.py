#!/usr/bin/env python3
"""
Basic flask web app with a simple template
"""
import flask


app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)
