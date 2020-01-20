#!/usr/bin/python3

"""Script that starts a Flask web application"""

from flask import Flask

"""__name__ means this current file. In this case, it will be main.py.
 This current file will represent my web application."""

app = Flask(__name__)
app.url_map.strict_slashes = False

"""Routes:/: display “Hello HBNB!” """


@app.route("/")
def home():
    return "Hello HBNB!"


"""Web application must be listening on 0.0.0.0, port 5000"""
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
