#!/usr/bin/python3

"""Fabric script that creates and distributes an archive to your web servers,
 using the function deploy"""

import os.path
from fabric.api import local
from datetime import datetime


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


def do_deploy():
    pass


def deploy():
    """creates and distributes an archive using the function deploy"""

    path_arch = do_pack()

    if path_arch is None:
        return False
    return do_deploy(path_arch)
