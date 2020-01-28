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


@app.route("/states")
@app.route("/states/<id>")
def states(id=None):
    """Display a HTML page"""
    return render_template("9-states.html", states=storage.all("State"), id=id)


@app.route("/hbnb_filters")
def amenities():
    """Display a HTML page"""
    return render_template('10-hbnb_filters.html', states=storage.all("State"),
                           amenities=storage.all("Amenity"))


@app.route("/hbnb")
def places():
    """Display a HTML page"""
    return render_template('100-hbnb.html', states=storage.all("State"),
                           amenities=storage.all("Amenity"),
                           places=storage.all("Place"))


@app.teardown_appcontext
def teardown_appcontext(self):
    """Call in this method storage.close()"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
