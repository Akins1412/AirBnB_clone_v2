#!/usr/bin/python3
"""Script that starts a Flask"""

from flask import Flask

app = Flask(__name__)
"""For instances"""
app.url_map.strict_slashes = False

@app.route('/')
def home():
    "Display homepage"
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000) 