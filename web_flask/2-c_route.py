#!/usr/bin/python3
'''This is a module'''

from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''
    display hello HBNB
    '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display():
    '''
    display hbnb
    '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    '''
    display c <text>
    '''
    return 'C {}'.format(escape(text.replace('_', ' ')))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
