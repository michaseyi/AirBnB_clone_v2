#!/usr/bin/python3
"""This modules creates and distributes an archive to web servers
"""
from fabric import api
from datetime import datetime
import os


api.env.user = 'ubuntu'
api.env.hosts = ['34.239.158.102', '18.208.159.79']


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


def deploy():
    """
    deploy creates and distributes an archive to a web server

    :return (bool): is True all operations were successful else
    False
    """
    if deploy.archive_path is None:
        deploy.archive_path = do_pack()
    if deploy.archive_path is None:
        return False
    if not do_deploy(deploy.archive_path):
        return False
    return True


deploy.archive_path = None
