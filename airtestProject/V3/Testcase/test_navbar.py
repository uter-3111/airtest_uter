# createtime:2021/3/9 9:57
# user:luoli
# project:airtestProject
# -*- encoding=utf8 -*-
__author__ = "luoli"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import logging
import unittest
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from V3.Base.onlysetup import Only_setup
from V3.Base.onlylog import Only_log
from airtest.report.report import simple_report
from V3.Base.ExceptionDeclare import DayOrNightExceptiondeclare

class TestNavBar(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logger = logging.getLogger("airtest")
        logger.setLevel(logging.ERROR)

        if not cli_setup():
            Only_setup(__file__, devices=[
                "android://127.0.0.1:5037/127.0.0.1:62001?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=MINITOUCH", ])
        cls.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

    def setUp(self) -> None:
        print("start...")

    def get_methodname(self):
        name = self._testMethodName.split('_')[-1]
        path = os.path.dirname(__file__)
        logpath = path + f"/{name}log"
        output = path + f"/Report/{name}.html"
        return logpath, output

    @DayOrNightExceptiondeclare()
    def test_case1_DayOrNight(self):
        try:
            logpath, output = self.get_methodname()
            Only_log(logdir=logpath)
            time.sleep(2)
            start_app("com.psyone.brainmusic")
            sleep(5)
            self.poco("com.psyone.brainmusic:id/tv_label_report").click()
            self.poco.swipe((0.477, 0.600), (0.477, 0.439))
            self.poco(text="夜间模式").click()
            assert_exists(Template(r"../TestData/tpl1615200195815.png", record_pos=(0.125, 0.517), resolution=(720, 1280)),
                          "判断是否切换为夜间模式")
            self.poco(text="日间模式").click()
            self.creat_report(logpath, output)
        except Exception as e:
            log(e, desc="执行异常")
            print("Error: ", e)
            raise e
        finally:
            self.poco("com.psyone.brainmusic:id/tv_label_report").click()
            if self.poco(text="日间模式").exists():
                self.poco(text="日间模式").click()
            else:
                pass

    def test_case2_playmusic(self):
        try:
            logpath, output = self.get_methodname()
            Only_log(logdir=logpath)
            time.sleep(2)
            self.poco("com.psyone.brainmusic:id/img_home_triangle2").click()
            time.sleep(2)
            self.poco(text="雷雨").click()
            time.sleep(2)
            self.poco(text="隐隐春雷").click()
            assert_exists(Template(r"../TestData/tpl1615200631156.png", record_pos=(0.015, -0.3), resolution=(720, 1280)),
                          "判断播放键是否存在")
            self.poco.click((0.534, 0.33))
            self.poco.click((0.056, 0.056))
            self.creat_report(logpath, output)
        except Exception as e:
            log(e, desc="执行异常")
            print("Error: ", e)
            raise e
        finally:
            while not (self.poco(text="首页").exists() and self.poco(text="我的").exists()):
                keyevent("BACK")

    def test_case3_search(self):
        # case3
        try:
            logpath, output = self.get_methodname()
            Only_log(logdir=logpath)
            self.poco.click((0.534, 0.33))
            self.poco.click((0.056, 0.056))
            self.poco(text="首页").click()
            self.poco("com.psyone.brainmusic:id/img_search_float").click()
            text("李沁")
            time.sleep(2)
            self.poco.click((0.093, 0.132))
            time.sleep(2)
            res = self.poco("com.psyone.brainmusic:id/layout_music_brain_decor").offspring(
                "com.psyone.brainmusic:id/rootView").offspring("com.psyone.brainmusic:id/layout_radio").offspring(
                "com.psyone.brainmusic:id/tv_coax_star_name").get_text()
            assert_equal(res, "李沁的哄睡故事", "测试是否打开李沁的哄睡故事")
            self.creat_report(logpath, output)
        except Exception as e:
            log(e, desc="执行异常")
            print("Error: ", e)
            raise e
        finally:
            while not (self.poco(text="首页").exists() and self.poco(text="我的").exists()):
                keyevent("BACK")

    def test_case4_Takerest(self):
        try:
            logpath, output = self.get_methodname()
            Only_log(logdir=logpath)
            time.sleep(2)
            self.poco(text="作息梦话").click()
            self.poco(text="自定义小憩").click()
            while True:
                if self.poco("android.widget.LinearLayout").child("android.widget.TextView")[1].get_text() != '90':
                    self.poco.swipe((0.5, 0.375), (0.5, 0.05))
                else:
                    break
            time.sleep(5)
            res = self.poco("android:id/content").offspring("com.psyone.brainmusic:id/rootView").child(
                "android.widget.LinearLayout").offspring("com.psyone.brainmusic:id/layout_label_noise").offspring(
                "com.psyone.brainmusic:id/tv_label_noise").get_text()
            # assert_equal(res,"首页","判断首页是否返回")
            # print(res)
            assert_equal(res, "首页", "请填写测试点.")
            self.creat_report(logpath, output)
        except Exception as e:
            log(e, desc="执行异常")
            print("Error: ", e)
            raise e
        finally:
            while not (self.poco(text="首页").exists() and self.poco(text="我的").exists()):
                keyevent("BACK")

    def test_case5_sleepceremony(self):
        try:
            logpath, output = self.get_methodname()
            Only_log(logdir=logpath)
            self.poco(text="作息梦话").click()
            self.poco(text="睡前仪式").click()
            self.poco("com.psyone.brainmusic:id/iv_start").click()
            while True:
                if self.poco("com.psyone.brainmusic:id/tv_sleep_prepare_next").get_text() == "进入下一项":
                    self.poco(text="进入下一项").click()
                else:
                    self.poco(text="提前结束").click()
                    break
            texts = self.poco("com.psyone.brainmusic:id/root").child("android.widget.LinearLayout").offspring(
                "com.psyone.brainmusic:id/tv_unlock_button_text_tips").get_text()
            assert_equal(texts, "长按结束", "测试是否进入睡眠模式")
            self.poco.long_click((0.49, 0.729), duration=4)
            time.sleep(30)
            self.creat_report(logpath, output)
        except Exception as e:
            log(e, desc="执行异常")
            print("Error: ", e)
            raise e
        finally:
            while not (self.poco(text="首页").exists() and self.poco(text="我的").exists()):
                keyevent("BACK")

    def creat_report(self, logpath, output):
        simple_report(__file__, logpath=logpath, output=output)

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
