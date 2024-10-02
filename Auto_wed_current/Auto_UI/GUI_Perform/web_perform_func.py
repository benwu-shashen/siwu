from PyQt6.QtWidgets import QApplication

from Auto_wed_current.Auto_Post.post_window import post_window
from Auto_wed_current.Auto_UI.GUI_Attachment.web_attachment import web_attachment
from Auto_wed_current.Auto_UI.GUI_ComboBox.web_combobox import web_combobox
from Auto_wed_current.Auto_UI.GUI_Download_template.web_download_template import web_download_template
from Auto_wed_current.Auto_UI.GUI_Edit.web_edit_print import web_edit_print
from Auto_wed_current.Auto_UI.GUI_Error.web_error import web_error
from Auto_wed_current.Auto_UI.GUI_PushButton.web_button import web_button_IsEnabled
from Auto_wed_current.Auto_UI.GUI_Report.web_report import web_report
from Auto_wed_current.Auto_UI.GUI_Template.GUI_Template_Perform import web_template_perform
from Auto_wed_current.Auto_UI.GUI_Template.web_template import web_template
from Auto_wed_current.Auto_UI.GUI_Thread.web_thread import execute_thread
from Auto_wed_current.Auto_UI.__init__ import property_data
from Auto_wed_current.Auto_base.error_reminder import error_reminder
from Auto_wed_current.Auto_UI.GUI_Setting.web_setting import web_setting
from PyQt6.QtCore import Qt
from Auto_wed_current.Auto_driver.driver_class import driver, driver_class
from Auto_wed_current.Auto_UI.GUI_Logging.web_logging import web_logging
from Auto_wed_current.Auto_UI.GUI_Import_Export.web_import_export import web_import_export

class web_perform_func(property_data):
    """
    报错初始化
    """
    def __init__(self):
        super().__init__()
        error_reminder.perform_error = self.perform_error
        self.bt = web_button_IsEnabled() # 按钮控制是否显示
        self.ep = web_edit_print() # 执行过程文本展示
        self.cb = web_combobox() # 初始化行数，默认添加一行，初始化选项数据
        self.cw = self.cb.cw # 获取当前csv内存数据
        web_template_perform.web_perform_func.cb = self.cb
        self.tp = web_template()  # 编辑模板
        self.wr = web_report() # 测试报告函数
        self.we = web_error() # 报错函数
        self.lw = web_logging() # 启用日志
        self.ie = web_import_export() # 导入和导出

        self.pw_bool = False

        self.perform_connect()

        # 新窗口函数
        self.ps = web_setting()  # 参数设置窗口

        self.wa = web_attachment()  # 上传附件

        self.log_print = '关闭打印'

        driver.mode = '启动正常模式'
        driver()
        driver_class().driver_connect()

    def perform_connect(self):
        """
        开始执行、暂停执行、继续执行、结束执行信号触发
        :return:
        """
        self.pushButton_start.clicked.connect(self.perform_start) # 开始执行
        self.pushButton_pause.clicked.connect(self.perform_pause)
        self.pushButton_resume.clicked.connect(self.perform_resume)
        self.pushButton_end.clicked.connect(self.perform_end)
        self.pushButton_edit_template.clicked.connect(self.edit_template)  # 点击编辑模板，取至web_qt_gui
        self.pushButton_edit_attachment.clicked.connect(self.edit_attachment) # 点击编辑附件，取至web_qt_gui
        self.pushButton_clear_text.clicked.connect(self.ep.clear_text) # 清空文本
        self.pushButton_parameter_setting.clicked.connect(self.setting_window) # 点击参数设置
        self.pushButton_logging.clicked.connect(self.logging_window) # 点击启用日志
        self.pushButton_import.clicked.connect(self.ie.import_file)
        self.pushButton_export.clicked.connect(self.ie.export_file)
        self.pushButton_post.clicked.connect(self.open_interface) # 接口测试

        self.lw.logging_close.connect(self.logging_close_signal) # 日志窗口打印判断条件

    def perform_start(self):  # 点击开始执行
        perform_result, csv_file = self.cw.csv_data_write()
        if not perform_result:
            return

        # 该功能后面再调整，这个是报告的功能
        # text = self.pushButton_report.text()
        # if text == '禁用报告':
        #     report_result = self.wr.report_judge()
        #
        # elif text == '启用报告':
        #     report_result = '执行报告'
        #
        # if report_result == '执行报告':
        #     for file in csv_file:
        #         del self.csv_file_all[0]
        #         if file in self.csv_file_all:
        #             perform_result = '执行失败_01'
        #
        #         elif file not in self.csv_file_all:
        #             pass
        #
        # elif report_result != '执行报告':
        #     perform_result = '执行失败_01'

        self.execute = execute_thread()

        self.execute.text_Edit.connect(self.ep.Edit)
        self.execute.text_Edit_summary.connect(self.ep.Edit_summary)
        self.execute.text_Edit_logging.connect(self.logging_text)
        self.execute.set_Enabled_bf.connect(self.bt.set_Enabled_bf)
        self.execute.set_Enabled_af.connect(self.bt.set_Enabled_af)
        self.execute.set_Enabled_pa.connect(self.bt.set_Enabled_pa)
        self.execute.set_Enabled_re.connect(self.bt.set_Enabled_re)

        self.execute.start()
        self.bt.set_Enabled_bf()  # 结束程序按钮展示

    def perform_pause(self):
        self.execute.pause()

    def perform_resume(self):
        self.execute.resume()

    def perform_end(self):
        self.execute.terminate()
        self.bt.set_Enabled_bf()

    def perform_error(self, text):
        self.ep.Edit_error(text)

    def setting_window(self):
        self.ps.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.ps.show()

    def edit_template(self):
        self.tp.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.tp.show()

    def edit_attachment(self):
        self.wa.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.wa.show()

    def open_interface(self):
        self.pw = post_window()  # 打开接口窗口
        self.pw.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.pw.show()


    def logging_window(self):
        self.log_print = '启用打印'
        self.lw.show()

    def logging_text(self, error_text):
        """
        日志线程
        :param error_text:
        :return:
        """
        if self.log_print == '启用打印':
            self.lw.log_windowa_prite(error_text)

        elif self.log_print == '关闭打印':
            pass

    def logging_close_signal(self):
        self.log_print = '关闭打印'