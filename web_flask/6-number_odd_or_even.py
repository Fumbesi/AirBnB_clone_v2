#!/usr/bin/python3
"""
This is a Flask web application with multiple routes.
"""

from flask import Flask, render_template

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
    Replace underscore (_) symbols with spaces.
    """
    text = text.replace('_', ' ')
    return "C " + text

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_with_text(text):
    """
    Route that displays "Python " followed by the value of the text variable.
    Replace underscore (_) symbols with spaces. Default text is "is cool".
    """
    text = text.replace('_', ' ')
    return "Python " + text

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Route that displays "n is a number" only if n is an integer.
    """
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Route that displays an HTML page only if n is an integer.
    It generates an HTML page with the number displayed inside an H1 tag.
    """
    return render_template('6-number_odd_or_even.html', number=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Route that displays an HTML page only if n is an integer.
    It generates an HTML page with the number displayed inside an H1 tag along with its even/odd status.
    """
    status = "odd" if n % 2 != 0 else "even"
    return render_template('6-number_odd_or_even.html', number=n, status=status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
