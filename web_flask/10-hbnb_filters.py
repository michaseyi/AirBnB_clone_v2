#!/usr/bin/python3
"""This script starts a Flask web application"""
import sys
from flask import Flask, render_template

sys.path.append('..')

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def hbnb_filters():
    """
    hbnb_filters renders hbnb page
    """
    from models.state import State
    from models.amenity import Amenity
    from models import storage

    states = list(storage.all(State).values())
    states.sort(key=lambda state: state.name)
    for state in states:
        state.cities.sort(key=lambda city: city.name)
    amenities = list(storage.all(Amenity).values())
    amenities.sort(key=lambda amenity: amenity.name)
    return render_template(
        '10-hbnb_filters.html',
        states=states,
        amenities=amenities)


@app.teardown_appcontext
def reload_db(exception):
    """
    reload_db reloads the current sesson after each request
    """
    from models import storage
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)