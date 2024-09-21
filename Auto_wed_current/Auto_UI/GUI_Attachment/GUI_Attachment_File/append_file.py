from Auto_wed_current.Auto_UI.GUI_Error.web_error import web_error
from Auto_wed_current.Auto_UI.GUI_Attachment.GUI_Thread_Attachment.thread_attachment_append import thread_attachment_append
from Auto_wed_current.Auto_UI.GUI_Attachment.__init__ import att_property_data

class append_file(att_property_data):
    def __init__(self):
        super().__init__()

    def attachment_file(self):
        self.thread = thread_attachment_append(self.listWidget_attachment)
        self.thread.start()
        self.thread.dialog_box.connect(self.QMessageBox_warning)

    def QMessageBox_warning(self):
        web_error().box_warning('选择的文件重名，请重新选择')
