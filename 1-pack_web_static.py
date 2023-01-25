#!/usr/bin/python3
"""This is a module containing fabric configuration"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """A function that generates a .tgz archive"""

    now = datetime.now()
    opt = '{}{}{}{}{}{}'.format(now.year, now.month, now.day, now.hour,
                                now.minute, now.second)
    version = local('mkdir -p versions')
    file_ = 'versions/web_static_{}.tgz'.format(opt)
    check = local('tar -czvf {} web_static'.format(file_))

    if check.succeeded:
        return os.path.relpath(file_)
    return None
