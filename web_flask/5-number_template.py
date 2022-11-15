#!/usr/bin/python3
"""
    A script that starts a Flask web application with parameters.
"""
from flask import Flask
from flask import render_template

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


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def route_for_python(text='is cool'):
    '''Feeding a string to return as a response.'''
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def route_for_ints(n=None):
    '''Feeding a string to return as a response.'''
    if type(n) is int:
        return '{} is a number'.format(n)


@app.route('/number_template/int:n>', strict_slashes=False)
def route_for_number_template(n=None):
    '''Feeding a string to return as a response.'''
    if type(n) is int:
        return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
