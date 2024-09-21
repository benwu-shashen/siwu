from Auto_wed_current.Auto_UI.GUI_Template.GUI_Template_Thread.thread_template_append import thread_template_append
from Auto_wed_current.Auto_UI.GUI_Template.__init__ import tem_property_data

class append_file(tem_property_data):
    def __init__(self):
        super().__init__()

    def original_file(self):
        condition = '原始模板'
        thread_template_append(self.listWidget_original, condition).filedialog()

    def replace_file(self):
        condition = '替换模板'
        thread_template_append(self.listWidget_original, condition).filedialog()



