import os
import re
import time

# import pywinauto
# from pywinauto.keyboard import send_keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Auto_wed_current.Auto_base.error_reminder import error_reminder
from Auto_wed_current.Auto_driver.driver_class import driver_class

"""
xpath读取以及操作
"""

class driver_xpath(object):
    def __init__(self, row, xpath, account, error, text, excel_file, excel_sheet):
        self.xpath = xpath # 获取xapth
        self.account = account # 获取账号
        self.error = error # 获取报错行数
        self.text = text # 获取文本框内容
        self.row = row # 获取当前步骤
        self.driver = driver_class().driver_Chrome(self.account) # 获取浏览器实例
        self.excel_file = excel_file  # 获取文件夹
        self.excel_sheet = excel_sheet  # 获取工作表

    def text_variable(self, text):
        num_string = -1
        list_01 = []  # 变量值下标
        list_02 = []
        list_03 = []  # 变量列表

        for string in text:
            num_string += 1
            if string == '【':
                list_02 = []
                list_02.append(num_string)
                list_01.append(list_02)
            elif string == '】':
                list_02.append(num_string)
            if string == '《':
                list_02 = []
                list_02.append(num_string)
                list_01.append(list_02)
            elif string == '》':
                list_02.append(num_string)

        if list_01 == []:
            raise error_reminder('xpath_text_04', text=list_01)

        for num in list_01:
            if text[num[0]] + text[num[1]] == '【】' or text[num[0]] + text[num[1]] == '《》':
                pass
            else:
                raise error_reminder('xpath_text_02', text=text[0])  # 判断获取的字符是否符合填写格式，如果不符合填写格式，则会报错

        for num in list_01:
            string_value = ''
            for x in range(num[0], num[1] + 1):
                string_value += text[x]
            list_03.append(string_value)  # 获取变量值，循环每一个字符，符合条件的字符就相加，最终生成一个列表变量

        return list_01, list_03

    def xpath_click(self): # 点击
        try:
            self.driver.find_element(By.XPATH, self.xpath).click()
        except Exception:
            try:
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.xpath).click()
            except Exception:
                try:
                    time.sleep(2)
                    self.driver.find_element(By.XPATH, self.xpath).click()
                except Exception:
                    raise error_reminder('xpath_click')

    def xpath_send_keys(self, text_list): # 文本框输入
        def substitute_variable(text):
            data_6 = []
            for key in text_list:
                if key in(text):
                    data_6.append(key)

            if data_6 != []:
                for variable in data_6:
                    text = text.replace(variable, text_list[variable])

            return text

        data_1 = re.findall('%H:%M:%S', self.text) # 读取指定内容

        if data_1 == []:
            try:
                text = substitute_variable(self.text)
                self.driver.find_element(By.XPATH, self.xpath).send_keys(text)
            except Exception:
                raise error_reminder('xpath_send_keys')

        elif data_1[0] == '%H:%M:%S':
            data_3 = self.text.strip('%H:%M:%S') # 去掉时间戳内容
            data_4 = time.strftime(data_1[0]) # 获取时间戳
            data_5 = data_3 + data_4

            try:
                text = substitute_variable(data_5)
                self.driver.find_element(By.XPATH, self.xpath).send_keys(text)
            except Exception:
                raise error_reminder('xpath_send_keys')

    def xpath_frame(self): # 切换框架
        try:
            ele = self.driver.find_element(By.XPATH, self.xpath)
        except Exception:
            raise error_reminder('xpath_frame')
        self.driver.switch_to.frame(ele)
        time.sleep(2)

    def xpath_file(self): # 上传附件
        file_current_path = '{}{}{}{}上传文件'.format(
            os.path.dirname(os.path.dirname(__file__)), os.sep, 'Auto_file', os.sep
        )  # 获取存放文件路径
        file_current_judge = []
        file_path = []
        file_quotation_mark = '""'  # 用来占位文件
        file_list = re.split(',', self.text)  # 获取所有文件名，以列表形式展现

        for i in file_list:
            file = '"{}"'.format(i)  # 重新命名文件名，格式为"文件名"
            file_path.append(file)  # 创建文件名列表

        for root, dirs, files in os.walk(file_current_path): # 获取上传文件下的所有文件名
            file_current_judge = files

        for file_01 in file_list: # 判断excel文档上传的文件名和上传文件的文件名是否一致
            for file_02 in file_current_judge:
                if file_02 != file_current_judge[-1]:
                    if file_02 == file_01:
                        break
                    else:
                        pass
                else:
                    if file_02 == file_01:
                        break
                    else:
                        raise error_reminder('xpath_file_01', file_01=file_01)

        if len(file_path) > 10:  # 上传文件数量大于10报错
            raise error_reminder('xpath_file_02')

        while len(file_path) < 10:  # 判断是否大于11，目前只允许上传10个文件
            file_path.append(file_quotation_mark)  # 填满10个文件位置

        try:
            self.driver.find_element(By.XPATH, self.xpath).click()
        except Exception:
            raise error_reminder('xpath_file_03')

        file_1 = '{}{}{}{}{}'.format(file_path[0], file_path[1], file_path[2], file_path[3], file_path[4])
        file_2 = '{}{}{}{}{}'.format(file_path[5], file_path[6], file_path[7], file_path[8], file_path[9])
        file_sun = '{}{}'.format(file_1, file_2)  # 分两次，相加文件

        try:
            app = pywinauto.Desktop()  # 使用pywinauto来选择文件
            dlg = app["打开"]  # 选择文件上传的窗口
            dlg["Toolbar3"].click()  # 选择文件地址输入框
            send_keys(file_current_path)  # 键盘输入上传文件的路径
            send_keys("{VK_RETURN}")  # 键盘输入回车，打开该路径
            dlg["文件名(&N):Edit"].type_keys(file_sun)  # 选中文件名输入框，输入文件名
            dlg["打开(&O)"].click()  # 点击打开
            try:
                dlg["打开(&O)"].click()  # 点击打开
            except Exception:
                pass
        except Exception:
            raise error_reminder('xpath_file_03')
        else:
            time.sleep(2)

    def xpath_roll(self): # 滑动滚动条
        try:
            js = self.driver.find_element(By.XPATH, self.xpath)
        except Exception:
            raise error_reminder('xpath_roll')
        else:
            self.driver.execute_script('arguments[0].scrollIntoView()', js)

    def xpath_clear(self):  # 清空文本框
        try:
            self.driver.find_element(By.XPATH, self.xpath).send_keys(Keys.CONTROL, 'a')
            self.driver.find_element(By.XPATH, self.xpath).send_keys(Keys.DELETE)
        except Exception:
            raise error_reminder('xpath_clear')

    def xpath_timeAndSpace(self): # 填写时间控件
        try:
            try:
                js = self.driver.find_element(By.XPATH, self.xpath)
                self.driver.execute_script('arguments[0].removeAttribute("readonly");', js)
            except Exception:
                self.driver.find_element(By.XPATH, self.xpath).send_keys(self.text)
            else:
                js.send_keys(self.text)
        except Exception:
            raise error_reminder('xpath_timeAndSpace')

    def xpath_text(self): # 获取文本
        if '-->' in(self.text):
            data = re.split('-->', self.text)

            capture_value = re.split(',', data[1])
            if len(capture_value) != 2:
                raise error_reminder('xpath_text_05', text=data[1])

            try:
                text_value_all = self.driver.find_element(By.XPATH, self.xpath).text # 获取文本
            except Exception:
                raise error_reminder('xpath_text_01')
            else:
                value = re.compile('\{}(.*?)\{}'.format(capture_value[0], capture_value[1]))
                capture = value.findall(text_value_all) # 循环整个文本，获取共有多少个截取片段，最终生成列表文本
                # capture：文本列表
                if capture == []:
                    raise error_reminder('xpath_text_03', text=capture)

                text_value_capture = ''  #
                text_value_capture_all = []
                text_variable_value = self.text_variable(data[0])

                if len(capture) != len(text_variable_value[1]):
                    raise error_reminder('xpath_text_06', text='变量数：{}，文本数：{}'.format(len(text_variable_value[1]), len(capture)))

                order = 0
                for num in text_variable_value[0]:
                    if data[0][num[0]] + data[0][num[1]] == '【】':
                        text_value_capture = capture_value[0] + capture[order] + capture_value[1]
                    elif  data[0][num[0]] + data[0][num[1]] == '《》':
                        text_value_capture = capture[order]
                    order += 1

                    text_value_capture_all.append(text_value_capture)

            return text_variable_value[1], text_value_capture_all

        elif '-->' not in(self.text):
            capture = []
            try:
                text_value_capture_all = self.driver.find_element(By.XPATH, self.xpath).text
            except Exception:
                raise error_reminder('xpath_text_01')
            else:
                text_variable_value = self.text_variable(self.text)
                capture.append(text_value_capture_all)

                if len(capture) != len(text_variable_value[1]):
                    raise error_reminder('xpath_text_06', text='变量数：{}，文本数：{}'.format(len(text_variable_value[1]), len(capture)))

            return text_variable_value[1], text_value_capture_all




