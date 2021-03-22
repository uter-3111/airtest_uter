# createtime:2021/3/10 17:46
# user:luoli
# project:airtestProject
from airtest.cli.parser import cli_setup
import logging
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from V3.Base.onlysetup import Only_setup


class Getpoco():
    poco = None

    def __init__(self):
        pass

    @classmethod
    def get_poco(cls):

        logger = logging.getLogger("airtest")
        logger.setLevel(logging.ERROR)
        if cls.poco is None:
            if not cli_setup():
                Only_setup(__file__, devices=[
                    "android://127.0.0.1:5037/127.0.0.1:62001?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=MINITOUCH", ])
            cls.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        return cls.poco
