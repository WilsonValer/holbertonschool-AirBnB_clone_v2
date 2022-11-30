#!/usr/bin/python3
""" Starting a Flask web application """
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ display a message """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ display a message """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_isfun(text):
    """ display “C ” followed by the value of the text variable """
    c_fun = text.replace('_', ' ')
    return 'C {}'.format(c_fun)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
