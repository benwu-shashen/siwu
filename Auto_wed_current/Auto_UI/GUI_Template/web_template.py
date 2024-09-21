from PyQt6 import QtWidgets

from Auto_wed_current.Auto_UI.GUI_Template.__init__ import tem_property_data
from Auto_wed_current.Auto_UI.GUI_Untitled.untitled_template import Ui_Form_Template
from Auto_wed_current.Auto_UI.GUI_Template.GUI_Template_Perform.web_template_perform import web_perform_func

class web_template(QtWidgets.QMainWindow, Ui_Form_Template):
    def __init__(self):
        super(web_template, self).__init__()
        self.setupUi(self)
        self.control_property()

        web_perform_func()

    def control_property(self):  # 所有控件属性
        # 模板窗口按钮
        tem_property_data.pushButton_template_cancel = self.pushButton_template_cancel  # 取消
        tem_property_data.pushButton_template_confirm = self.pushButton_template_confirm  # 确认

        tem_property_data.pushButton_original_append = self.pushButton_original_append  # 原始模板添加
        tem_property_data.pushButton_original_delete = self.pushButton_original_delete  # 原始模板删除
        tem_property_data.pushButton_replace_append = self.pushButton_replace_append  # 替换模板添加
        tem_property_data.pushButton_replace_delete = self.pushButton_replace_delete  # 替换模板删除

        tem_property_data.pushButton_template_close = self.close  # 关闭函数

        # 模板窗口列表
        tem_property_data.listWidget_original = self.listWidget_original  # 原始模板列表
        tem_property_data.listWidget_replace = self.listWidget_replace  # 替换模板列表

