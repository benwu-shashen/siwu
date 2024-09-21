import re
from PyQt6.QtGui import QTextCursor

from Auto_wed_current.Auto_UI.GUI_Error.web_error import web_error
from Auto_wed_current.Auto_UI.__init__ import property_data
from Auto_wed_current.Auto_execute.execute_summary import execute_summary


class web_edit_print(property_data):
    def __init__(self):
        super().__init__()
        execute_summary.Edit_summary = self.Edit_summary  # 执行完结果打印

    def move_Position(self):
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        self.textEdit.setTextCursor(cursor)

    def Edit(self, text):
        """
        文本线程
        :param text:
        :return:
        """
        self.textEdit.append("<font color='black'>{}</font>".format(text))
        self.move_Position()

    def Edit_error(self, text):
        self.textEdit.append("<font color='red'>{}</font>".format(text))
        self.move_Position()

    def judge_data(self, text):
        if '原始数据' in text:
            text_rl = text.replace('原始数据', '<font color="green">原始数据</font>')
            return text_rl

        elif '替换数据' in text:
            text_rl = text.replace('原始数据', '<font color="yellow">替换数据</font>')
            return text_rl

    def Edit_summary(self, text, title, judge=None):
        """
        过程打印
        :param text:
        :param title:
        :param judge:
        :return:
        """
        if title == 'file':
            self.textEdit.append("<font color='black'>{}</font>".format(text))
            self.move_Position()

        elif title == 'sheet':
            if judge == '成功':
                text = self.judge_data(text)
                self.textEdit.append("<font color='black'>{}</font>".format(text))
                self.move_Position()

            elif judge == '失败':
                if '原始数据' in text:
                    text = self.judge_data(text)
                    self.textEdit.append("<font color='red'>{}</font>".format(text))
                    self.move_Position()

        elif title == 'summary':
            result = re.search('失败数\d*', text)
            info = result.group()
            text = text.replace(info, '<font color="red">{}</font>'.format(info))
            self.textEdit.append("<font color='black'>{}</font>".format(text))
            self.textEdit.append("".format(text))
            self.move_Position()

    def clear_text(self):
        self.textEdit.clear()
        web_error().box_information('清理成功')