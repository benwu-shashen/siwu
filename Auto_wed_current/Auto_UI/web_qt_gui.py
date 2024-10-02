import os
import sys

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox

from Auto_wed_current.Auto_UI.GUI_ComboBox.web_combobox import web_combobox
from Auto_wed_current.Auto_UI.GUI_Download_template.web_download_template import web_download_template
from Auto_wed_current.Auto_UI.GUI_Logging.web_logging_func import wed_logging
from Auto_wed_current.Auto_UI.GUI_Perform.web_perform_func import web_perform_func
from Auto_wed_current.Auto_UI.GUI_Template.GUI_Template_Perform import web_template_perform
from Auto_wed_current.Auto_UI.GUI_Untitled.untitled import Ui_MainWindow
from Auto_wed_current.Auto_UI.__init__ import property_data
from Auto_wed_current.Auto_driver.driver_class import driver_class

"""
打包命令：Pyinstaller -F -w web_qt_gui.py
"""

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.control_property()  # 赋值按钮控件函数

        self.dt = web_download_template()  # 模板下载
        self.cb = web_combobox()  # 初始化行数，默认添加一行，初始化选项数据
        self.cw = self.cb.cw  # 获取当前csv内存数据
        web_template_perform.web_perform_func.cb = self.cb
        # self.tp = web_template()  # 编辑模板

        self.perform_connect() # 信号连接
        web_perform_func()
        wed_logging()

    def closeEvent(self, event):
        messageBox = QMessageBox()
        messageBox.setIcon(QMessageBox.Icon.Question)  # 设置图标
        messageBox.setWindowTitle('关闭GUI')  # 设置标题
        messageBox.setText('是否关闭GUI程序')  # 设置内容
        messageBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)  # 设置按钮
        buttonY = messageBox.button(QMessageBox.StandardButton.Yes)
        buttonN = messageBox.button(QMessageBox.StandardButton.No)
        buttonY.setText('确定')
        buttonN.setText('取消')
        messageBox.exec()

        # 关闭软件，顺便关闭进程
        if messageBox.clickedButton() == buttonY:
            event.accept()
            driver = driver_class().driver_Chrome('account_01')
            driver.close()
            os.system('taskkill /im chromedriver.exe /F')

        elif messageBox.clickedButton() == buttonN:
            event.ignore()

    def perform_connect(self):
        self.pushButton_download_template.clicked.connect(self.dt.download_file)  # 点击模板下载，取至web_qt_gui
        # self.pushButton_edit_template.clicked.connect(self.edit_template)  # 点击编辑模板，取至web_qt_gui

    def control_property(self): # 所有控件属性
        # 按钮控件
        property_data.pushButton_start = self.pushButton_start # 开始执行
        property_data.pushButton_pause = self.pushButton_pause # 暂停执行
        property_data.pushButton_resume = self.pushButton_resume # 继续执行
        property_data.pushButton_end = self.pushButton_end # 结束执行
        property_data.pushButton_edit_template = self.pushButton_edit_template # 编辑模板
        property_data.pushButton_download_template = self.pushButton_download_template # 下载模板
        property_data.pushButton_edit_attachment = self.pushButton_edit_attachment # 编辑附件

        # 打印窗口控件
        property_data.textEdit = self.textEdit

        # 新增行，删除行表单
        property_data.frame_box = self.frame_box

        # 报告模块控件
        property_data.lineEdit_report = self.lineEdit_report # 地址文本
        property_data.label_report_text = self.label_report_text # 地址标题
        property_data.toolButton_report = self.toolButton_report # 选择控件
        property_data.pushButton_report = self.pushButton_report  # 报告按钮

        # 清空文本
        property_data.pushButton_clear_text = self.pushButton_clear_text

        # 参数设置
        property_data.pushButton_parameter_setting = self.pushButton_parameter_setting

        # 启动日志
        property_data.pushButton_logging = self.pushButton_logging

        # 导入和导出
        property_data.pushButton_import = self.pushButton_import
        property_data.pushButton_export = self.pushButton_export

        # 打开接口窗口
        property_data.pushButton_post = self.pushButton_post

    # def edit_template(self):
    #     self.tp.setWindowModality(Qt.WindowModality.ApplicationModal)
    #     self.tp.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())


