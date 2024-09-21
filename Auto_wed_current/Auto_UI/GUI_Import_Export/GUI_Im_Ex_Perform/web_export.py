from Auto_wed_current.Auto_UI import property_data
from Auto_wed_current.Auto_UI.GUI_Thread.Thread_Export.thread_export import thread_export
from Auto_wed_current.Auto_UI.GUI_Error.web_error import web_error

class web_export(property_data):
    def super(self):
        self.te = thread_export()

    def export_csv(self):
        self.te.export_tips.connect(self.export_information)
        self.te.control_dict = self.control_dict # 来自web_combobox
        self.te.start()

    def export_information(self, text):
        web_error().box_information(text)