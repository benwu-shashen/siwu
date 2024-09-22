import sys

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox

from Auto_wed_current.Auto_Post.GUI_Post_Perform.post_perform import post_perform_func
from Auto_wed_current.Auto_Post.__init__ import post_property_data
from Auto_wed_current.Auto_Post.GUI_Post_Untitled.untitled_post import Ui_MainWindow_Post
class post_window(QtWidgets.QMainWindow, Ui_MainWindow_Post):
    def __init__(self):
        super(post_window, self).__init__()
        self.setupUi(self)
        self.control_property()

        post_perform_func()

    def control_property(self):  # 所有控件属性
        post_property_data.pushButton_post_close = self.close

        post_property_data.pushButton_post_start = self.pushButton_post_start # 测试
        post_property_data.pushButton_download_template = self.pushButton_download_template # 下载模板
        post_property_data.pushButton_edit_template = self.pushButton_edit_template  # 编辑模板
        post_property_data.tableWidget_preview = self.tableWidget_preview # 表格
        post_property_data.pushButton_post_preview = self.pushButton_post_preview # 预览

    def closeEvent(self, event):
        messageBox = QMessageBox()
        messageBox.setIcon(QMessageBox.Icon.Question)  # 设置图标
        messageBox.setWindowTitle('关闭GUI')  # 设置标题
        messageBox.setText('是否关闭接口程序')  # 设置内容
        messageBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)  # 设置按钮
        buttonY = messageBox.button(QMessageBox.StandardButton.Yes)
        buttonN = messageBox.button(QMessageBox.StandardButton.No)
        buttonY.setText('确定')
        buttonN.setText('取消')

        messageBox.exec()

        if messageBox.clickedButton() == buttonY:
            event.accept()

        elif messageBox.clickedButton() == buttonN:
            event.ignore()