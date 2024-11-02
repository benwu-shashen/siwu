# coding:utf-8
import sys

from PyQt6.QtCore import QFile, QPropertyAnimation, QTimer, Qt, QEvent, QPoint
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (QApplication, QFrame, QGraphicsDropShadowEffect,
                             QHBoxLayout, QLabel, QWidget, QPushButton)


class ToolTip(QFrame):

    def __init__(self, text='', parent=None):
        super().__init__(parent=parent)
        self.__text = text
        self.__duration = 1000
        self.timer = QTimer(self)
        self.hBox = QHBoxLayout(self)
        self.label = QLabel(text, self)
        self.ani = QPropertyAnimation(self, b'windowOpacity', self)

        # set layout
        self.hBox.addWidget(self.label)
        self.hBox.setContentsMargins(10, 7, 10, 7)

        # add shadow
        self.shadowEffect = QGraphicsDropShadowEffect(self)
        self.shadowEffect.setBlurRadius(32)
        self.shadowEffect.setColor(QColor(0, 0, 0, 60))
        self.shadowEffect.setOffset(0, 5)
        self.setGraphicsEffect(self.shadowEffect)

        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.hide)

        # set style
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
        self.setDarkTheme(False)
        self.__setQss()

    def text(self):
        return self.__text

    def setText(self, text: str):
        """ set text on tooltip """
        self.__text = text
        self.label.setText(text)
        self.label.adjustSize()
        self.adjustSize()

    def duration(self):
        return self.__duration

    def setDuration(self, duration: int):
        """ set tooltip duration in milliseconds """
        self.__duration = abs(duration)

    def __setQss(self):
        """ set style sheet """
        f = QFile("resource/tooltip.qss")
        f.open(QFile.OpenModeFlag.ReadOnly)
        self.setStyleSheet(str(f.readAll(), encoding='utf-8'))
        f.close()

        self.label.adjustSize()
        self.adjustSize()

    def setDarkTheme(self, dark=False):
        """ set dark theme """
        dark = 'true' if dark else 'false'
        self.setProperty('dark', dark)
        self.label.setProperty('dark', dark)
        self.setStyle(QApplication.style())

    def showEvent(self, e):
        self.timer.stop()
        self.timer.start(self.__duration)
        super().showEvent(e)

    def hideEvent(self, e):
        self.timer.stop()
        super().hideEvent(e)

class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.hBox = QHBoxLayout(self)
        self.button1 = QPushButton('キラキラ', self)
        self.button2 = QPushButton('食べた愛', self)
        self._toolTip = ToolTip(parent=self)
        # self._toolTip.setDarkTheme(True)

        self.button1.setToolTip('aiko - キラキラ ✨')
        self.button2.setToolTip('aiko - 食べた愛 🥰')
        self.button1.setToolTipDuration(1000)
        self.button2.setToolTipDuration(5000)

        self.button1.installEventFilter(self)
        self.button2.installEventFilter(self)

        self.hBox.setContentsMargins(30, 30, 30, 30)
        self.hBox.setSpacing(20)
        self.hBox.addWidget(self.button1)
        self.hBox.addWidget(self.button2)

        self.resize(600, 300)
        self._toolTip.hide()

        with open(r'C:\Users\16946\Desktop\文件\文件\siwu\Auto_wed_current\demo.qss', encoding='utf-8') as f:
            self.setStyleSheet(f.read())

    def eventFilter(self, obj, e: QEvent):
        if obj is self:
            return super().eventFilter(obj, e)

        tip = self._toolTip
        if e.type() == QEvent.Type.Enter:
            tip.setText(obj.toolTip())
            tip.setDuration(obj.toolTipDuration())

            pos = obj.mapTo(self, QPoint(0, 0))
            x = pos.x() + obj.width()//2 - tip.width()//2
            y = pos.y() - 5 - tip.height()

            # adjust postion to prevent tooltips from appearing outside the window
            x = min(max(5, x), self.width() - tip.width() - 5)
            y = min(max(5, y), self.height() - tip.height() - 5)

            tip.move(x, y)
            tip.show()
        elif e.type() == QEvent.Type.Leave:
            tip.hide()
        elif e.type() == QEvent.Type.ToolTip:
            return True

        return super().eventFilter(obj, e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    app.exec()


