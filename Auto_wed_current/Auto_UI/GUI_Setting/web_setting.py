import sys

from PyQt6 import QtWidgets

from Auto_wed_current.Auto_UI.GUI_Setting.__init__ import set_property_data
from Auto_wed_current.Auto_UI.GUI_Untitled.untitled_setting import Ui_Form_setting
from Auto_wed_current.Auto_UI.GUI_Setting.GUI_Setting_Perform.web_setting_perform import web_perform_func
from Auto_wed_current.Auto_driver.driver_class import driver_class

class web_setting(QtWidgets.QMainWindow, Ui_Form_setting):
    def __init__(self):
        super(web_setting, self).__init__()
        self.setupUi(self)
        self.control_property()

        web_perform_func()

    def control_property(self):  # 所有控件属性
        # 浏览器模式选择
        set_property_data.pushButton_normal_mode = self.pushButton_normal_mode
        set_property_data.pushButton_incognito_mode = self.pushButton_incognito_mode

    def closeEvent(self, event):
        driver_class().driver_connect()
