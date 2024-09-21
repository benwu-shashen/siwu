from PyQt6.QtWidgets import QFileDialog

from Auto_wed_current.Auto_UI.GUI_Error.web_error import web_error
from Auto_wed_current.Auto_UI.GUI_Template.GUI_Template_Thread.thread_data_staging import thread_data_staging
from Auto_wed_current.Auto_UI.GUI_Template.__init__ import tem_property_data

class thread_template_append(tem_property_data): # 执行开始线程
    def __init__(self, listWidget=True, condition=True):
        super().__init__()
        self.listWidget = listWidget # 传入控件
        self.condition = condition # 传入参数，是否是原始模板还是替换模板
        self.we = web_error()

    def filedialog(self): # 创建文件对话框
        dir = QFileDialog()
        dir.setFileMode(QFileDialog.FileMode.ExistingFiles)  # 设置多选
        dir.setDirectory('C:/')  # 设置初始路径为桌面
        dir.setNameFilter('文件(*.xls)') # 只显示xls文件格式

        if dir.exec() == QFileDialog.DialogCode.Accepted:  # 判断是否选择了文件
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
                    self.QMessageBox_error()
                    return

            self.listWidget.addItems(filename_list)

            thread_ds = thread_data_staging()
            thread_ds.append_data(filename_list, self.condition, text = self.text)

    def QMessageBox_error(self):
        self.we.box_warning('选择的文件重名，请重新选择')
