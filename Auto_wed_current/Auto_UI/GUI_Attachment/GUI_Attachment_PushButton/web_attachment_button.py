from Auto_wed_current.Auto_UI.GUI_Attachment.__init__ import att_property_data

class web_attachment_button(att_property_data):
    def __init__(self):
        super().__init__()

    def attachment_bf(self):  # 选择附件列表文本之前
        self.pushButton_attachment_delete.setEnabled(False)

    def attachment_af(self):  # 选择附件列表文本之后
        self.pushButton_attachment_delete.setEnabled(True)

