#!/usr/bin/python3
"""This script starts a Flask web application"""
import sys
from flask import Flask, render_template

sys.path.append('..')

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """
    states_list renders a list of available states
    """
    from models.state import State
    from models import storage
    states = list(storage.all(State).values())
    states.sort(key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def reload_db(exception):
    """
    reload_db reloads the current sesson after each request
    """
    from models import storage
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
