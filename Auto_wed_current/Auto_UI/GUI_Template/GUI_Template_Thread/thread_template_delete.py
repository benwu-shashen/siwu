from Auto_wed_current.Auto_UI.GUI_Template.GUI_Template_Thread.thread_data_staging import thread_data_staging
from Auto_wed_current.Auto_UI.GUI_Template.__init__ import tem_property_data

class thread_template_delete(tem_property_data): # 执行开始线程
    def __init__(self, listWidget=True, condition=True): #
        super().__init__()
        self.listWidget = listWidget
        self.condition = condition

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

        self.thread_ds = thread_data_staging()
        self.thread_ds.delete_data(filename_list, self.condition)

