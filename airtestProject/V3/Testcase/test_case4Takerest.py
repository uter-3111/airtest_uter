# createtime:2021/3/10 18:35
# user:luoli
# project:airtestProject

import unittest
from V3.Base.onlylog import Only_log
from V3.Base.Getmethodname import get_methodname
from V3.Base.ExceptionDeclare import BackExceptiondeclare
from V3.Base.Getpoco import Getpoco
from airtest.core.api import *


class TestTakerest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.poco = Getpoco.get_poco()

    def setUp(self) -> None:
        pass

    @BackExceptiondeclare()
    def test_case_Takerest(self):
        self.logpath, self.outputpath = get_methodname(self)
        Only_log(logdir=self.logpath)
        time.sleep(2)
        self.poco(text="作息梦话").click()
        self.poco(text="自定义小憩").click()
        while True:
            if self.poco("android.widget.LinearLayout").child("android.widget.TextView")[1].get_text() != '90':
                self.poco.swipe((0.5, 0.375), (0.5, 0.05))
            else:
                break
        self.poco("com.psyone.brainmusic:id/iv_type_icon").click()
        time.sleep(5)
        self.poco("com.psyone.brainmusic:id/iv_type_icon").click()
        res = self.poco(text="首页").get_text()
        assert_equal(res, "首页", "请填写测试点.")

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
