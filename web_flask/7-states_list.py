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
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return render_template('7-states_list.html', storage=states)


@app.teardown_appcontext
def teardown_db(exception):
    '''closes the storage on teardown'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
