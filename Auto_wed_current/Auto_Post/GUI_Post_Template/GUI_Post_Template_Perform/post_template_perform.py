from Auto_wed_current.Auto_Post.GUI_Post_Template import tem_property_data
from Auto_wed_current.Auto_Post.GUI_Post_Template.GIU_Post_Template_File.append_file import append_file
from Auto_wed_current.Auto_Post.GUI_Post_Template.GIU_Post_Template_File.delete_file import delete_file
from Auto_wed_current.Auto_Post.GUI_Post_Template.GIU_Post_Template_File.template_show import template_show
from Auto_wed_current.Auto_Post.GUI_Post_Template.GUI_Post_Template_Open_File.template_open_file import \
    template_open_file
from Auto_wed_current.Auto_Post.GUI_Post_Template.GUI_Post_Template_PushButton.post_template_button import \
    post_template_button


class post_perform_func(tem_property_data):
    def __init__(self):
        super().__init__()
        self.pushButton_original_delete.setEnabled(False)

        self.tb = post_template_button()
        self.listWidget_original.itemSelectionChanged.connect(
            lambda: self.template_button_del(self.listWidget_original))

        self.af = append_file()
        self.df = delete_file()
        self.te_of = template_open_file()
        self.tempalte_perform_connect()
        # self.thread_ds = thread_data_staging()
        template_show() # 初始页面展示

        self.test = self.test  # 一个bug，需要这样写才会触发信号

    def tempalte_perform_connect(self):
        # 取消和关闭窗口槽函数
        self.pushButton_template_quit.clicked.connect(self.template_close)

        # 原始模板新增按钮
        self.pushButton_original_append.clicked.connect(self.af.original_file)

        # 原始模板删除按钮
        self.pushButton_original_delete.clicked.connect(self.df.original_file)

        # 原始模板，双击选项，打开选项文件
        self.listWidget_original.doubleClicked.connect(self.template_open_orfile)

    def template_close(self):
        self.pushButton_template_close()


    def template_button_del(self, listWidget): # 选中时，才会触发删除按钮
        listWidget_data = []
        count = listWidget.count()  # 获取条目数

        for num in range(count):  # 遍历listwidget中的内容
            listWidget_data.append(listWidget.item(num).text())

        for num in range(len(listWidget_data)):
            select = listWidget.item(num).isSelected()
            if select == True:
                self.tb.template_original_af()
                break

            elif select == False:
                self.tb.template_original_bf()

    def template_open_orfile(self):
        self.te_of.open_orfile()

    def test(self): # 不能删
        pass
