import sys
from PyQt6 import QtWidgets

from Auto_wed_current.Auto_UI.GUI_Untitled.untitled_test import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.test_01)

    def test_01(self):
        print("test_01")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())