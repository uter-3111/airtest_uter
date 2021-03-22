# createtime:2021/3/10 17:50
# user:luoli
# project:airtestProject
from airtest.report.report import simple_report


def creat_report(logpath, output):
    simple_report(__file__, logpath=logpath, output=output)
