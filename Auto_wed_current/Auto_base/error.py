import os
import shutil
import time

from Auto_wed_current.Auto_base.error_reminder import error_reminder
from Auto_wed_current.Auto_base.filename import filename
from Auto_wed_current.Auto_driver.driver_class import driver_class
from Auto_wed_current.Auto_file.setting_csv import setting_csv


class error_all():
    def __init__(self, row, xpath, action, account, text, excel_file, excel_sheet, row_replace=None, data_judge=None):
        self.row = row
        self.xpath = xpath
        self.account = account
        self.action = action
        self.text = text
        self.excel_file = excel_file
        self.excel_sheet = excel_sheet
        self.driver = driver_class().driver_Chrome(self.account)
        self.row_replace = row_replace
        self.data_judge = data_judge
        self.img = ''

    def error_screenshot(self): # 报错截图
        judge = setting_csv()

        if judge[1][0] == '是':
            time.sleep(1)
            if self.data_judge == '替换数据':
                self.img = '替换数据-第' + str(self.row_replace - 1) + '步报错截图.png'

            elif self.data_judge == None:
                self.img = '第' + str(self.row) + '步报错截图.png'

            elif self.data_judge == '原始数据':
                self.img = '原始数据-第' + str(self.row) + '步报错截图_1.png'
                for num in range(1, 100):
                    file = self.filename(r'\Auto_file\报错截图\{}\{}\{}'.format(self.excel_file, self.excel_sheet, self.img))
                    file_judge = os.path.exists(file)
                    if file_judge == True:
                        num += 1

                    elif file_judge == False:
                        self.img = '原始数据-第' + str(self.row) + '步报错截图_{}.png'.format(num)
                        break

            self.driver.save_screenshot(self.img)
            src = os.path.join(os.getcwd() + os.sep + self.img)
            excel_file_dir = filename().filename(r'\Auto_file\报错截图\{}'.format(self.excel_file))
            excel_sheet_dir = excel_file_dir + os.sep + self.excel_sheet

            excel_file_judge = os.path.exists(excel_file_dir) # 判断excel文件是否存在
            if excel_file_judge == True:
                try:
                    os.mkdir(excel_sheet_dir)
                except Exception:
                    pass

            else:
                os.mkdir(excel_file_dir)
                excel_sheet_judge = os.path.exists(excel_sheet_dir)
                if excel_sheet_judge == True:
                    os.remove(self.img)
                else:
                    os.mkdir(excel_sheet_dir)

            try:
                shutil.move(src, excel_sheet_dir) # 移动截图
            except Exception:
                os.remove(self.img)
                raise error_reminder('error_screenshot_01', img=self.img)

        elif judge[1][0] == '否':
            pass

    def error_action(self):
        data = [
            '其他-输入网址',
            '其他-窗口最大化',
            '其他-窗口最小化',
            '其他-切换窗口',
            '其他-关闭窗口或标签',
            '其他-清除句柄',
            '其他-新建标签',
            '其他-新建窗口',
            '其他-刷新页面',
            '其他-关闭浏览器',
            '其他-切换主框架',
            '其他-强制等待',
            '其他-坐标-点击',
            '其他-坐标-文本框输入',
            '其他-坐标-获取文本',
            '其他-图形交互_点击',
        ]

        if self.action not in data:
            raise error_reminder('error_action')

    def error_xpath(self):
        data = [
            'xpath-点击',
            'xpath-文本框输入',
            'xpath-切换框架',
            'xpath-上传附件',
            'xpath-滑动滚动条',
            'xpath-清空文本框',
            'xpath-填写时间控件',
            'xpath-获取文本',
        ]

        if self.action not in data:
            raise error_reminder('error_xpath')

    def error_account(self):
        if self.account != 'account_01':
            raise error_reminder('error_account')

    def error_text(self):
        data = [
            'xpath-文本框输入',
            'xpath-上传附件',
            'xpath-填写时间控件',
            'xpath_获取文本',
            '其他-输入网址',
            '其他-切换窗口',
            '其他-关闭窗口或标签',
            '其他-清除句柄',
            '其他-强制等待',
            '其他-坐标点击',
            '其他-坐标文本框输入',
            '其他-坐标-获取文本',
            '其他-图形交互_点击',
        ]

        if self.action in data:
            if self.text == '' or self.text == None:
                raise  error_reminder('error_text')




