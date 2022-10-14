#!/usr/bin/python3
"""This script starts a Flask web application"""
from flask import Flask, render_template

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

    :param text(str): path vairable
    :return (str): is C <text>
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python(text='is_cool'):
    """
    python is the handler for request to the /python/<text> route

    :param text(str): path variable, default is 'is_cool'
    :return (str): is Python <text>
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n: int):
    """
    number is the handler for request to the /number/<int:n> route

    :param n(int): path variable
    :return (str): is <n> is a number
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n: int):
    """
    number_template is the handler for request to the /number/<int:n> route

    :param n(int): path variable
    :return (str)
    """
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
