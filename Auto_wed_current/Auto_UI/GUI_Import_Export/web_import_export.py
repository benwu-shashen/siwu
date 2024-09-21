from .GUI_Im_Ex_Perform.web_export import web_export
from .GUI_Im_Ex_Perform.web_import import web_import

class web_import_export:
    def __init__(self):
        self.we = web_export()
        self.wi = web_import()

    def import_file(self):  # 导入文件
        self.wi.import_csv()

    def export_file(self): # 导出文件
        self.we.export_csv()