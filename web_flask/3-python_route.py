#!/usr/bin/python3
"""3. Python is cool!"""
from flask import Flask, url_for
from markupsafe import escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    text = text.replace('_', ' ')
    return f"C {escape(text)}"


@app.route('/python', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def ismagic(text):
    if ('_' in text):
        text = text.replace('_', ' ')
    return f"Python {escape(text)}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
