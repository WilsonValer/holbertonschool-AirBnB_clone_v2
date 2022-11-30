#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """This function returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """display “C ” followed by the value of the text variable"""
    c_fun = text.replace('_', ' ')
    return 'C {}'.format(c_fun)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """display “Python ”, followed by the value of the text variable"""
    c_fun = text.replace('_', ' ')
    return 'C {}'.format(c_fun)


@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """This fuction displays  “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """H1 tag: Number: n inside the tag BODY"""
    return render_template('5-number.html', key_name=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5003')
