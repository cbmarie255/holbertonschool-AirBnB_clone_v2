#!/usr/bin/python3
"""
    A script that starts a Flask web application with parameters.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''returning a string as a response.'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def route_dos():
    '''returning a string as a response.'''
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def route_for_c(text=None):
    '''Feeding a string to return as a response.'''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<string:text>', strict_slashes=False)
def route_for_python(text='is cool'):
    '''Feeding a string to return as a response.'''
    return 'Python {}'.format(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
