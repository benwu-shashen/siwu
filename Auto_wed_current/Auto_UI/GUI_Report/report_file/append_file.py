import shutil

from Auto_wed_current.Auto_UI.GUI_Error.web_error import web_error
from Auto_wed_current.Auto_UI.__init__ import property_data
from .report_html import report_html

class append_file(property_data):
    def __init__(self):
        super().__init__()

    def report_spanned_file(self):
        # 会执行report_html函数，返回文件名，这里主要是移动文件到保存的路径
        path = self.lineEdit_report.text()
        if path == '':
            self.QMessageBox_warning()
            self.report_result = ''

        elif path != '':
            self.report_result = '执行报告'

        return self.report_result

    def report_create_html(self, total_result):
        path = self.lineEdit_report.text()
        if path == '':
            pass

        elif path != '':
            html_name = report_html().create_html(total_result)
            shutil.move(html_name, path)

    def QMessageBox_warning(self):
        web_error().box_warning('请选择测试报告存储路径')