#!/usr/bin/python3
'''This is a module'''

from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state():
    '''
    handle state route
    '''
    return render_template('7-states_list.html', storage=storage.all(State))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
