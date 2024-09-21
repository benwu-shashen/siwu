import xlrd

from Auto_wed_current.Auto_base.error_reminder import error_reminder
from Auto_wed_current.Auto_base.filename import filename

"""
excel表格读取可添加需要读取的字段
"""

"""
注意：这里还要添加一个变量，row_replace，因为这个和原本的row是不一样的，记得加
"""

class excel_all(object):
    def __init__(self, row, excel_file, excel_sheet, data_judge, row_replace=None):
        """
        row:获取行
        row_replace:获取替换行
        excel_file:获取读取excel模板
        excel_sheet:获取读取sheet表
        replace_date:获取是否替换数据
        line:sheet列
        """

        self.row = row
        self.row_replace = row_replace
        self.file_original = filename().filename_func(r'\Auto_file\原始导入excel模板\{}'.format(excel_file)) # 原始数据
        self.file_replace = filename().filename_func(r'\Auto_file\替换导入excel模板\{}'.format(excel_file)) # 替换数据
        self.file_work = excel_sheet
        self.data_judge = data_judge


    def book_read(func):
        def book_judge(self, line, data_judge):
            line, file, row = func(self, line, data_judge)
            try:
                book = xlrd.open_workbook('{}'.format(file), encoding_override='utf-8')
            except Exception:
                raise error_reminder('excel_file', file=file)

            try:
                data = book.sheet_by_name(self.file_work)
            except Exception:
                raise error_reminder('excel_sheet', sheet=self.file_work)
            else:

                try:
                    valus = data.cell_value(row, line)
                except Exception:
                    pass
                else:
                    return valus

        return book_judge

    @book_read
    def book_read_judge(self, line, data_judge):
        if data_judge == '原始数据': # 读取原始数据
            return line, self.file_original, self.row

        elif data_judge == '替换数据': # 读取替换数据
            return line, self.file_replace, self.row_replace

    def excel_replace_num(self): # 获取替换数据num
        excel_xpath_valus = self.book_read_judge(0, self.data_judge)
        return excel_xpath_valus

    def excel_xpath(self): # 获取xpath
        excel_xpath_valus = self.book_read_judge(1, self.data_judge)
        return excel_xpath_valus

    def excel_action(self): # 获取操作
        excel_action_valus = self.book_read_judge(2, self.data_judge)
        return excel_action_valus

    def excel_text(self): # 获取内容输入
        excel_text_valus = self.book_read_judge(3, self.data_judge)
        return excel_text_valus

    def excel_account(self): # 获取account
        excel_account_valus = self.book_read_judge(4, self.data_judge)
        return excel_account_valus

    def excel_screenshot(self): # 获取是否截图
        excel_screenshot_valus = self.book_read_judge(5, self.data_judge)
        return excel_screenshot_valus

    def excel_account_num(self): # 获取账号数量，决定多开多少个浏览器
        book = xlrd.open_workbook('{}'.format(self.file_original))
        data = book.sheet_by_name(self.file_work)
        valus_account_sun = []

        while True:
            try:
                valus_xpath = data.cell_value(self.row, 1)
            except Exception:
                self.row -= 1
                break
            else:
                if valus_xpath == '' or valus_xpath == None:
                    self.row -= 1
                    break
                else:
                    self.row += 1

        for valus_account_num in range(self.row):
            valus_account_num += 1
            valus_account = data.cell_value(valus_account_num, 4)
            valus_account_sun.append(valus_account)

        if '' in valus_account_sun:
            valus_num = set(valus_account_sun)
            valus_num.remove('')
        else:
            valus_num = set(valus_account_sun)

        if len(valus_num) == 0:
            raise error_reminder('excel_account_num')
        else:
            return len(valus_num)
