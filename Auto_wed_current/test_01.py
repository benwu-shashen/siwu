from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt, QPoint


class CustomTooltip(QWidget):
    def __init__(self, text):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.FramelessWindowHint | Qt.WindowType.Tool)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
        layout = QVBoxLayout()
        label = QLabel(text)
        layout.addWidget(label)
        self.setLayout(layout)

    def show_tooltip(self, position):
        self.move(position)
        self.show()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.button = QPushButton("悬浮我")
        self.button.setToolTip("这是按钮的提示信息")

        # 创建悬浮窗口
        self.tooltip = CustomTooltip("这是悬浮窗口的内容")

        # 连接鼠标事件
        self.button.enterEvent = self.show_tooltip
        self.button.leaveEvent = self.hide_tooltip

        layout.addWidget(self.button)
        self.setLayout(layout)

    def show_tooltip(self, event):
        pos = self.button.mapToGlobal(QPoint(0, self.button.height()))
        self.tooltip.show_tooltip(pos)

    def hide_tooltip(self, event):
        self.tooltip.hide()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.setWindowTitle("悬浮窗口示例")
    window.resize(300, 200)
    window.show()
    app.exec()

