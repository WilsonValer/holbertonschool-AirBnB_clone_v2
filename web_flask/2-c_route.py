#!/usr/bin/python3
""" Write a script that starts a Flask web application:"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

#  Utilice el route()decorador para vincular una función a una URL.


@app.route("/")
def hello_world():
    """ method that return mesages in the server"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ method that return mesages in the server"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    """Write a script that starts a Flask web application:"""
    c_fun = text.replace('_', ' ')
    return f'C {escape(c_fun)}'


if (__name__ == '__main__'):
    app.run(debug=True, host="0.0.0.0", port=6000)
