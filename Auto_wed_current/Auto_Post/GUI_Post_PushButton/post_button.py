from Auto_wed_current.Auto_Post.__init__ import post_property_data

class post_button_IsEnabled(post_property_data):
    def __init__(self):
        super().__init__()

    def set_Enabled_bf(self): # 执行完毕
        self.pushButton_post_start.setEnabled(True)

    def set_Enabled_af(self): # 执行中
        self.pushButton_post_start.setEnabled(False)

