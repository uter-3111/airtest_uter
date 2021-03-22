# createtime:2021/3/10 18:01
# user:luoli
# project:airtestProject
import unittest
from BeautifulReport import BeautifulReport
from V3.Testcase.test_case1DayOrNight import TestDayOrNight
from V3.Testcase.test_case2playmusic import Testplaymusic
from V3.Testcase.test_case3Search import Testsearch
from V3.Testcase.test_case4Takerest import TestTakerest
from V3.Testcase.test_case5sleepceremony import Testsleepceremony
from V3.Base.DIYBeautifulReport import DIYBeautifulReport

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    Testcase1 = unittest.TestLoader().loadTestsFromTestCase(TestDayOrNight)
    # Testcase2 = unittest.TestLoader().loadTestsFromTestCase(Testplaymusic)
    # Testcase3 = unittest.TestLoader().loadTestsFromTestCase(Testsearch)
    # Testcase4 = unittest.TestLoader().loadTestsFromTestCase(TestTakerest)
    # Testcase5 = unittest.TestLoader().loadTestsFromTestCase(Testsleepceremony)
    suite.addTest(Testcase1)
    # suite.addTest(Testcase2)
    # suite.addTest(Testcase3)
    # suite.addTest(Testcase4)
    # suite.addTest(Testcase5)

    # runner = BeautifulReport(suite)
    runner = DIYBeautifulReport(suite)
    runner.report("小睡眠测试报告汇总", "report4.html")
