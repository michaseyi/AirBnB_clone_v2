#!/usr/bin/python3
"""This module contains a function that deploys a web_static
to remote hosts"""
import os
from fabric import api


api.env.user = 'ubuntu'
api.env.hosts = ['34.239.158.102', '18.208.159.79']


def do_deploy(archive_path: str):
    """
    do_deploy deploys web_static to hosts servers

    :param archive_path(str): is the path to archive to be deployed
    :return (bool): is True if operations is successful else False
    """
    current = "/data/web_static/current"
    archive_name = os.path.split(archive_path)[1]
    unziped_file_name = archive_name[:archive_name.find(".")]
    unziped_file_path = os.path.join(
        "/data/web_static/releases",
        unziped_file_name)
    if not os.path.isfile(archive_path):
        return False
    if api.put(
            local_path=archive_path,
            remote_path="/tmp",
            use_sudo=True).failed:
        return False
    if api.run("rm -rf {}".format(unziped_file_path)).failed:
        return False
    if api.run("mkdir -p {}".format(unziped_file_path)).failed:
        return False
    if api.run("tar -xzf {} -C {}".format(
        os.path.join("/tmp", archive_name),
        unziped_file_path
    )).failed:
        return False
    if api.run("rm -f /tmp/{}".format(archive_name)).failed:
        return False
    if api.run("rm -f /data/web_static/current").failed:
        return False
    if api.run("mv -f {}/* {}".format(
            os.path.join(unziped_file_path, "web_static"),
            unziped_file_path,
    )).failed:
        return False
    if api.run(
            "rm -rf {}".format(os.path.join(
                unziped_file_path, "web_static"))).failed:
        return False
    if api.run("ln -sf -T {} {}".format(
        unziped_file_path,
        current
    )).failed:
        return False
    return True
