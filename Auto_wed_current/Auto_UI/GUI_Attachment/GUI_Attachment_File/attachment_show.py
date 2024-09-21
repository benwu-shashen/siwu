import os

from PyQt6 import QtWidgets

from Auto_wed_current.Auto_UI.GUI_Attachment.GUI_Thread_Attachment.thread_data_staging import thread_data_staging
from Auto_wed_current.Auto_UI.GUI_Attachment.__init__ import att_property_data
from Auto_wed_current.Auto_base.filename import filename


class attachment_show(att_property_data):
    def __init__(self):
        super().__init__()
        self.filename_show()

    def filename_show(self):
        files_attachment = []

        self.listWidget_attachment.clear()

        filename_attachment = filename().filename_func(r'\Auto_file\上传附件')

        for (root, dirs, file) in os.walk(filename_attachment):  # 附件列表展示
            files_attachment = file

        for dict in files_attachment:
            self.item = QtWidgets.QListWidgetItem(self.listWidget_attachment)  # 创建列表项
            self.item.setText(dict)  # 设置项文本
            self.item.setToolTip(dict)

        thread_data_staging.initial_attachment_list = files_attachment # 初始附件列表数据
        thread_data_staging.delete_attachment_list = [] # 要被删除的模板列表
