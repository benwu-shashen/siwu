import csv
import time
from time import sleep

from PyQt6.QtCore import QThread, QWaitCondition, QMutex, pyqtSignal
from PyQt6.QtWidgets import QFileDialog

class thread_export(QThread): # 执行开始线程
    export_tips = pyqtSignal(str)
    def __init__(self):
        super(QThread, self).__init__()
        self.cond = QWaitCondition()
        self.mutex = QMutex()

    def filedialog(self): # 创建文件对话框
        dir = QFileDialog()
        text = dir.getExistingDirectory(None, "选择文件夹路径", 'C:/')  # 选择文件夹位置
        sleep(0.5)

        if text == '':
            pass

        elif text != '':
            self.move_file(text)
            self.export_tips.emit('导出成功')

    def move_file(self, path):
        list_text_all = [] # 全部文本
        list_verify = ['模板', '文件名', '工作表名', '等待时间'] # 校验文本
        list_num = [] # 文本编号

        name = path + '/' + self.filename() + '填写模板.csv'

        for property in self.control_dict:
            if property[-1] in list_num:
                pass

            elif property[-1] not in list_num:
                list_num.append(property[-1])
                globals()['list_num' + property[-1]] = []

            if 'box_template' in property:
                template = self.control_dict[property].currentText()
                globals()['list_num' + property[-1]].append(template)

            if 'box_file' in property:
                file = self.control_dict[property].currentText()
                globals()['list_num' + property[-1]].append(file)

            if 'box_sheet' in property:
                sheet = self.control_dict[property].currentText()
                globals()['list_num' + property[-1]].append(sheet)

            if 'box_wait' in property:
                wait = self.control_dict[property].value()
                globals()['list_num' + property[-1]].append(wait)

        list_text_all.append(list_verify) # 添加校验文本
        for num in list_num:
            list_text_all.append(globals()['list_num' + num])

        with open(name, 'w', encoding='ANSI', newline='') as write_text:
            writer = csv.writer(write_text)
            writer.writerows(list_text_all) # 多行写入

    def filename(self):
        now_time = time.strftime('%Y%m%d-%H%M%S', time.localtime())

        return now_time

    def run(self):
        self.mutex.lock()
        self.filedialog()
        self.mutex.unlock()
