# createtime:2021/3/10 18:37
# user:luoli
# project:airtestProject

import unittest
from V3.Base.onlylog import Only_log
from V3.Base.Getmethodname import get_methodname
from V3.Base.ExceptionDeclare import BackExceptiondeclare
from V3.Base.Getpoco import Getpoco
from airtest.core.api import *
from V3.Base.Createreport import creat_report


class Testsleepceremony(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.poco = Getpoco.get_poco()

    def setUp(self) -> None:
        pass

    @BackExceptiondeclare()
    def test_case5_sleepceremony(self):
        self.logpath, self.outputpath = get_methodname(self)
        Only_log(logdir=self.logpath)
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
        try:
            self.poco(text="下一步").click()
        except:
            pass
        try:
            assert_equal(texts, "开始睡眠", "测试是否进入睡眠模式")
        except Exception as e:
            self.poco.long_click((0.49, 0.729), duration=4)
            time.sleep(30)
            log(e, desc="执行异常")
            print("Error: ", e)
            raise e

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
