from PyQt6 import QtWidgets, QtCore

class MyScrollArea(QtWidgets.QScrollArea):
    def __init__(self, parent=None):
        super(MyScrollArea, self).__init__(parent)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

    def wheelEvent(self, event):
        # 忽略滚轮事件
        event.ignore()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    layout = QtWidgets.QVBoxLayout(window)

    scroll_area = MyScrollArea()
    content = QtWidgets.QWidget()
    content.setMinimumSize(400, 800)  # 设置内容的最小尺寸以确保可以滚动
    scroll_area.setWidget(content)

    layout.addWidget(scroll_area)
    window.setLayout(layout)
    window.show()

    sys.exit(app.exec())