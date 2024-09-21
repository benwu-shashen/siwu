from Auto_wed_current.Auto_UI.__init__ import property_data

class web_button_IsEnabled(property_data):
    def __init__(self):
        super().__init__()
        self.set_Enabled_bf()

    def set_Enabled_bf(self): # 未点击开始执行
        self.pushButton_start.setEnabled(True)
        self.pushButton_pause.setEnabled(False)
        self.pushButton_resume.setEnabled(False)
        self.pushButton_end.setEnabled(False)

    def set_Enabled_af(self): # 点击开始执行之后
        self.pushButton_start.setEnabled(False)
        self.pushButton_pause.setEnabled(True)
        self.pushButton_resume.setEnabled(False)
        self.pushButton_end.setEnabled(True)

    def set_Enabled_pa(self): # 点击暂停执行之后
        self.pushButton_start.setEnabled(False)
        self.pushButton_pause.setEnabled(False)
        self.pushButton_resume.setEnabled(True)
        self.pushButton_end.setEnabled(True)

    def set_Enabled_re(self): # 点击继续执行之后
        self.pushButton_start.setEnabled(False)
        self.pushButton_pause.setEnabled(True)
        self.pushButton_resume.setEnabled(False)
        self.pushButton_end.setEnabled(True)

    def template_original_bf(self): # 选择原始模板列表文本之前
        self.pushButton_original_delete.setEnabled(False)

    def template_original_af(self): # 选择原始模板列表文本之后
        self.pushButton_original_delete.setEnabled(True)

    def template_replace_bf(self): # 选择替换模板列表文本之前
        self.pushButton_replace_delete.setEnabled(False)

    def template_replace_af(self): # 选择替换模板列表文本之后
        self.pushButton_replace_delete.setEnabled(True)

    def attachment_bf(self): # 选择附件列表文本之前
        self.pushButton_attachment_delete.setEnabled(False)

    def attachment_af(self): # 选择附件列表文本之后
        self.pushButton_attachment_delete.setEnabled(True)

