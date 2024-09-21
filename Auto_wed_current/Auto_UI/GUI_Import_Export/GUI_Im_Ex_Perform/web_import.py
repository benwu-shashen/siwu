from Auto_wed_current.Auto_UI.GUI_Thread.Thead_Import.thread_import import thread_import
from Auto_wed_current.Auto_UI.GUI_Error.web_error import web_error

class web_import:
    def __init__(self):
        self.ti = thread_import()

    def import_csv(self):
        self.import_connext()
        self.ti.import_verify.connect(self.import_information)
        self.ti.start()

    def import_information(self, text):
        web_error().box_warning(text)

    def import_connext(self):
        self.ti.import_append.connect(self.append_line) # 函数取至web_combobox