# createtime:2021/3/10 19:08
# user:luoli
# project:airtestProject
import os

from airtest.core.api import connect_device
from airtest.core.settings import Settings as ST
from airtest.core.helper import G


def Only_setup(basedir=None, devices=None, project_root=None, compress=None):
    if basedir:
        if os.path.isfile(basedir):
            basedir = os.path.dirname(basedir)
        if basedir not in G.BASEDIR:
            G.BASEDIR.append(basedir)
    if devices:
        for dev in devices:
            connect_device(dev)
    if project_root:
        ST.PROJECT_ROOT = project_root
    if compress:
        ST.SNAPSHOT_QUALITY = compress
