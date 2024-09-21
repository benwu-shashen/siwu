import os

from Auto_wed_current.Auto_UI.GUI_Template.__init__ import tem_property_data
from Auto_wed_current.Auto_base.filename import filename

class template_open_file(tem_property_data):
    def __init__(self):
        super().__init__()
        self.original_dir = filename().filename_func(r'\Auto_file\原始导入excel模板')
        self.replace_dir = filename().filename_func(r'\Auto_file\替换导入excel模板')

    def open_orfile(self):
        text = self.listWidget_original.selectedItems()[0].text()
        os.startfile(self.original_dir + os.sep + text)

    def open_refile(self):
        text = self.listWidget_replace.selectedItems()[0].text()
        os.startfile(self.replace_dir + os.sep + text)


