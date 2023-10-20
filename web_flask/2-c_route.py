#!/usr/bin/python3
"""
This is a simple Flask web application with three routes: '/', '/hbnb', and '/c/<text>'.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route that displays "Hello HBNB!".
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route that displays "HBNB".
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    """
    Route that displays "C " followed by the value of the text variable.
    Replace underscore (_) symbols with a space.
    """
    text = text.replace('_', ' ')
    return "C " + text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
