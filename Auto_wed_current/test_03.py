from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

app = QApplication([])

# 创建主窗口和表格
window = QWidget()
layout = QVBoxLayout()
table = QTableWidget(0, 3)  # 0 行 3 列

# 设置表头
table.setHorizontalHeaderLabels(['Column 1', 'Column 2', 'Column 3'])


# 添加一行数据
def add_row(data):
    row_position = table.rowCount()
    table.insertRow(row_position)  # 插入新行

    for column, value in enumerate(data):
        table.setItem(row_position, column, QTableWidgetItem(value))  # 设置单元格内容

    table.resizeRowsToContents()  # 自动调整行高


# 传入一整行的数据
row_data = ['Data 1', 'Data 2', 'Data 3']
add_row(row_data)

layout.addWidget(table)
window.setLayout(layout)
window.show()

app.exec()
