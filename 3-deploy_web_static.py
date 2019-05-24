#!/usr/bin/python3
"""Fab file to archive web_static content"""
from os import remove
from os.path import isfile
from fabric.api import *
from datetime import datetime


env.hosts = ['35.245.121.190']


def do_pack():
    """Pack web_static files into archive"""
    try:
        dt = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions/")
        path = local("tar -cvzf versions/tript_{}.tgz tript"
                     .format(dt))
        return "versions/tript_{}.tgz".format(dt)
    except:
        return None


def do_deploy(archive_path):
    """Deploy function for archive to get deployed to servers"""
    if not isfile(archive_path):
        return False
    fileNameExt = archive_path.split('/')[-1]
    fileName = fileNameExt.split(".")[0]
    result = put(archive_path, '/tmp/{}'.format(fileNameExt))
    if result.failed:
        return False
    result = sudo("rm -rf /data/tript/releases/{}/".format(fileName))
    if result.failed:
        return False
    result = sudo("mkdir -p /data/tript/releases/{}/".format(fileName))
    if result.failed:
        return False
    result = sudo("tar -xzf /tmp/{} -C /data/tript/releases/{}/"
                 .format(fileNameExt, fileName))
    if result.failed:
        return False
    result = sudo("rm /tmp/{}".format(fileNameExt))
    if result.failed:
        return False
    input = "mv /data/tript/releases/{}/tript/*\
 /data/tript/releases/{}/".format(fileName, fileName)
    result = sudo(input)
    if result.failed:
        return False
    result = sudo("rm -rf /data/tript/releases/{}/tript"
                 .format(fileName))
    if result.failed:
        return False
    result = sudo("rm -rf /data/tript/current")
    if result.failed:
        return False
    result = sudo("ln -s /data/tript/releases/{}/ /data/tript/current"
                 .format(fileName))
    if result.failed:
        return False
    print("New version deployed!")
    return True


def deploy():
    """Call pack and deploy"""
    path = do_pack()
    if path is None:
        return False
    do_deploy(path)
