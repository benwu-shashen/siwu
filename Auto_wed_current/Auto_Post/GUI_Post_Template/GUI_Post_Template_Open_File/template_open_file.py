import os

from Auto_wed_current.Auto_Post.GUI_Post_Template import tem_property_data
from Auto_wed_current.Auto_base.filename import filename

class template_open_file(tem_property_data):
    def __init__(self):
        super().__init__()
        self.original_dir = filename().filename_func(r'\Auto_file\接口CSV模板')

    def open_orfile(self):
        text = self.listWidget_original.selectedItems()[0].text()
        os.startfile(self.original_dir + os.sep + text)