import xlrd

workbook = xlrd.open_workbook('原始模板V1.0.xls')  # 替换为你的文件名
sheet = workbook.sheet_by_index(0)  # 选择第一个工作表

# 遍历每一行
for row_index in range(sheet.nrows):
    row_values = sheet.row_values(row_index)
    print(row_values)  # 输出当前行的数据
