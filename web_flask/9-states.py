#!/usr/bin/python3
'''This is a module'''

from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def state():
    '''
    handle state route
    '''
    states = storage.all(State)
    return render_template('9-states.html', storage=states)


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    '''
    handle state route
    '''
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html', storage=state)
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown_db(exception):
    '''closes the storage on teardown'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
