#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /hbnb: HBnB home page.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnbs():
    """Displays the main HBnB filters HTML page."""
    state = storage.all("State")
    amenity = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("100-hbnb.html",
                           state=state, amenity=amenity, places=places)


@app.teardown_appcontext
def teardown(exemp):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
