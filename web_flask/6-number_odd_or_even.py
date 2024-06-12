#!/usr/bin/python3
"""4. Is it a number? """
from flask import Flask, url_for, render_template
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
    if '_' in text:
        text = text.replace('_', ' ')
    return f"Python {escape(text)}"


@app.route('/number/<int:n>', strict_slashes=False)
def isnumber(n):
    return f"{escape(n)} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def numbertemplate(n):
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def evenOdd(n):
    if n % 2 == 0:
        res = "even"
    else:
        res = "odd"

    return render_template("6-number_odd_or_even.html", n=n, res=res)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
