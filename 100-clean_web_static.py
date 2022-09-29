#!/usr/bin/python3
"""This module contains do_clean that deletes out of date archives
"""
from fabric import api
import os


api.env.user = 'ubuntu'
api.env.hosts = ['34.239.158.102', '18.208.159.79']


def do_clean(number=0):
    """
    do_clean deletes out-of-date archives
    """
    number = int(number)
    if number < 2:
        number = 1
    if os.path.isdir("versions"):
        dirs = sorted(os.listdir("versions"), reverse=True)
        for file in dirs[number:]:
            os.unlink(os.path.join("versions", file))
    with api.cd("/data/web_static/releases"):
        command = """\
        keep=$(ls -t | grep web_static | head -n {})
        for file in $(ls | grep web_static); do
            if ! [[ "${{keep[*]}}" =~ "$file" ]]; then
                rm -rf $file
            fi
        done
        """.format(number)
        if api.run("{}".format(command)).failed:
            return False
