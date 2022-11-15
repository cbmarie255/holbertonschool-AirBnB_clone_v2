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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
