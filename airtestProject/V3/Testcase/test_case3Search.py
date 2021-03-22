# createtime:2021/3/10 18:33
# user:luoli
# project:airtestProject
import unittest
from V3.Base.onlylog import Only_log
from V3.Base.Getmethodname import get_methodname
from V3.Base.ExceptionDeclare import BackExceptiondeclare
from V3.Base.Getpoco import Getpoco
from airtest.core.api import *


class Testsearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.poco = Getpoco.get_poco()

    def setUp(self) -> None:
        pass

    @BackExceptiondeclare()
    def test_case_search(self):
        self.logpath, self.outputpath = get_methodname(self)
        Only_log(logdir=self.logpath)
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

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass
if __name__ == '__main__':
    unittest.main()