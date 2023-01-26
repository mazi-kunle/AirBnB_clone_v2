#!/usr/bin/python3
"""This is a module containing fabric configuration"""

from fabric.api import *
from datetime import datetime
import os
import re


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


# set login details
env.user = 'ubuntu'
env.hosts = ['54.236.28.149', '54.157.143.204']
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    '''
    A function that distributes an archive to your web servers'
    '''

    if not os.path.exists(archive_path):
        return False

    match = re.search(r'web_static_[0-9]*', archive_path).group()
    new_directory = '/data/web_static/releases/{}/'.format(match)
    file_ = re.search(r'web_static_[0-9]*\.tgz', archive_path).group()
    # upload archive
    put(archive_path, '/tmp/')

    check1 = run('mkdir -p {}'.format(new_directory))
    check2 = run('tar -zxvf /tmp/{} -C {}'.format(file_, new_directory))
    check3 = run('rm /tmp/{}'.format(file_))
    check4 = run('rm -rf /data/web_static/current')
    check5 = run('mv {}web_static/* {}'.format(new_directory, new_directory))
    check6 = run('rm -rf {}web_static'.format(new_directory))
    check7 = run('ln -s {} /data/web_static/current'
                 .format(new_directory))

    if (check1.succeeded and check2.succeeded and check3.succeeded and
            check3.succeeded and check4.succeeded and check5.succeeded and
            check6.succeeded and check7.succeeded):
        return True
    return False
