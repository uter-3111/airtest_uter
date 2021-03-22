# -*- encoding=utf8 -*-
__author__ = "luoli"

from airtest.core.api import *

auto_setup(__file__)


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

poco("com.psyone.brainmusic:id/img_home_triangle2").click()

poco("com.psyone.brainmusic:id/iv_type_icon").click()
poco("com.psyone.brainmusic:id/iv_type_icon").click()
