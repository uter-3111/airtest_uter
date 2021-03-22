# createtime:2021/3/12 15:17
# user:luoli
# project:airtestProject
import json
import os
import time

from BeautifulReport import BeautifulReport


class DIYBeautifulReport(BeautifulReport, ):
    template_path = os.path.join(os.path.dirname(__file__), '../template')
    config_tmp_path = os.path.join(template_path, 'template.html')

    def __init__(self, suites):
        super(BeautifulReport, self).__init__(suites)
        self.suites = suites
        self.report_dir = None
        self.title = '自动化测试报告'
        self.filename = 'report.html'

    def output_report(self, theme):
        """
            生成测试报告到指定路径下
        :return:
        """

        def render_template(params: dict, template: str):
            for name, value in params.items():
                name = '${' + name + '}'
                template = template.replace(name, value)
            return template

        template_path = self.config_tmp_path
        with open(os.path.join(self.template_path, theme + '.json'), 'r') as theme:
            render_params = {
                **json.load(theme),
                'resultData': json.dumps(self.fields, ensure_ascii=False, indent=4)
            }

        override_path = os.path.abspath(self.report_dir) if \
            os.path.abspath(self.report_dir).endswith('/') else \
            os.path.abspath(self.report_dir) + '/'

        with open(template_path, 'rb') as file:
            body = file.read().decode('utf-8')
        with open(override_path + self.filename, 'w', encoding='utf-8', newline='\n') as write_file:
            html = render_template(render_params, body)
            write_file.write(html)

    @staticmethod
    def get_testcase_property(test) -> tuple:
        """
            接受一个test, 并返回一个test的class_name, method_name, method_doc,html_path属性
        :param test:
        :return: (class_name, method_name, method_doc,html_path) -> tuple
        """
        class_name = test.__class__.__qualname__
        method_name = test.__dict__['_testMethodName']
        method_doc = test.__dict__['_testMethodDoc']
        html_path = test.__dict__['html_path']
        start_time = test.__dict__['start_time']
        return class_name, method_name, method_doc, html_path, start_time

    def stopTestRun(self, title=None) -> dict:
        """
            所有测试执行完成后, 执行该方法
        :param title:
        :return:
        """
        self.fields['testPass'] = self.success_counter
        for item in self.result_list:
            item = json.loads(str(DIYMakeResultJson(item)))
            self.fields.get('testResult').append(item)
        self.fields['testAll'] = len(self.result_list)
        self.fields['testName'] = title if title else self.default_report_name
        self.fields['testFail'] = self.failure_count
        self.fields['beginTime'] = self.begin_time
        end_time = int(time.time())
        start_time = int(time.mktime(time.strptime(self.begin_time, '%Y-%m-%d %H:%M:%S')))
        self.fields['totalTime'] = str(end_time - start_time) + 's'
        self.fields['testError'] = self.error_count
        self.fields['testSkip'] = self.skipped
        return self.fields


class DIYMakeResultJson:
    """ make html table tags """

    def __init__(self, datas: tuple):
        """
        init self object
        :param datas: 拿到所有返回数据结构
        """
        self.datas = datas
        self.result_schema = {}

    def __setitem__(self, key, value):
        """

        :param key: self[key]
        :param value: value
        :return:
        """
        self[key] = value

    def __repr__(self) -> str:
        """
            返回对象的html结构体
        :rtype: dict
        :return: self的repr对象, 返回一个构造完成的tr表单
        """
        keys = (
            'className',
            'methodName',
            'description',
            'html_path',
            'start_time',
            'spendTime',
            'status',
            'log',
        )
        for key, data in zip(keys, self.datas):
            self.result_schema.setdefault(key, data)
        return json.dumps(self.result_schema)
