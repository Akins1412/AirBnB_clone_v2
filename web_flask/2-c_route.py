#!/usr/bin/python3
"""Script that starts a Flask"""

from flask import Flask

app = Flask(__name__)
"""For instances"""
# app.url_map.strict_slashes = False

@app.route('/', strict_slashes=False)
def home():
    "Display homepage"
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    "Dispaly HBNB"
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    "Display followed by the value of the text variable"
    return text.replace("_", "")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
