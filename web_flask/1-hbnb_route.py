#!/usr/bin/python3
""" Write a script that starts a Flask web application:"""
from flask import Flask

app = Flask(__name__)


@app.route("/") # Utilice el route()decorador para vincular una función a una URL.
def hello_world():
    """ method that return mesages in the server"""
    return "Hello HBNB!"

@app.route("/hbnb") 
def hbnb():
    """ method that return mesages in the server"""
    return "HBNB!"


if (__name__ == '__main__'):
    app.run(debug=True, host="0.0.0.0", port=5000)