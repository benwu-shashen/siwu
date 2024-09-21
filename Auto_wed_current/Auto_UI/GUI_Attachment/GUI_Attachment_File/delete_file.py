from Auto_wed_current.Auto_UI.GUI_Attachment.GUI_Thread_Attachment.thread_attachment_delete import thread_attachment_delete
from Auto_wed_current.Auto_UI.GUI_Attachment.__init__ import att_property_data


class delete_file(att_property_data):
    def __init__(self):
        super().__init__()

    def attachment_file(self):
        self.thread = thread_attachment_delete(self.listWidget_attachment)
        self.thread.start()
