#!/usr/bin/python3
"""Initialize a Flask application with state_list, using the Storage"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Dispaly the list of cities"""
    states = storage.all(State).values()
    return (render_template('9-states.html', states=states))


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Dispaly the list of cities"""
    value_objts = storage.all(State).values()
    for states in value_objts:
        if states.id == id:
            return render_template('9-states.html', states=states)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """to clse the conection"""
    storage.close()


if (__name__ == '__main__'):
    app.run(host="0.0.0.0", port=5000)
