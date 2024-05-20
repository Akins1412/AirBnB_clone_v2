#!/usr/bin/python3
"""Script that starts a Flask
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): Displays 'Python' followed by the value of <text>.
    /number/<n>: Displays 'n is a number' only if <n> is an integer.

"""

from flask import Flask
from flask import render_template

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
    text = text.replace("_", " ")
    return "C {}".format(text)

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    "display “Python ”, followed by the value of the text variable"
    text = text.replace("_", " ")
    return "Python {}".format(text)

@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    "display “n is a number” only if n is an integer"
    return f"{} n is a number"

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    "display a HTML page only if n is an integer"
    return number_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000) 
