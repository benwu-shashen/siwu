from PyQt6.QtCore import QThread, QWaitCondition, QMutex, pyqtSignal
from PyQt6.QtWidgets import QFileDialog

from Auto_wed_current.Auto_UI.GUI_Attachment.GUI_Thread_Attachment.thread_data_staging import thread_data_staging
from Auto_wed_current.Auto_UI.GUI_Attachment.__init__ import att_property_data

class thread_attachment_append(QThread, att_property_data): # 执行开始线程
    dialog_box = pyqtSignal()
    def __init__(self, listWidget=True, parent=None):
        super(QThread, self).__init__()
        self.cond = QWaitCondition()
        self.mutex = QMutex()
        self.listWidget = listWidget # 传入控件
        self.judge = ''

    def filedialog(self): # 创建文件对话框
        dir = QFileDialog()
        dir.setFileMode(QFileDialog.FileMode.ExistingFiles)  # 设置多选
        dir.setDirectory('C:/')  # 设置初始路径为桌面
        dir.setNameFilter('文件(*)') # 只显示xls文件格式

        if dir.exec():  # 判断是否选择了文件
            self.text = dir.selectedFiles()
            filename_list = [] # 文件名列表

            for filename in self.text:
                num = int(len(filename) - 1)

                for str in range(len(filename), -1, -1):
                    if filename[str - 1] == '/':
                        filename = filename[num + 1: len(filename)]
                        filename_list.append(filename)
                        break

                    elif filename[str - 1] != '/':
                        num -= 1

            listWidget_data = []
            count = self.listWidget.count() # 获取条目数

            for num in range(count): # 遍历listwidget中的内容
                listWidget_data.append(self.listWidget.item(num).text())

            for filename in filename_list:
                if filename in listWidget_data:
                    self.dialog_box.emit() # 触发文件重复报错
                    self.judge = '导入失败'
                    break

                elif filename not in listWidget_data:
                    self.judge = '导入成功'
                    # 在这里写入数据

            if self.judge == '导入成功':
                self.listWidget.addItems(filename_list)  # 将选择的文件显示在列表中

            elif self.judge == '导入失败':
                pass

            self.thread_ds = thread_data_staging()
            self.thread_ds.append_data(filename_list, text=self.text)

    def run(self):
        self.mutex.lock()
        self.filedialog()
        self.mutex.unlock()
