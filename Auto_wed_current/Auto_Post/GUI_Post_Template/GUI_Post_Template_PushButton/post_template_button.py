from Auto_wed_current.Auto_Post.GUI_Post_Template import tem_property_data


class post_template_button(tem_property_data):
    def __init__(self):
        super().__init__()

    def template_original_bf(self): # 选择原始模板列表文本之前
        self.pushButton_original_delete.setEnabled(False)

    def template_original_af(self): # 选择原始模板列表文本之后
        self.pushButton_original_delete.setEnabled(True)

