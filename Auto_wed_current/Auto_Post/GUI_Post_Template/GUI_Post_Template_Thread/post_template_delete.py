import os

from Auto_wed_current.Auto_UI.GUI_Error.web_error import web_error
from Auto_wed_current.Auto_UI.GUI_Template.GUI_Template_Thread.thread_data_staging import thread_data_staging
from Auto_wed_current.Auto_UI.GUI_Template.__init__ import tem_property_data
from Auto_wed_current.Auto_base.filename import filename


class post_template_delete(tem_property_data): # 执行开始线程
    def __init__(self, listWidget=True): #
        super().__init__()
        self.listWidget = listWidget
        self.original_dir = filename().filename_func(r'\Auto_file\接口CSV模板')
        self.we = web_error()

    def del_listwidget(self):
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

        for data in filename_list:
            os.remove(self.original_dir + r'\\' + data)

        self.we.box_information("删除完成")
