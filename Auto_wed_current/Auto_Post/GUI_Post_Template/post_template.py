from PyQt6 import QtWidgets

from Auto_wed_current.Auto_Post.GUI_Post_Template import tem_property_data
from Auto_wed_current.Auto_Post.GUI_Post_Template.GUI_Post_Template_Perform.post_template_perform import \
    post_perform_func
from Auto_wed_current.Auto_Post.GUI_Post_Untitled.untitled_post_template import Ui_Form_Template


class post_template(QtWidgets.QMainWindow, Ui_Form_Template):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.control_property()

        post_perform_func()

    def control_property(self):  # 所有控件属性
        # 模板窗口按钮
        tem_property_data.pushButton_original_append = self.pushButton_original_append  # 原始模板添加
        tem_property_data.pushButton_original_delete = self.pushButton_original_delete  # 原始模板删除

        tem_property_data.pushButton_template_quit = self.pushButton_template_quit # 退出窗口
        tem_property_data.pushButton_template_close = self.close  # 关闭函数

        # 模板窗口列表
        tem_property_data.listWidget_original = self.listWidget_original  # 原始模板列表


