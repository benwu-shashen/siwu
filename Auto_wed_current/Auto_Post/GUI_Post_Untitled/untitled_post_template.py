# Form implementation generated from reading ui file 'untitled_post_template.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form_Template(object):
    def setupUi(self, Form_Template):
        Form_Template.setObjectName("Form_Template")
        Form_Template.resize(370, 300)
        self.frame_Edit_Template = QtWidgets.QFrame(parent=Form_Template)
        self.frame_Edit_Template.setGeometry(QtCore.QRect(10, 10, 351, 281))
        self.frame_Edit_Template.setStyleSheet("QFrame\n"
"{\n"
"border:2px solid rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_Edit_Template.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.frame_Edit_Template.setLineWidth(3)
        self.frame_Edit_Template.setObjectName("frame_Edit_Template")
        self.listWidget_original = QtWidgets.QListWidget(parent=self.frame_Edit_Template)
        self.listWidget_original.setGeometry(QtCore.QRect(10, 60, 256, 192))
        self.listWidget_original.setStyleSheet("QListWidget\n"
"{\n"
"border:2px solid rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"background-color: rgb(0, 0, 0, 0);\n"
"}")
        self.listWidget_original.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
        self.listWidget_original.setObjectName("listWidget_original")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_Edit_Template)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 61, 21))
        self.label_2.setStyleSheet("QLabel\n"
"{\n"
"border: none;\n"
"border-radius: 5px;\n"
"background-color: rgb(0, 0, 0, 0);\n"
"}")
        self.label_2.setObjectName("label_2")
        self.pushButton_original_append = QtWidgets.QPushButton(parent=self.frame_Edit_Template)
        self.pushButton_original_append.setGeometry(QtCore.QRect(270, 60, 75, 23))
        self.pushButton_original_append.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_original_append.setStyleSheet("QPushButton {\n"
"border:2px solid rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"background-color: rgb(0, 0, 0, 0);\n"
"}")
        self.pushButton_original_append.setObjectName("pushButton_original_append")
        self.pushButton_original_delete = QtWidgets.QPushButton(parent=self.frame_Edit_Template)
        self.pushButton_original_delete.setGeometry(QtCore.QRect(270, 90, 75, 23))
        self.pushButton_original_delete.setStyleSheet("QPushButton {\n"
"border:2px solid rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"background-color: rgb(0, 0, 0, 0);\n"
"}")
        self.pushButton_original_delete.setObjectName("pushButton_original_delete")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_Edit_Template)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 81, 21))
        self.label_4.setStyleSheet("QLabel\n"
"{\n"
"border: none;\n"
"border-radius: 5px;\n"
"background-color: rgb(0, 0, 0, 0);\n"
"}")
        self.label_4.setObjectName("label_4")
        self.pushButton_template_quit = QtWidgets.QPushButton(parent=self.frame_Edit_Template)
        self.pushButton_template_quit.setGeometry(QtCore.QRect(270, 230, 75, 23))
        self.pushButton_template_quit.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_template_quit.setStyleSheet("QPushButton {\n"
"border:2px solid rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"background-color: rgb(0, 0, 0, 0);\n"
"}")
        self.pushButton_template_quit.setObjectName("pushButton_template_quit")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_Edit_Template)
        self.label_5.setGeometry(QtCore.QRect(70, 30, 191, 21))
        self.label_5.setStyleSheet("QLabel\n"
"{\n"
"border: none;\n"
"border-radius: 5px;\n"
"background-color: rgb(0, 0, 0, 0);\n"
"}")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form_Template)
        self.listWidget_original.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(Form_Template)

    def retranslateUi(self, Form_Template):
        _translate = QtCore.QCoreApplication.translate
        Form_Template.setWindowTitle(_translate("Form_Template", "编辑模板"))
        self.listWidget_original.setSortingEnabled(False)
        self.label_2.setText(_translate("Form_Template", " 导入模板"))
        self.pushButton_original_append.setText(_translate("Form_Template", "新增"))
        self.pushButton_original_delete.setText(_translate("Form_Template", "删除"))
        self.label_4.setText(_translate("Form_Template", " 编辑接口模板"))
        self.pushButton_template_quit.setText(_translate("Form_Template", "退出"))
        self.label_5.setText(_translate("Form_Template", "注意：导入xls文件会转换为csv文件"))
