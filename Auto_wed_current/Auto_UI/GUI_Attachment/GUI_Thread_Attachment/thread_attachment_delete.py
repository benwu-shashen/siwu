from PyQt6.QtCore import QThread, QWaitCondition, QMutex

from Auto_wed_current.Auto_UI.GUI_Attachment.GUI_Thread_Attachment.thread_data_staging import thread_data_staging
from Auto_wed_current.Auto_UI.GUI_Attachment.__init__ import att_property_data


class thread_attachment_delete(QThread, att_property_data): # 执行开始线程
    def __init__(self, listWidget=True, condition=True, parent=None):
        super(QThread, self).__init__()
        self.cond = QWaitCondition()
        self.mutex = QMutex()
        self.listWidget = listWidget
        self.condition = condition

    def del_listwidget(self): # 创建文件对话框
        listwidget_data = []
        listwidget_count = []
        filename_list = []
        count = self.listWidget.count()  # 获取条目数

        for num in range(count):  # 遍历listwidget中的内容
            listwidget_data.append(self.listWidget.item(num).text())

        for num in range(len(listwidget_data)):
            select = self.listWidget.item(num).isSelected()
            if select == True:
                listwidget_count.append(num)

            elif select == False:
                pass

        for num in listwidget_count: # 获取要被删除的文件名
            filename_list.append(self.listWidget.item(num).text())

        listwidget_count.reverse()

        for num in listwidget_count:
            self.listWidget.takeItem(num)

        self.thread_ds = thread_data_staging()
        self.thread_ds.delete_data(filename_list)

    def run(self):
        self.mutex.lock()
        self.del_listwidget()
        self.mutex.unlock()
