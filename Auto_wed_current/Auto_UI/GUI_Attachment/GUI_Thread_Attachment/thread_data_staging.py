from PyQt6.QtCore import QThread, QWaitCondition, QMutex

from Auto_wed_current.Auto_UI.GUI_Attachment.GUI_Attachment_Data_Staging.data_staging import data_staging
from Auto_wed_current.Auto_UI.GUI_Attachment.__init__ import att_property_data

class thread_data_staging(QThread, att_property_data): # 执行开始线程
    def __init__(self, parent=None):
        super(QThread, self).__init__()
        self.cond = QWaitCondition()
        self.mutex = QMutex()

    def append_data(self, filename_list, text=None):
        filename_dict_staging = dict(zip(filename_list, text))
        for data in filename_list:
            if data not in self.append_attachment_list: # 是否在新增模板里面
                self.append_attachment_list.append(data)

            elif data in self.append_attachment_list:
                del filename_dict_staging[data]
                filename_list.remove(data)

        self.attachment_dict.update(filename_dict_staging)

    def delete_data(self, filename_list):
        for data in filename_list:
            if data in self.initial_attachment_list:
                self.delete_attachment_list.append(data)

            elif data not in self.initial_attachment_list:
                pass

            if data in self.append_attachment_list:
                self.append_attachment_list.remove(data)
                del self.attachment_dict[data]

            elif data not in self.append_attachment_list:
                pass

    def run(self):
        self.mutex.lock()
        self.ds = data_staging(
            self.append_attachment_list,
            self.attachment_dict,
            self.delete_attachment_list,
        )
        self.ds.file_update()
        self.mutex.unlock()