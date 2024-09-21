import pyperclip
from PyQt6.QtWidgets import *

class web_error:
    def __init__(self):
        pass
    # 继承于QDialog，需要show,exec,open来弹出
    # 默认是一个模态对话框，即使show弹出的对话框也是模态的
    # mb = QMessageBox(QMessageBox.NoIcon,'对话框标题','<h2>主要标题信息</h2>',QMessageBox.Ok | QMessageBox.Discard    ,self)
    # 参数1 图标:
    # QMessageBox.NoIcon  没有图标
    # QMessageBox.Warning  警告图标
    # QMessageBox.Critical  严重问题图标
    # QMessageBox.Information   没有任何异常图标
    # QMessageBox.Question  提问图标
    # 参数2 对话框标题
    # 参数3 主要标题信息--可以是富文本
    # 参数4 按钮：
    # QMessageBox.Ok          使用AcceptRole定义的“确定”按钮
    # QMessageBox.Discard     “丢弃”或“不保存”按钮，具体取决于使用DestructiveRole定义的平台
    # QMessageBox.Open   使用AcceptRole定义的“打开”按钮。
    # QMessageBox.Save   使用AcceptRole定义的“保存”按钮。
    # QMessageBox.Cancel   使用RejectRole定义的“取消”按钮。
    # QMessageBox.Close   使用RejectRole定义的“关闭”按钮。
    # QMessageBox.Apply   使用ApplyRole定义的“应用”按钮。
    # QMessageBox.Reset   使用ResetRole定义的“重置”按钮。
    # QMessageBox.RestoreDefaults  使用ResetRole定义的“恢复默认值”按钮。
    # QMessageBox.SaveAll   使用AcceptRole定义的“全部保存”按钮。
    # QMessageBox.Yes   使用YesRole定义的“是”按钮。
    # QMessageBox.YesToAll   使用YesRole定义的“Yes to All”按钮。
    # QMessageBox.No   使用NoRole定义的“否”按钮。
    # QMessageBox.Help  使用HelpRole定义的“帮助”按钮。
    # QMessageBox.NoToAll  使用NoRole定义的“No to All”按钮。
    # QMessageBox.Abort   使用RejectRole定义的“Abort”按钮。
    # QMessageBox.Retry  使用AcceptRole定义的“重试”按钮。
    # QMessageBox.Ignore   使用AcceptRole定义的“忽略”按钮。
    # QMessageBox.NoButton   无效按钮。

    def box_critical(self, text): # 报错
        ScrollMessageBox.critical_text = text
        ScrollMessageBox(QMessageBox.Icon.Critical, "错误", text)

    def box_warning(self, text): # 警告
        """
        警告用法
        :param text: 警告语
        :return:
        """
        messageBox = QMessageBox()
        messageBox.setIcon(QMessageBox.Icon.Warning)
        messageBox.setWindowTitle('警告')
        messageBox.setText(text)
        messageBox.setStandardButtons(QMessageBox.StandardButton.Yes)
        buttonY = messageBox.button(QMessageBox.StandardButton.Yes)
        buttonY.setText('确定')
        messageBox.exec()

    def box_information(self, text): # 建议
        messageBox = QMessageBox()
        messageBox.setIcon(QMessageBox.Icon.Information) # 设置图标
        messageBox.setWindowTitle('消息') # 设置标题
        messageBox.setText(text) # 设置内容
        messageBox.setStandardButtons(QMessageBox.StandardButton.Yes) # 设置按钮
        buttonY = messageBox.button(QMessageBox.StandardButton.Yes)
        buttonY.setText('确定')
        messageBox.exec()

    def box_cancel(self, text):
        messageBox = QMessageBox()
        messageBox.setIcon(QMessageBox.Icon.Warning)
        messageBox.setWindowTitle('是否取消')
        messageBox.setText(text)
        messageBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
        buttonY = messageBox.button(QMessageBox.StandardButton.Yes)
        buttonN = messageBox.button(QMessageBox.StandardButton.Cancel)
        buttonY.setText('确定')
        buttonN.setText('取消')
        result = messageBox.exec()

        if result == QMessageBox.StandardButton.Yes:
            return True

        elif result == QMessageBox.StandardButton.Cancel:
            return False

class ScrollMessageBox(QMessageBox):
    def ScrollMessageBox(self, *args, **kwargs):
        QMessageBox.__init__(self, *args, **kwargs)

        self.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        buttonY = self.button(QMessageBox.StandardButton.Yes)
        buttonCopy = self.button(QMessageBox.StandardButton.No)
        buttonY.setText('确认')
        buttonCopy.setText('复制文本')
        chldn = self.children()
        scrll = QScrollArea(self)
        scrll.setWidgetResizable(True)
        grd = self.findChild(QGridLayout)
        lbl = QLabel(chldn[1].text(), self)
        lbl.setWordWrap(True)
        scrll.setWidget(lbl)
        scrll.setMinimumSize (500,100)
        grd.addWidget(scrll , 0 , 1)
        chldn[1].setText('')
        self.exec()

        if self.clickedButton() == buttonCopy:
            pyperclip.copy(self.critical_text)
            # pyperclip.paste()  # 获取剪切板内容

        elif self.clickedButton() != buttonCopy:
            pass

