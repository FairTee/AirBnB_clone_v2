#!/usr/bin/python3
"""Starts Flask web app
Listening on 0.0.0.0:5000
Route '/' displays "Hello HBNB!"
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Handler function for the root URL."""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
