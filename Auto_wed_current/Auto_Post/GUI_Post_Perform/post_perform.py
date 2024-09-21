import csv

from PyQt6.QtWidgets import QTableWidgetItem

from Auto_wed_current.Auto_Post.GUI_Post_Download_template.post_download_template import post_download_template
from Auto_wed_current.Auto_Post.GUI_Post_PushButton.post_button import post_button_IsEnabled
from Auto_wed_current.Auto_Post.GUI_Post_Thread.post_thread import execute_thread
from Auto_wed_current.Auto_Post.__init__ import post_property_data
from Auto_wed_current.Auto_base.filename import filename


class post_perform_func(post_property_data):
    def __init__(self):
        super().__init__()

        self.post_tableWidget_setting()
        self.dt = post_download_template()  # 模板下载
        self.et = execute_thread()
        self.bt = post_button_IsEnabled()

        self.post_perform_connect()

        self.test = self.test  # 一个bug，需要这样写才会触发信号

    def post_perform_connect(self):
        self.pushButton_post_start.clicked.connect(self.post_start)
        self.pushButton_download_template.clicked.connect(self.dt.download_file)  # 点击模板下载，取至web_qt_gui

        self.pushButton_post_preview.clicked.connect(self.post_tableWidget_preview) # 预览数据

        self.et.set_Enabled_bf.connect(self.bt.set_Enabled_bf)
        self.et.set_Enabled_af.connect(self.bt.set_Enabled_af)

    def post_tableWidget_setting(self):
        self.tableWidget_preview.setHorizontalHeaderLabels([
    "测试编号", "测试名称", "请求类型", "请求url",
    "请求参数", "响应码", "响应参数", "结果", "说明"
])

    def post_tableWidget_preview(self): # 填充数据
        self.tableWidget_preview.setRowCount(0)  # 清空所有行
        path = filename().filename_func(r'\Auto_file\接口CSV模板\接口模板.csv')
        with open(path, 'r', newline='', encoding='gbk') as f:
            csv_reader = csv.reader(f)
            next(csv_reader)  # 跳过第一行
            for row in csv_reader:
                row_position = self.tableWidget_preview.rowCount()
                self.tableWidget_preview.insertRow(row_position)

                for col, item in enumerate(row):
                    self.tableWidget_preview.setItem(row_position, col, QTableWidgetItem(item))

    def post_start(self):
        self.et.start()
        # r = requests.get('http://jsonplaceholder.typicode.com/posts')
        # print(r.status_code)
        # print(r.json())
    # def attachment_button_del(self, listWidget):  # 选中时，才会触发删除按钮
    #     listWidget_data = []
    #     count = listWidget.count()  # 获取条目数
    #
    #     self.bt_af = self.bt.attachment_af  # 未选择数据则隐藏
    #     self.bt_bf = self.bt.attachment_bf  # 选择数据后则显示
    #
    #     for num in range(count):  # 遍历listwidget中的内容
    #         listWidget_data.append(listWidget.item(num).text())
    #
    #     for num in range(len(listWidget_data)):
    #         select = listWidget.item(num).isSelected()
    #         if select == True:
    #             self.bt_af()
    #             break
    #
    #         elif select == False:
    #             self.bt_bf()
    #
    # def attachment_open(self):
    #     thread_data_staging.append_attachment_list = []  # 用来存新增的虚拟数据地址
    #     thread_data_staging.delete_attachment_list = []  # 用来存新增的虚拟数据地址
    #
    #     thread_data_staging.attachment_dict = {}
    #
    #     attachment_show()  # 初始页面展示
    #
    # def attachment_close(self):
    #     self.pushButton_attachment_close()
    #
    # def attachment_confirm(self):
    #     self.thread_ds.start()
    #     self.attachment_close()
    #
    def test(self): # 不能删
        pass