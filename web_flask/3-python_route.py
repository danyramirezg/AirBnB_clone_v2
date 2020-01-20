#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
