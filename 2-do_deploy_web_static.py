#!/usr/bin/python3
"""Fabric script that distributes an archive to the web servers,
using the function do_deploy"""

from fabric.api import local, put, run, env
import os.path
from datetime import datetime
from os.path import exists

env.hosts = ['35.237.153.43', '35.229.32.216']


def do_pack():
    """Generates a .tgz archive from the contents of the web_static"""

    dtime = datetime.utcnow()
    archi = "versions/web_static_{}{}{}{}{}{}.tgz".format(dtime.year,
                                                          dtime.month,
                                                          dtime.day,
                                                          dtime.hour,
                                                          dtime.minute,
                                                          dtime.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(archi)).failed is True:
        return None
    return archi


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False

    new_path = archive_path[9:]
    b_path = archive_path[9:-4]
    path = "/data/web_static/releases/"

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Uncompress the archive to the folder
        run('mkdir -p {}{}'.format(path, b_path))
        run('tar -xzf /tmp/{} -C {}{}/'.format(new_path, path, b_path))
        run('rm /tmp/{}'.format(new_path))
        run('rm /tmp/{}'.format(new_path))
        run('mv {}/web_static/* {}'.format(b_path, b_path))
        run('rm -rf {}/web_static'.format(path))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, new_path))
        return True
    except:
        return False
