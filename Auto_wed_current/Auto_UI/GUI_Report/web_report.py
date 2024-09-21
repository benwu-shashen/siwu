from Auto_wed_current.Auto_UI.GUI_Thread.Thread_Report.thread_report_path import thread_report_path
from Auto_wed_current.Auto_UI.__init__ import property_data
from .report_file.append_file import append_file

class web_report(property_data):
    def __init__(self):
        super().__init__()
        self.tp = thread_report_path()
        self.disable_report()
        self.toolButton_report.clicked.connect(self.select_path)
        self.pushButton_report.clicked.connect(self.state_report)

    def state_report(self):
        text = self.pushButton_report.text()
        if text == '禁用报告':
            self.pushButton_report.setText('启用报告')
            self.lineEdit_report.setVisible(False)
            self.label_report_text.setVisible(False)
            self.toolButton_report.setVisible(False)

        elif text == '启用报告':
            self.pushButton_report.setText('禁用报告')
            self.lineEdit_report.setVisible(True)
            self.label_report_text.setVisible(True)
            self.toolButton_report.setVisible(True)

    def disable_report(self):
        self.pushButton_report.setText('启用报告')
        self.lineEdit_report.setVisible(False)
        self.label_report_text.setVisible(False)
        self.toolButton_report.setVisible(False)

    def select_path(self):
        self.tp.start()

    def report_judge(self):
        perform_result = append_file().report_spanned_file()

        return perform_result