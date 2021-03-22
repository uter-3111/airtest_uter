# createtime:2021/3/10 17:58
# user:luoli
# project:airtestProject
import unittest
from V3.Base.onlylog import Only_log
from V3.Base.Getmethodname import get_methodname
from V3.Base.ExceptionDeclare import BackExceptiondeclare
from V3.Base.Getpoco import Getpoco
from airtest.core.api import *


class Testplaymusic(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.poco = Getpoco.get_poco()

    def setUp(self) -> None:
        pass

    @BackExceptiondeclare()
    def test_case_playmusic(self):
        self.logpath, self.outputpath = get_methodname(self)
        Only_log(logdir=self.logpath)
        time.sleep(2)
        self.poco().click((0.49, 0.96))
        time.sleep(2)
        try:
            self.poco(text="雷雨").click()
        except:
            self.poco().click((0.14027, 0.056))
            self.poco(text="雷雨").click()
        time.sleep(2)
        self.poco(text="隐隐春雷").click()
        assert_exists(
            Template(r"../TestData/tpl1615200631156.png", record_pos=(0.015, -0.3), resolution=(720, 1280)),
            "判断播放键是否存在")
        self.poco.click((0.534, 0.33))
        self.poco.click((0.056, 0.056))

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
