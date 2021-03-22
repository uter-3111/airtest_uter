# createtime:2021/3/10 17:46
# user:luoli
# project:airtestProject
import unittest
from V3.Base.onlylog import Only_log
from airtest.core.api import *
from V3.Base.Getmethodname import get_methodname
from V3.Base.ExceptionDeclare import DayOrNightExceptiondeclare
from V3.Base.Getpoco import Getpoco


class TestDayOrNight(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.poco = Getpoco.get_poco()

    def setUp(self) -> None:
        pass

    @DayOrNightExceptiondeclare()
    def test_case_DayOrNight(self):
        self.logpath, self.outputpath = get_methodname(self)
        Only_log(logdir=self.logpath)
        time.sleep(2)
        start_app("com.psyone.brainmusic")
        sleep(5)
        self.poco("com.psyone.brainmusic:id/tv_label_report").click()
        self.poco.swipe((0.477, 0.600), (0.477, 0.439))
        self.poco(text="夜间模式").click()
        assert_exists(
            Template(r"../TestData/tpl1615200195815.png", record_pos=(0.125, 0.517), resolution=(720, 1280)),
            "判断是否切换为夜间模式")

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
