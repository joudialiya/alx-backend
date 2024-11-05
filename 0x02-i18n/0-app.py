#!/usr/bin/env python3
import flask
"""Basic app"""

app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template("index.html")
