# createtime:2021/3/10 17:52
# user:luoli
# project:airtestProject
import os


def get_methodname(self):
    name = self._testMethodName.split('_')[-1]
    path = os.path.dirname(os.path.dirname(__file__))
    logpath = path + f"/logs/{name}log"
    output = path + f"/Report/{name}.html"
    return logpath, output
