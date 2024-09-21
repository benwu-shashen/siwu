import sys
import time

from PyQt6 import QtWidgets
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QApplication

from Auto_wed_current.Auto_UI.GUI_Logging.__init__ import log_property_data
from Auto_wed_current.Auto_UI.GUI_Untitled.untitled_logging import Ui_MainWindow_logging
from Auto_wed_current.Auto_UI.GUI_Logging.GUI_Logging_Perform.web_logging_perform import web_perform_func

class web_logging(QtWidgets.QMainWindow, Ui_MainWindow_logging):
    logging_close = pyqtSignal()
    def __init__(self):
        super(web_logging, self).__init__()
        self.setupUi(self)
        self.control_property()

        web_perform_func()

    def control_property(self):  # 所有控件属性
        # 窗口控件
        log_property_data.lineEdit_logging = self.lineEdit_logging  # 标题
        log_property_data.textEdit_logging = self.textEdit_logging  # 窗口

        # 按钮控件
        log_property_data.pushButton_logging_clear = self.pushButton_logging_clear # 清空文本
        log_property_data.pushButton_logging_close = self.pushButton_logging_close # 关闭窗口

        # 关闭窗口
        log_property_data.close = self.close

    def log_windowa_prite(self, error_text):
        write_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.textEdit_logging.append(write_time + '>>>' + error_text)

    def closeEvent(self, event):
        self.logging_close.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = web_logging()
    MainWindow.show()
    sys.exit(app.exec_())