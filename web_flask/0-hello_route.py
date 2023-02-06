#!/usr/bin/python3
'''This is a module'''

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''
    display hello HBNB
    '''
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
