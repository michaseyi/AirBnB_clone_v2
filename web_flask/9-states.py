#!/usr/bin/python3
"""This script starts a Flask web application"""
import sys
from flask import Flask, render_template

sys.path.append('..')

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def states_list():
    """
    states_list renders a list of available states
    """
    from models.state import State
    from models import storage
    states = list(storage.all(State).values())
    states.sort(key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states')
def cities_by_states():
    """
    cities_by_states renders a list of available states and cities
    """
    from models.state import State
    from models import storage
    states = list(storage.all(State).values())
    states.sort(key=lambda state: state.name)
    for state in states:
        state.cities.sort(key=lambda city: city.name)
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states/<id>')
def states(id):
    """
    states displays a state and its cities

    :param id(str): is the id of the state to be desplayed
    """
    from models.state import State
    from models import storage
    state = storage.all(State).get("State.{}".format(id), None)
    if state is not None:
        state.cities.sort(key=lambda city: city.name)
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def reload_db(exception):
    """
    reload_db reloads the current sesson after each request
    """
    from models import storage
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
