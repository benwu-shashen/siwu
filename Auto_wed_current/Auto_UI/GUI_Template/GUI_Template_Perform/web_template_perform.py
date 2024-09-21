from Auto_wed_current.Auto_UI.GUI_Error.web_error import web_error
from Auto_wed_current.Auto_UI.GUI_Template.GUI_Template_PushButton.web_template_button import web_template_button
from Auto_wed_current.Auto_UI.GUI_Template.__init__ import tem_property_data
from Auto_wed_current.Auto_UI.GUI_Template.GIU_Template_File.append_file import append_file
from Auto_wed_current.Auto_UI.GUI_Template.GIU_Template_File.delete_file import delete_file
from Auto_wed_current.Auto_UI.GUI_Template.GIU_Template_File.template_show import template_show
from Auto_wed_current.Auto_UI.GUI_Template.GUI_Template_Thread.thread_data_staging import thread_data_staging
from Auto_wed_current.Auto_UI.GUI_Template.GUI_Template_Open_File.template_open_file import template_open_file

class web_perform_func(tem_property_data):
    def __init__(self):
        super().__init__()
        self.pushButton_original_delete.setEnabled(False)
        self.pushButton_replace_delete.setEnabled(False)

        self.tb = web_template_button()
        self.listWidget_original.itemSelectionChanged.connect(
            lambda: self.template_button_del(self.listWidget_original, 'original'))
        self.listWidget_replace.itemSelectionChanged.connect(
            lambda: self.template_button_del(self.listWidget_replace, 'replace'))

        self.af = append_file()
        self.df = delete_file()
        self.te_of = template_open_file()
        self.tempalte_perform_connect()
        self.thread_ds = thread_data_staging()
        self.template_open()
        self.we = web_error()

        self.test = self.test  # 一个bug，需要这样写才会触发信号

    def tempalte_perform_connect(self):
        # 取消和关闭窗口槽函数
        self.pushButton_template_cancel.clicked.connect(self.template_close)

        # 确认按钮函数
        self.pushButton_template_confirm.clicked.connect(self.template_confirm)

        # 原始模板和替换模板模板新增按钮
        self.pushButton_original_append.clicked.connect(self.af.original_file)
        self.pushButton_replace_append.clicked.connect(self.af.replace_file)

        # 原始模板和替换模板删除按钮
        self.pushButton_original_delete.clicked.connect(self.df.original_file)
        self.pushButton_replace_delete.clicked.connect(self.df.replace_file)

        # 原始模板，双击选项，打开选项文件
        self.listWidget_original.doubleClicked.connect(self.template_open_orfile)

        # 替换模板，双击选项，打开选项文件
        self.listWidget_replace.doubleClicked.connect(self.template_open_refile)

    def template_button_del(self, listWidget, template): # 选中时，才会触发删除按钮
        listWidget_data = []
        count = listWidget.count()  # 获取条目数

        if template == 'original':
            self.bt_af = self.tb.template_original_af
            self.bt_bf = self.tb.template_original_bf

        elif template == 'replace':
            self.bt_af = self.tb.template_replace_af
            self.bt_bf = self.tb.template_replace_bf

        for num in range(count):  # 遍历listwidget中的内容
            listWidget_data.append(listWidget.item(num).text())

        for num in range(len(listWidget_data)):
            select = listWidget.item(num).isSelected()
            if select == True:
                self.bt_af()
                break

            elif select == False:
                self.bt_bf()

    def template_open(self):
        thread_data_staging.append_original_list = []  # 用来存新增的虚拟数据地址
        thread_data_staging.append_replace_list = []  # 用来存新增的虚拟数据地址
        thread_data_staging.delete_original_list = []  # 用来存新增的虚拟数据地址
        thread_data_staging.delete_replace_list = []  # 用来存新增的虚拟数据地址

        thread_data_staging.original_dict = {}
        thread_data_staging.replace_dict = {}

        template_show() # 初始页面展示

    def template_close(self):
        value = self.we.box_cancel("是否取消，取消不会保存当前值")
        if value:
            self.pushButton_template_close()

    def template_confirm(self):
        self.thread_ds.start()
        self.pushButton_template_close()
        self.we.box_information("修改成功")

    def template_open_orfile(self):
        self.te_of.open_orfile()

    def template_open_refile(self):
        self.te_of.open_refile()

    def test(self): # 不能删
        pass
