# createtime:2021/3/10 16:39
# user:luoli
# project:airtestProject
from airtest.core.api import *
from V3.Base.Createreport import creat_report


def DayOrNightExceptiondeclare():
    def funchandl(func):
        def handle(func_self, *args, **kwargs):
            try:
                func(func_self, *args, **kwargs)
            except Exception as e:
                log(e, desc="执行异常")
                print("Error: ", e, isinstance(e, Exception))
                raise e
            finally:
                strftime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                func_self.__dict__['html_path'] = func_self.outputpath
                func_self.__dict__['start_time'] = strftime
                creat_report(func_self.logpath, func_self.outputpath)
                func_self.poco("com.psyone.brainmusic:id/tv_label_report").click()
                if func_self.poco(text="日间模式").exists():
                    func_self.poco(text="日间模式").click()
                else:
                    pass

        return handle

    return funchandl


def BackExceptiondeclare():
    def funchandl(func):
        def handle(func_self, *args, **kwargs):
            try:
                func(func_self, *args, **kwargs)
            except Exception as e:
                log(e, desc="执行异常")
                print("Error: ", e)
                raise e
            finally:
                strftime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                func_self.__dict__['html_path'] = func_self.outputpath
                func_self.__dict__['start_time'] = strftime
                creat_report(func_self.logpath, func_self.outputpath)
                while not (func_self.poco(text="首页").exists() and func_self.poco(text="我的").exists()):
                    keyevent("BACK")

        return handle

    return funchandl
