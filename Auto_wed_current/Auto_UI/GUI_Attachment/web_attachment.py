import sys

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication

from Auto_wed_current.Auto_UI.GUI_Attachment.__init__ import att_property_data
from Auto_wed_current.Auto_UI.GUI_Untitled.untitled_attachment import Ui_Form_attachment
from Auto_wed_current.Auto_UI.GUI_Attachment.GUI_Attachment_Perform.web_attachment_perform import web_perform_func

class web_attachment(QtWidgets.QMainWindow, Ui_Form_attachment):
    def __init__(self):
        super(web_attachment, self).__init__()
        self.setupUi(self)
        self.control_property()

        web_perform_func()

    def control_property(self):  # 所有控件属性
        # 附件按钮
        att_property_data.pushButton_attachment_close = self.close
        att_property_data.pushButton_attachment_cancel = self.pushButton_attachment_cancel
        att_property_data.pushButton_attachment_confirm = self.pushButton_attachment_confirm

        att_property_data.pushButton_attachment_append = self.pushButton_attachment_append # 添加附件
        att_property_data.pushButton_attachment_delete = self.pushButton_attachment_delete # 删除附件

        # 附件按钮
        att_property_data.listWidget_attachment = self.listWidget_attachment

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = web_attachment()
    MainWindow.show()
    sys.exit(app.exec())
