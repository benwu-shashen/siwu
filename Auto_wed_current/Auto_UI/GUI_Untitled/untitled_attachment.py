# Form implementation generated from reading ui file 'untitled_attachment.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form_attachment(object):
    def setupUi(self, Form_attachment):
        Form_attachment.setObjectName("Form_attachment")
        Form_attachment.resize(370, 331)
        self.frame_Edit_attachment = QtWidgets.QFrame(parent=Form_attachment)
        self.frame_Edit_attachment.setGeometry(QtCore.QRect(10, 10, 351, 311))
        self.frame_Edit_attachment.setMinimumSize(QtCore.QSize(351, 0))
        self.frame_Edit_attachment.setStyleSheet("QFrame\n"
"{\n"
"border:2px solid rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_Edit_attachment.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.frame_Edit_attachment.setLineWidth(3)
        self.frame_Edit_attachment.setObjectName("frame_Edit_attachment")
        self.listWidget_attachment = QtWidgets.QListWidget(parent=self.frame_Edit_attachment)
        self.listWidget_attachment.setGeometry(QtCore.QRect(10, 60, 256, 192))
        self.listWidget_attachment.setStyleSheet("QListWidget\n"
"{\n"
"border:2px solid rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"background-color: rgb(0, 0, 0, 0);\n"
"}")
        self.listWidget_attachment.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
        self.listWidget_attachment.setObjectName("listWidget_attachment")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_Edit_attachment)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 81, 21))
        self.label_5.setStyleSheet("QLabel\n"
"{\n"
"border: none;\n"
"border-radius: 5px;\n"
"background-color: rgb(0, 0, 0, 0);\n"
"}")
        self.label_5.setObjectName("label_5")
        self.pushButton_attachment_append = QtWidgets.QPushButton(parent=self.frame_Edit_attachment)
        self.pushButton_attachment_append.setGeometry(QtCore.QRect(270, 60, 75, 23))
        self.pushButton_attachment_append.setStyleSheet("QPushButton {\n"
"border:2px solid rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"background-color: rgb(0, 0, 0, 0);\n"
"}")
        self.pushButton_attachment_append.setObjectName("pushButton_attachment_append")
        self.pushButton_attachment_delete = QtWidgets.QPushButton(parent=self.frame_Edit_attachment)
        self.pushButton_attachment_delete.setGeometry(QtCore.QRect(270, 90, 75, 23))
        self.pushButton_attachment_delete.setStyleSheet("QPushButton {\n"
"border:2px solid rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"background-color: rgb(0, 0, 0, 0);\n"
"}")
        self.pushButton_attachment_delete.setObjectName("pushButton_attachment_delete")
        self.label_6 = QtWidgets.QLabel(parent=self.frame_Edit_attachment)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 81, 21))
        self.label_6.setStyleSheet("QLabel\n"
"{\n"
"border: none;\n"
"border-radius: 5px;\n"
"background-color: rgb(0, 0, 0, 0);\n"
"}")
        self.label_6.setObjectName("label_6")
        self.pushButton_attachment_confirm = QtWidgets.QPushButton(parent=self.frame_Edit_attachment)
        self.pushButton_attachment_confirm.setGeometry(QtCore.QRect(40, 270, 75, 23))
        self.pushButton_attachment_confirm.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_attachment_confirm.setStyleSheet("QPushButton {\n"
"border:2px solid rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"background-color: rgb(0, 0, 0, 0);\n"
"}")
        self.pushButton_attachment_confirm.setObjectName("pushButton_attachment_confirm")
        self.pushButton_attachment_cancel = QtWidgets.QPushButton(parent=self.frame_Edit_attachment)
        self.pushButton_attachment_cancel.setGeometry(QtCore.QRect(170, 270, 75, 23))
        self.pushButton_attachment_cancel.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_attachment_cancel.setStyleSheet("QPushButton {\n"
"border:2px solid rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"background-color: rgb(0, 0, 0, 0);\n"
"}")
        self.pushButton_attachment_cancel.setObjectName("pushButton_attachment_cancel")

        self.retranslateUi(Form_attachment)
        self.listWidget_attachment.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(Form_attachment)

    def retranslateUi(self, Form_attachment):
        _translate = QtCore.QCoreApplication.translate
        Form_attachment.setWindowTitle(_translate("Form_attachment", "上传附件"))
        self.listWidget_attachment.setSortingEnabled(False)
        self.label_5.setText(_translate("Form_attachment", " 附件"))
        self.pushButton_attachment_append.setText(_translate("Form_attachment", "新增"))
        self.pushButton_attachment_delete.setText(_translate("Form_attachment", "删除"))
        self.label_6.setText(_translate("Form_attachment", " 维护上传文件"))
        self.pushButton_attachment_confirm.setText(_translate("Form_attachment", "确认"))
        self.pushButton_attachment_cancel.setText(_translate("Form_attachment", "取消"))
