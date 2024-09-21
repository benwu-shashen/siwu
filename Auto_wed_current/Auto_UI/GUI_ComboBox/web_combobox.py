from PyQt6 import QtCore
from PyQt6.QtWidgets import *

from Auto_wed_current.Auto_UI.GUI_CSV.web_csv_write import web_csv_write
from Auto_wed_current.Auto_UI.__init__ import property_data
from .web_combobox_file import web_combobox_file
from .web_combobox_sheet import web_combobox_sheet
from .web_combobox_sheet_QlineEdit import web_combobox_sheet_QlineEdit
from .web_combobox_template import web_combobox_template

class web_combobox(property_data):
    def __init__(self):
        super().__init__()
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
        self.isBox_file_dict = [] # 为true时，才会更新box_sheet

        self.current_del_line = -1 # 当前删除行

        self.wf = web_combobox_file()
        self.cw = web_csv_write() # 获取cs目录
        self.ws = web_combobox_sheet()
        self.wt = web_combobox_template()
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
        if 'box_template' in key:
            dir[key].setGeometry(QtCore.QRect(0, 0, 80, 22))

        elif 'box_file' in key:
            dir[key].setGeometry(QtCore.QRect(0, 0, 120, 22))

        elif 'box_sheet'.format(num) in key:
            dir[key].setGeometry(QtCore.QRect(0, 0, 200, 22))

        elif 'box_wait'.format(num) in key:
            dir[key].setGeometry(QtCore.QRect(0, 0, 50, 22))

        elif 'bu_add'.format(num) in key:
            dir[key].setGeometry(QtCore.QRect(0, 0, 75, 22))

    def append_move(self, key, control_dict_loacls):
        """
        移动调整每一个列表数据
        :param key:
        :return:
        """
        y = self.num * 30 + 10# 首行为10px，所以不相乘，加10，因此减1
        if 'box_template' == key:
            control_dict_loacls[key].move(10, y)

        elif 'box_file' == key:
            control_dict_loacls[key].move(100, y)

        elif 'box_sheet' == key:
            control_dict_loacls[key].move(240, y)

        elif 'box_wait' == key:
            control_dict_loacls[key].move(460, y)

        elif 'bu_add'== key:
            control_dict_loacls[key].move(550, y)

        elif 'bu_del' == key:
            control_dict_loacls[key].move(645, y)

    def delete_move(self, key, delete_line):
        """
        删除时，复位每一条数据
        :param key:
        :param delete_line:
        :return:
        """
        num_y = delete_line  # 首行为10px，所以不相乘，加10，因此减1
        y = num_y * 30 + 10
        if 'box_template' in key:
            self.control_dict[delete_line][key].move(10, y)

        elif 'box_file' in key:
            self.control_dict[delete_line][key].move(100, y)

        elif 'box_sheet' in key:
            self.control_dict[delete_line][key].move(240, y)

        elif 'box_wait' in key:
            self.control_dict[delete_line][key].move(460, y)

        elif 'bu_add' in key:
            self.control_dict[delete_line][key].move(550, y)

        elif 'bu_del' in key:
            self.control_dict[delete_line][key].move(645, y)

    def append_title(self):
        """
        标题文字
        :return:
        """
        con = ['title_template', 'title_file', 'title_sheet', 'title_wait', 'title_handle']
        for i in con:
            self.title_labels[i] = QLabel(self.topFiller)

        for i in con:
            if 'title_template' == i:
                self.title_labels[i].setText('模板')
                self.title_labels[i].move(10, 10)

            elif 'title_file' == i:
                self.title_labels[i].setText('文件名')
                self.title_labels[i].move(100, 10)

            elif 'title_sheet' == i:
                self.title_labels[i].setText('工作表名')
                self.title_labels[i].move(240, 10)

            elif 'title_wait' == i:
                self.title_labels[i].setText('等待时间')
                self.title_labels[i].move(460, 10)

            elif 'title_handle' == i:
                self.title_labels[i].setText('操作')
                self.title_labels[i].move(550, 10)

    def append_signal_trigger(self, line : int): # 新增时，触发信号
        """
        新增时，添加每个控件槽信号
        :return:
        """
        control_groove_locals = {}
        for i in self.control_dict[line]:
            if 'bu_add' in i:
                control_locals_template = self.control_dict[line]['box_template']
                control_locals_file = self.control_dict[line]['box_file']
                control_locals_sheet = self.control_dict[line]['box_sheet']
                control_locals_wait = self.control_dict[line]['box_wait']
                self.control_dict[line][i].clicked.connect(self.append_line)

            elif 'bu_del' in i:
                control_locals = self.control_dict[line][i]
                control_groove_locals[i + 'test'] = lambda: self.delete_line(control_locals)
                self.control_dict[line][i].clicked.connect(control_groove_locals[i + 'test'])

            elif 'box_file' in i:
                control_locals_template = self.control_dict[line]['box_template']
                control_locals_file = self.control_dict[line]['box_file']
                control_locals_sheet = self.control_dict[line]['box_sheet']
                control_locals_wait = self.control_dict[line]['box_wait']
                control_groove_locals[i + 'test'] = lambda : self.wf.option_value(control_locals_template, control_locals_file, self)
                self.control_dict[line]['box_template'].currentIndexChanged.connect(control_groove_locals[i + 'test'])

                control_groove_locals[i + 'csv'] = lambda : self.cw.csv_data_append(control_locals_template, control_locals_file, control_locals_sheet, control_locals_wait, self)
                self.control_dict[line]['box_template'].currentIndexChanged.connect(control_groove_locals[i + 'csv'])

            elif 'box_sheet' in i:
                control_locals_template = self.control_dict[line]['box_template']
                control_locals_file = self.control_dict[line]['box_file']
                control_locals_sheet = self.control_dict[line]['box_sheet']
                control_locals_wait = self.control_dict[line]['box_wait']
                control_locals_QlineEdit = self.control_dict[line]['box_QlineEdit']
                control_groove_locals[i + 'test'] =  lambda : self.ws.option_value(control_locals_template, control_locals_file, control_locals_sheet, control_locals_wait, control_locals_QlineEdit, self)
                self.control_dict[line]['box_file'].currentIndexChanged.connect(control_groove_locals[i + 'test'])

                control_groove_locals[i + 'csv'] = lambda: self.ws.show_selected(control_locals_template, control_locals_file, control_locals_sheet, control_locals_wait, control_locals_QlineEdit, self)
                self.control_dict[line]['box_file'].currentIndexChanged.connect(control_groove_locals[i + 'csv']) # 触发sheet选项变更，更改选项内容

            elif 'box_wait' in i:
                control_locals_template = self.control_dict[line]['box_template']
                control_locals_file = self.control_dict[line]['box_file']
                control_locals_sheet = self.control_dict[line]['box_sheet']
                control_locals_wait = self.control_dict[line]['box_wait']
                control_groove_locals[i + 'csv'] = lambda : self.cw.csv_data_append(control_locals_template, control_locals_file, control_locals_sheet, control_locals_wait, self)
                self.control_dict[line][i].valueChanged.connect(control_groove_locals[i + 'csv'])

        self.control_groove[line] = control_groove_locals

    def append_line(self): # 新增函数
        """
        添加每一行列表数据
        :return:
        """
        self.num += 1
        con = ['box_template', 'box_file', 'box_sheet', 'box_wait', 'bu_add', 'bu_del', 'box_QlineEdit']
        control_dict_loacls = {}

        for i in con[0: 4]:
            if 'box_wait' in i: # 添加等待变量
                control_dict_loacls[i]= QSpinBox(self.topFiller)
                control_dict_loacls[i].setValue(15)
                self.location_size(control_dict_loacls, i, self.num)
                control_dict_loacls[i].show()

            elif 'box_wait' not in i: # 添加下拉变量
                control_dict_loacls[i] = QComboBox(self.topFiller)
                control_dict_loacls[i].setMaxVisibleItems(5)
                self.location_size(control_dict_loacls, i, self.num)
                control_dict_loacls[i].show()
                if 'box_template' in i:
                    self.isBox_file_dict.append(False)
                    self.wt.option_value(control_dict_loacls[i])

        for i in con[4: 7]:
            if 'box_QlineEdit' in i:
                control_dict_loacls[i] = web_combobox_sheet_QlineEdit()
                continue

            control_dict_loacls[i] = QPushButton(self.topFiller)
            if 'bu_add' in i:
                control_dict_loacls[i].setText('新增')
                self.location_size(control_dict_loacls, i, self.num)
                control_dict_loacls[i].show()

            elif 'bu_del' in i:
                control_dict_loacls[i].setText('删除')
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
        self.cw.csv_data_append(self.control_dict[self.num]['box_template'], self.control_dict[self.num]['box_file'], self.control_dict[self.num]['box_sheet'], self.control_dict[self.num]['box_wait'], self)

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

                    elif 'box_template' in i:
                        self.control_dict[line][i].deleteLater()

                    elif 'bu_add' in i:
                        self.control_dict[line][i].deleteLater()

                    elif 'box_file' in i:
                        self.control_dict[line][i].deleteLater()

                    elif 'box_sheet' in i:
                        self.control_dict[line][i].deleteLater()

                    elif 'box_wait' in i:
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

    def isBox_file_dict_bool(self, comboBox_template):
        return self.isBox_file_dict[self.reture_Box_line_dict(comboBox_template)]

    def reture_Box_line_dict(self, comboBox_template):
        for line in self.control_dict:
            if self.control_dict[line]['box_template'] == comboBox_template:
                return line - 1
        return None