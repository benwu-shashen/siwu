import shutil

from PyQt6.QtWidgets import QFileDialog

from Auto_wed_current.Auto_Post.GUI_Post_Template import tem_property_data
from Auto_wed_current.Auto_UI.GUI_Error.web_error import web_error
from Auto_wed_current.Auto_base.filename import filename

class post_template_append(tem_property_data): # 执行开始线程
    def __init__(self, listWidget=True):
        super().__init__()
        self.listWidget = listWidget # 传入控件
        self.we = web_error()
        self.filename_original = filename().filename_func(r'\Auto_file\接口CSV模板')


    def filedialog(self): # 创建文件对话框
        dir = QFileDialog()
        dir.setFileMode(QFileDialog.FileMode.ExistingFiles)  # 设置多选
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
                filename_list.append(filename.replace('.xls', '.csv'))
                filename_list.remove(filename)
                if filename in listWidget_data:
                    self.QMessageBox_error()
                    return

            self.listWidget.addItems(filename_list)

            for data in self.text:  # 替换模板文件复制函数
                shutil.copy(data, self.filename_original)

            self.we.box_information("导入完成")

    def QMessageBox_error(self):
        self.we.box_warning('选择的文件重名，请重新选择')
