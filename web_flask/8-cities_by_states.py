#!/usr/bin/python3

"""Script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/cities_by_states")
def cities_by_states():
    """Display a HTML page: (inside the tag BODY)"""
    return render_template("8-cities_by_states.html",
                           states=storage.all("State"))


@app.teardown_appcontext
def teardown_appcontext(self):
    """Call in this method storage.close()"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
