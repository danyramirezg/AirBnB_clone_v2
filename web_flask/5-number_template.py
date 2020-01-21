#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask, render_template

"""__name__ means this current file. In this case, it will be main.py.
 This current file will represent my web application."""

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    """Routes: /: display “Hello HBNB!” """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """Routes: /hbnb: display “HBNB" """
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    """Routes: /c/<text> Display “C ” followed by the value of the text
    variable (replace underscore _ symbols with a space )"""
    return "C " + text.replace("_", " ")


@app.route("/python/")
@app.route("/python/<text>")
def python(text="is cool"):
    """"Display “Python ”, followed by the value of the text variable
    (replace underscore _ symbols with a space )"""
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>")
def number(n):
    """Display “n is a number” only if n is an integer
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def template(n):
    """Display a HTML page only if n is an integer:
        H1 tag: “Number: n” inside the tag BODY"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
