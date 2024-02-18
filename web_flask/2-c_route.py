#!/usr/bin/python3
"""Starts Flask web app
Routes:
    / - display "Hello HBNB!"
    /hbnb - display "HBNB"
    /c/<text> - display "C <text>"
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Handler function for the root URL."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Handler function for '/hbnb' URL."""
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    """Handler function for '/c/<text>' URL."""
    text = text.replace("_", " ")
    return "C %s" % text


if __name__ == "__main__":
    app.run(host="0.0.0.0")
