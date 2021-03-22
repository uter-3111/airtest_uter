# createtime:2021/3/9 14:52
# user:luoli
# project:airtestProject
import os
import shutil


from airtest.core.helper import G
from airtest.core.settings import Settings as ST
from airtest.utils.compat import script_log_dir

def Only_log(basedir=None, logdir=None):
    if logdir:
        logdir = script_log_dir(basedir, logdir)
        if os.path.exists(logdir):
            shutil.rmtree(logdir)
        os.makedirs(logdir)  # 根据当前文件路径，创建同级log文件夹
        ST.LOG_DIR = logdir
        G.LOGGER.set_logfile(os.path.join(ST.LOG_DIR, ST.LOG_FILE))
        return logdir
