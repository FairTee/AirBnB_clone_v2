#!/usr/bin/python3
"""Starts Flask web app
Routes:
    / - display "Hello HBNB!"
    /hbnb - display "HBNB"
    /c/<text> - display "C <text>"
    /python/<text> - display "Python is cool"
    /number/<n> - display n if integer
    /number_template/<n> - display a HTML page if n is int
    /number_odd_or_even/<n> - displays if a number is odd or even
"""
from flask import Flask, render_template

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


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text="is cool"):
    """Handler function for '/python/<text>' URL."""
    text = text.replace("_", " ")
    return "Python %s" % text


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """Handler function for '/number/<n>' URL."""
    return "%i is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Handler function for '/number_template/<n>' URL."""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Handler function for '/number_odd_or_even/<n>' URL"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
