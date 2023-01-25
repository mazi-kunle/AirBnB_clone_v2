#!/usr/bin/python3
'''This is a module containing fabric configuration'''

from fabric.api import *
from datetime import datetime
import os


def do_pack():
    '''
    A function that generates a .tgz archivw
    from the contents of the web_static folder
    '''
    now = datetime.now()
    opt = '{}{}{}{}{}{}'.format(now.year, now.month, now.day, now.hour,
                                now.minute, now.second)
    version = local('mkdir -p versions')
    file_ = f'versions/web_static_{opt}.tgz'
    check = local(f'tar -czvf {file_} /AirBnB_clone_v2/web_static/')

    if check.succeeded:
        return os.path.relpath(file_)
    return None
