#!/usr/bin/python3
"""This script starts a Flask web application"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """
    index is the handler for requests to the / route

    :return (str): is Hello HBNB!
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """
    hbnb is the handler for requests to the /hbnb route

    :return (str): is HBHB
    """
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    """
    c is the handler for request to the /c/<text> route

    :return (str): is C <text>
    """
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
