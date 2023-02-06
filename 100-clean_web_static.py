#!/usr/bin/python3
''' This is a fabfile containing fabric configuration '''

from fabric.api import *

# login details
env.user = 'ubuntu'
env.hosts = ['54.236.28.149', '54.157.143.204']
env.key_filename = '~/.ssh/school'


def do_clean(number=0):
    '''
    A cleanup function that deletes out of date archives
    '''
    
