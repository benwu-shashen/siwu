from PyQt5.QtCore import pyqtSignal, QObject
from Auto_wed_current.Auto_UI.GUI_Logging.__init__ import log_property_data


class web_logging_edit(QObject, log_property_data):
    text_Edit = pyqtSignal()
    def __init__(self):
        super().__init__()

    def logging_emit(self):
        self.textEdit_logging.setPlainText('你好')
        # self.text_Edit.emit()
        # print('测试1')

        # self.textEdit_logging.setText(traceback)
        # if self.state == '启动日志':
        #     self.textEdit_logging.setText(traceback)
        #
        # elif self.state == '关闭日志':
        #     pass
