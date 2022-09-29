#!/usr/bin/python3
"""This module contains a function that compresses a directory
to .tgz file"""
from fabric import api
from datetime import datetime
import os


def do_pack():
    """
    do_pack generates a .tgz archive from the contents of the web_static
    folder
    :return is the name of the archive created or None if it fails
    """
    time = datetime.now()
    archive_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        time.year, time.month, time.day, time.hour, time.minute, time.second)
    if not os.path.isdir("versions"):
        if api.local("mkdir -p versions").failed:
            return None
    if api.local("tar -cvzf {} web_static".format(archive_name)).failed:
        return None
    return archive_name
