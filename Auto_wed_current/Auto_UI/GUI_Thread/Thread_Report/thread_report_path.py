from time import sleep

from PyQt6.QtCore import QThread, QWaitCondition, QMutex
from PyQt6.QtWidgets import QFileDialog
from Auto_wed_current.Auto_UI.__init__ import property_data

class thread_report_path(QThread, property_data): # 执行开始线程
    def __init__(self):
        super(QThread, self).__init__()
        self.cond = QWaitCondition()
        self.mutex = QMutex()

    def filedialog(self): # 创建文件对话框
        dir = QFileDialog()
        text = dir.getExistingDirectory(None, "选择文件夹路径", 'C:/')  # 选择文件夹位置
        sleep(0.5)
        self.lineEdit_report.setText(text)
        self.lineEdit_report.setToolTip(text)

    def run(self):
        self.mutex.lock()
        self.filedialog()
        self.mutex.unlock()
