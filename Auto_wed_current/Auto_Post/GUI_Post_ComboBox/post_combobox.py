import csv

from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *

from Auto_wed_current.Auto_Post.GUI_Post_CSV.post_csv_write import post_csv_write
from Auto_wed_current.Auto_Post.__init__ import post_property_data
from Auto_wed_current.Auto_Post.GUI_Post_ComboBox.post_combobox_file import post_combobox_file
from Auto_wed_current.Auto_base.filename import filename


class post_combobox(post_property_data):
    def __init__(self):
        super().__init__()
        self.path = filename().filename_func(r'\Auto_file\接口CSV模板')
        self.topFiller = QWidget()
        self.num = 0
        self.scroll = QScrollArea()
        self.scroll.setWidget(self.topFiller)  # 设置一个Layout用于放ScrollArea，等同于放了所有的控件
        self.scroll.widget().resize(800, 250)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # 设置x轴滚动条不显示
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.scroll)
        self.frame_box.setLayout(self.vbox)  # 最后就是将结果在设置的显示区进行显示

        self.title_labels = {} #这个存放标题每一个Lab组件

        self.control_dict = {}  # 所有控件的字典
        self.control_groove = {} # 所有控件的槽

        self.current_del_line = -1 # 当前删除行

        self.pf = post_combobox_file()
        self.cw = post_csv_write() # 获取cs目录
        self.append_title()
        self.append_line()

    def location_size(self, dir, key, num):
        """
        调整每个控件宽度
        :param dir:
        :param key:
        :param num:
        :return:
        """
        if 'box_file' in key:
            dir[key].setGeometry(QtCore.QRect(0, 0, 80, 22))

        elif 'bu_add'.format(num) in key:
            dir[key].setGeometry(QtCore.QRect(0, 0, 75, 22))

        elif 'bu_del'.format(num) in key:
            dir[key].setGeometry(QtCore.QRect(0, 0, 75, 22))

        elif 'bu_preview'.format(num) in key:
            dir[key].setGeometry(QtCore.QRect(0, 0, 75, 22))

    def append_move(self, key, control_dict_loacls):
        """
        移动调整每一个列表数据
        :param key:
        :return:
        """
        y = self.num * 30 + 10# 首行为10px，所以不相乘，加10，因此减1
        if 'box_file' == key:
            control_dict_loacls[key].move(10, y)

        elif 'bu_add'== key:
            control_dict_loacls[key].move(300, y)

        elif 'bu_del' == key:
            control_dict_loacls[key].move(380, y)

        elif 'bu_preview' == key:
            control_dict_loacls[key].move(460, y)

    def delete_move(self, key, delete_line):
        """
        删除时，复位每一条数据
        :param key:
        :param delete_line:
        :return:
        """
        num_y = delete_line  # 首行为10px，所以不相乘，加10，因此减1
        y = num_y * 30 + 10
        if 'box_file' in key:
            self.control_dict[delete_line][key].move(10, y)

    def append_title(self):
        """
        标题文字
        :return:
        """
        con = ['title_file', 'title_handle']
        for i in con:
            self.title_labels[i] = QLabel(self.topFiller)

        for i in con:
            if 'title_file' == i:
                self.title_labels[i].setText('模板')
                self.title_labels[i].move(10, 10)

            elif 'title_handle' == i:
                self.title_labels[i].setText('操作')
                self.title_labels[i].move(300, 10)

    def append_signal_trigger(self, line): # 新增时，触发信号
        """
        新增时，添加每个控件槽信号
        :return:
        """
        control_groove_locals = {}
        for i in self.control_dict[line]:
            if 'bu_add' in i:
                self.control_dict[line][i].clicked.connect(self.append_line)

            elif 'bu_del' in i:
                control_locals = self.control_dict[line][i]
                control_groove_locals[i + 'test'] = lambda: self.delete_line(control_locals)
                self.control_dict[line][i].clicked.connect(control_groove_locals[i + 'test'])

            elif 'bu_preview' in i:
                control_locals = self.control_dict[line][i]
                control_groove_locals[i + 'test'] = lambda: self.preview_line(self.control_dict[line]['box_file'].currentText())
                self.control_dict[line][i].clicked.connect(control_groove_locals[i + 'test'])

            elif 'box_file' in i:
                control_locals_file = self.control_dict[line]['box_file']
                control_locals_preview = self.control_dict[line]['bu_preview']
                control_groove_locals[i + 'test'] = lambda: self.pf.preview_button_isbool(control_locals_file, control_locals_preview)
                self.control_dict[line]['box_file'].currentIndexChanged.connect(control_groove_locals[i + 'test'])
                self.pf.option_value(control_locals_file)
                # control_groove_locals[i + 'csv'] = lambda: self.cw.csv_data_append(control_locals_file)
                # self.control_dict[line]['box_file'].currentIndexChanged.connect(control_groove_locals[i + 'csv'])

        self.control_groove[line] = control_groove_locals

    def append_line(self): # 新增函数
        """
        添加每一行列表数据
        :return:
        """
        self.num += 1
        con = ['box_file', 'bu_add', 'bu_del', 'bu_preview']
        control_dict_loacls = {}

        for i in con[0: 1]:
            if 'box_file' in i: # 添加下拉变量
                control_dict_loacls[i] = QComboBox(self.topFiller)
                control_dict_loacls[i].setMaxVisibleItems(5)
                self.location_size(control_dict_loacls, i, self.num)
                control_dict_loacls[i].show()

        for i in con[1: 4]:
            control_dict_loacls[i] = QPushButton(self.topFiller)
            if 'bu_add' in i:
                control_dict_loacls[i].setText('新增')
                self.location_size(control_dict_loacls, i, self.num)
                control_dict_loacls[i].show()

            elif 'bu_del' in i:
                control_dict_loacls[i].setText('删除')
                self.location_size(control_dict_loacls, i, self.num)
                control_dict_loacls[i].show()

            elif 'bu_preview' in i:
                control_dict_loacls[i].setText('预览')
                self.location_size(control_dict_loacls, i, self.num)
                control_dict_loacls[i].show()

        for i in control_dict_loacls.keys():
            self.append_move(i, control_dict_loacls)

        if self.num >= 9:
            self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
            self.scroll.widget().resize(800, self.num * 30 + 10)
            self.scrollBar = self.scroll.verticalScrollBar()
            self.scrollBar.setValue(self.num * 30 + 10)

        elif self.num < 9:
            self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.control_dict[self.num] = control_dict_loacls
        self.append_signal_trigger(self.num)
        # self.cw.csv_data_append(self.control_dict[self.num]['box_file'], self)

    def delete_line(self, v):  # 传入一个名称，把名称提取出来数字，获取当前删除控件位置
        """
        删除时，会自动断开，删除表里面的数据
        :return:
        """
        for line in self.control_dict:
            if self.control_dict[line]['bu_del'] == v:
                for i in self.control_dict[line]:
                    if 'bu_del' in i:
                        self.control_dict[line][i].deleteLater()

                    elif 'bu_add' in i:
                        self.control_dict[line][i].deleteLater()

                    elif 'box_file' in i:
                        self.control_dict[line][i].deleteLater()

                    elif 'bu_preview' in i:
                        self.control_dict[line][i].deleteLater()

                self.num -= 1
                num_loacls = 1
                self.cw.csv_data_delete(line)
                del self.control_dict[line]
                control_dict_loacls = {}
                for i in self.control_dict:
                    dict_locals = self.control_dict[i]
                    control_dict_loacls[num_loacls] = dict_locals
                    num_loacls += 1

                del self.control_dict
                self.control_dict = control_dict_loacls

                num_loacls = 1
                del self.control_groove[line]
                control_dict_loacls = {}
                for i in self.control_groove:
                    dict_locals = self.control_groove[i]
                    control_dict_loacls[num_loacls] = dict_locals
                    num_loacls += 1

                del self.control_groove
                self.control_groove = control_dict_loacls

                del self.isBox_file_dict[line - 1]

                break

        for i in self.control_dict:
            for j in self.control_dict[i]:
                self.delete_move(j, i)

        if self.num == 0:
            self.append_line()

        if self.num >= 9:
            self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
            self.scroll.widget().resize(800, self.num * 30 + 10)
            self.scrollBar = self.scroll.verticalScrollBar()
            self.scrollBar.setValue(self.num * 30 + 10)

        elif self.num < 9:
            self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

    def preview_line(self, comboBox_preview_text):  # 预览功能
        self.tableWidget_preview.setRowCount(0)  # 清空所有行
        path = r"{}\{}".format(self.path, comboBox_preview_text)
        with open(path, 'r', newline='', encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            next(csv_reader)  # 跳过第一行
            for row in csv_reader:
                row_position = self.tableWidget_preview.rowCount()
                self.tableWidget_preview.insertRow(row_position)

                for col, item in enumerate(row):
                    items = QTableWidgetItem(item)
                    # 设置为只读
                    items.setFlags(items.flags() & ~Qt.ItemFlag.ItemIsEditable)
                    self.tableWidget_preview.setItem(row_position, col, items)

    def isBox_file_dict_bool(self, comboBox_template):
        return self.isBox_file_dict[self.reture_Box_line_dict(comboBox_template)]

    # def reture_Box_line_dict(self, comboBox_template):
    #     for line in self.control_dict:
    #         if self.control_dict[line]['box_template'] == comboBox_template:
    #             return line - 1
    #     return None