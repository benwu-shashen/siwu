from Auto_wed_current.Auto_UI.GUI_Attachment.__init__ import att_property_data

from Auto_wed_current.Auto_UI.GUI_Attachment.GUI_Attachment_PushButton.web_attachment_button import web_attachment_button
from Auto_wed_current.Auto_UI.GUI_Attachment.GUI_Thread_Attachment.thread_data_staging import thread_data_staging
from Auto_wed_current.Auto_UI.GUI_Attachment.GUI_Attachment_File.append_file import append_file
from Auto_wed_current.Auto_UI.GUI_Attachment.GUI_Attachment_File.delete_file import delete_file
from Auto_wed_current.Auto_UI.GUI_Attachment.GUI_Attachment_File.attachment_show import attachment_show


class web_perform_func(att_property_data):
    def __init__(self):
        super().__init__()

        self.pushButton_attachment_delete.setEnabled(False)

        self.bt = web_attachment_button()
        self.listWidget_attachment.itemSelectionChanged.connect(
            lambda: self.attachment_button_del(self.listWidget_attachment))

        self.af = append_file()  # 添加文件
        self.df = delete_file()  # 删除文件
        self.attachment_perform_connect()
        self.thread_ds = thread_data_staging()
        self.attachment_open()

        self.test = self.test  # 一个bug，需要这样写才会触发信号

    def attachment_perform_connect(self):
        # 取消和关闭窗口槽函数
        self.pushButton_attachment_cancel.clicked.connect(self.attachment_close)

        # 确认按钮函数
        self.pushButton_attachment_confirm.clicked.connect(self.attachment_confirm)

        # 附件新增按钮
        self.pushButton_attachment_append.clicked.connect(self.af.attachment_file)

        # 附件删除按钮
        self.pushButton_attachment_delete.clicked.connect(self.df.attachment_file)

    def attachment_button_del(self, listWidget):  # 选中时，才会触发删除按钮
        listWidget_data = []
        count = listWidget.count()  # 获取条目数

        self.bt_af = self.bt.attachment_af  # 未选择数据则隐藏
        self.bt_bf = self.bt.attachment_bf  # 选择数据后则显示

        for num in range(count):  # 遍历listwidget中的内容
            listWidget_data.append(listWidget.item(num).text())

        for num in range(len(listWidget_data)):
            select = listWidget.item(num).isSelected()
            if select == True:
                self.bt_af()
                break

            elif select == False:
                self.bt_bf()

    def attachment_open(self):
        thread_data_staging.append_attachment_list = []  # 用来存新增的虚拟数据地址
        thread_data_staging.delete_attachment_list = []  # 用来存新增的虚拟数据地址

        thread_data_staging.attachment_dict = {}

        attachment_show()  # 初始页面展示

    def attachment_close(self):
        self.pushButton_attachment_close()

    def attachment_confirm(self):
        self.thread_ds.start()
        self.attachment_close()

    def test(self): # 不能删
        pass