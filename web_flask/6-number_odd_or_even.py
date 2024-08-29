#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """Returns HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Replace underscores with spaces in the text variable"""
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_t(text="is cool"):
    """Replace underscores with spaces in the text variable"""
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Display “n is a number” only if n is an integer"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def numbn(n):
    """Display a HTML page only if n is an integer"""
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """Display a HTML page only if n is an integer"""
    parity = "even" if n % 2 == 0 else "odd"
    return render_template(
        "6-number_odd_or_even.html",
        number=n,
        parity=parity
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
