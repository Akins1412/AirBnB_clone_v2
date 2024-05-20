#!/usr/bin/python3

"""script that starts a Flask web application
Your web application must be listening on 0.0.0.0
"""

from flask import Flask
from flask import render_template
from model import storage

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    "display a HTML page"
    state = storage.all(State)
    return  render_template("7-states_list.html", state=state)

@app.teardown_appcontext
def teardown(exempt):
    "remove the current SQLAlchemy Session"
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
