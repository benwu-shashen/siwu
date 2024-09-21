import traceback
from datetime import datetime

from Auto_wed_current.Auto_UI.GUI_Logging.web_logging_func import web_logging_write
from Auto_wed_current.Auto_base.base import screenshot
from Auto_wed_current.Auto_base.error import error_all
from Auto_wed_current.Auto_base.error_reminder import error_reminder
from Auto_wed_current.Auto_base.handles import handles
from Auto_wed_current.Auto_base.wait import driver_wait
from Auto_wed_current.Auto_carry.action import action_judge
from Auto_wed_current.Auto_carry.xpath import driver_xpath
from Auto_wed_current.Auto_data.excel import excel_all

"""
执行自动化脚本
"""
class execute_while_value(object):
    def __init__(self, csv_dict, excel_file, list, handles_append, wait_time, Edit=None, data_judge=None, test_sum_data=None, test_sum_data_replace=None):
        self.csv_dict = csv_dict
        self.excel_file = excel_file
        self.list = list
        self.handles_append = handles_append
        self.wait_time = wait_time
        self.data_judge = data_judge
        self.test_sum_data = test_sum_data
        self.test_sum_data_replace = test_sum_data_replace
        self.Edit = Edit

    def text_Edit(self, result):
        print(result)
        curr_time = datetime.now()
        curr_str = curr_time.strftime('%Y-%m-%d %H:%M:%S')
        print_result = '{}>>>{}'.format(curr_str, result)
        self.Edit(print_result)

    def execute_function_original(self):
        for excel_sheet in self.csv_dict[self.excel_file][1].split(','):
            row = 1
            text_dirt = {}

            try:
                while True:
                    self.judge_pa_re() # 暂停线程，取自web_thread
                    # if row==4: # 断点使用
                    #     print("ok")
                    error = row
                    excel = excel_all(row, self.excel_file, excel_sheet, self.data_judge)
                    account = excel.excel_account()  # 获取account值
                    xpath = excel.excel_xpath()  # 获取xpath值

                    if xpath == None or xpath == '':
                        result = '[{}]>[{}]执行完毕，结束行数第{}行'.format(self.excel_file, excel_sheet, row - 1)
                        self.text_Edit(result)
                        succeed_current_append = [self.list, excel_sheet, row, '执行原始数据成功，结束行数第']
                        self.test_sum_data.append(succeed_current_append)
                        self.list += 1
                        break

                    action = excel.excel_action()  # 获取操作值
                    text = excel.excel_text()  # 获取文本框内容
                    error_warning = error_all(row, xpath, action, account, text, self.excel_file, excel_sheet)  # 获取报错提示实例
                    error_reminder.excel_file = self.excel_file # 报错excel
                    error_reminder.excel_sheet = excel_sheet # 报错sheet
                    error_reminder.row = row # 报错行数
                    error_warning.error_account() # 【account】数据验证报错提示
                    screen = excel.excel_screenshot()  # 是否截图
                    element = driver_xpath(row, xpath, account, error, text, self.excel_file, excel_sheet) # 执行操作
                    handles_get = handles(action, text, account, self.handles_append).handles_get()

                    if xpath == '生成用例':
                        row += 1

                    elif xpath == '其他操作':
                        try:
                            screenshot(row, xpath, account, error, screen, self.wait_time, self.excel_file, excel_sheet)
                            error_warning.error_action()# 【操作】数据验证报错提示
                            error_warning.error_text() # 【内容输入】数据验证报错提示

                            if action == '其他-坐标-获取文本':
                                variate, text_value = action_judge(row, action, account, text, handles_get, text_dirt)  # 最后执行操作
                                get_dirt = dict(zip(variate, text_value))
                                text_dirt.update(get_dirt)

                            elif action != '其他-坐标-获取文本':
                                if action == '其他-清除句柄':
                                    self.handles_append = action_judge(row, action, account, text, handles_get, text_dirt)
                                elif action != '其他-清除句柄':
                                    action_judge(row, action, account, text, handles_get, text_dirt) # 最后执行操作

                        except Exception:
                            lose_current_append = [self.list, excel_sheet, row, '执行原始数据失败，失败行数第']
                            self.test_sum_data.append(lose_current_append)
                            self.list += 1
                            error_warning.error_screenshot()
                            raise

                        row +=1

                    elif xpath != None and xpath != '':
                        try:
                            screenshot(row, xpath, account, error, screen, self.wait_time, self.excel_file, excel_sheet)
                            error_warning.error_xpath() # 【操作】数据验证报错提示
                            error_warning.error_text() # 【内容输入】数据验证报错提示
                            driver_wait(row, xpath, account, error, self.wait_time, excel_file=self.excel_file, excel_sheet=excel_sheet).wait_element()

                            if xpath != '':
                                if action == 'xpath-点击':
                                    element.xpath_click()

                                elif action == 'xpath-文本框输入':
                                    element.xpath_send_keys(text_dirt)

                                elif action == 'xpath-切换框架':
                                    element.xpath_frame()

                                elif action == 'xpath-上传附件':
                                    element.xpath_file()

                                elif action == 'xpath-滑动滚动条':
                                    element.xpath_roll()

                                elif action == 'xpath-清空文本框':
                                    element.xpath_clear()

                                elif action == 'xpath-填写时间控件':
                                    element.xpath_timeAndSpace()

                                elif action == 'xpath-获取文本':
                                    variate, text_value = element.xpath_text()
                                    get_dirt = dict(zip(variate, text_value))
                                    text_dirt.update(get_dirt)

                        except Exception:
                            lose_current_append = [self.list, excel_sheet, row, '执行原始数据失败，失败行数第']
                            self.test_sum_data.append(lose_current_append)
                            self.list += 1
                            error_warning.error_screenshot()
                            raise

                        row +=1

            except Exception:
                logging_write = web_logging_write(traceback.format_exc()) # 返回报错等级和提示
                error_text = logging_write.log_error_data()
                self.Edit_logging(error_text)

        return self.excel_file, self.test_sum_data

    def execute_function_replace(self):

        for excel_sheet in self.csv_dict[self.excel_file]:
            row = 1 # 原始数据行数
            row_replace = 1 # 替换数据行数
            data_original = '原始数据'
            data_replace = '替换数据'
            data_judge = ''
            debug = '成功'
            text_dirt = {}
            debug_class = '一级'

            try:
                while True:
                    # if row_replace == 1: # 断点使用，如果报错第5行，则要-1
                    #     print(row_replace)
                    if debug_class == '二级':
                        break

                    num = excel_all(row, self.excel_file, excel_sheet, data_replace, row_replace=row_replace).excel_replace_num()

                    if debug == '失败':
                        while True:
                            num = excel_all(row, self.excel_file, excel_sheet, data_replace, row_replace=row_replace).excel_replace_num()

                            if num == '替换完成':
                                row_replace += 1
                                self.list += 1
                                break

                            elif num == '' or num == None:
                                break

                            elif num != '替换完成':
                                row_replace += 1
                                continue

                    row = 1

                    if num == '' or num == None:
                        account_value = excel_all(row, self.excel_file, excel_sheet, data_replace, row_replace=row_replace).excel_account()

                        if account_value:
                            raise error_reminder('execute_function_replace_02', row_replace=row_replace)
                        else:
                            break

                    try:
                        while True:
                            # if row == 4: # 断点使用
                            #     print("ok")
                            excel = excel_all(row, self.excel_file, excel_sheet, data_replace, row_replace=row_replace)
                            excel_1 = excel_all(row, self.excel_file, excel_sheet, data_replace, row_replace=row_replace + 1)
                            num = excel.excel_replace_num()
                            num_1 = excel_1.excel_replace_num()

                            if num == '替换完成':
                                excel = excel_all(row, self.excel_file, excel_sheet, data_original)
                                data_judge = data_original

                            elif num == None or num == '':
                                excel = excel_all(row, self.excel_file, excel_sheet, data_original)
                                if row == 1:
                                    result = '[{}]>[{}]替换完毕，结束行数第{}行'.format(self.excel_file, excel_sheet, row_replace - 1)
                                    # self.Edit(result)
                                    break

                                elif row != 1:
                                    data_judge = data_original

                            elif int(num) != row: # 判断替换编号不能大于原始编号
                                if int(num) < row:
                                    raise error_reminder('execute_function_replace_01', row_replace=row_replace)

                                elif int(num) > row:
                                    excel = excel_all(row, self.excel_file, excel_sheet, data_original)
                                    data_judge = data_original

                            elif int(num) == row:
                                if num_1 == row:
                                    excel = excel_all(row, self.excel_file, excel_sheet, data_replace, row_replace=row_replace)

                                    data_judge = data_replace
                                    row_replace += 1

                                elif num_1 != row:
                                    excel = excel_all(row, self.excel_file, excel_sheet, data_replace, row_replace=row_replace)

                                    data_judge = data_replace
                                    row_replace += 1

                            error = row
                            account = excel.excel_account()  # 获取account值
                            xpath = excel.excel_xpath()  # 获取xpath值

                            if xpath == None or xpath == '':
                                if num == None or num == '':
                                    if row_replace != '替换完成':
                                        result = '[{}]>[{}]>[第{}行]替换完成，[替换文件]截止第{}行替换成功'.format(self.excel_file, excel_sheet, row - 1, row_replace - 1)
                                        # self.Edit(result)
                                        result = '[{}]>[{}]替换完毕，结束行数第{}行'.format(self.excel_file, excel_sheet, row_replace - 1)
                                        # self.Edit(result)

                                        self.succeed_current_append_replace = [self.list, excel_sheet, row_replace - 1, '执行替换数据成功，结束行数第']
                                    elif row_replace == '替换完成':
                                        result = '[{}]>[{}]替换完毕，结束行数第{}行'.format(self.excel_file, excel_sheet, row_replace)
                                        # self.Edit(result)

                                        self.succeed_current_append_replace = [self.list, excel_sheet, row_replace, '执行替换数据成功，结束行数第']

                                    self.test_sum_data_replace.append(self.succeed_current_append_replace)
                                    break

                                elif num not in(None, ''):
                                    result = '[{}]>[{}]>[第{}行]替换完成，[替换文件]截止第{}行替换成功'.format(self.excel_file, excel_sheet, row - 1, row_replace)
                                    # self.Edit(result)

                                    succeed_current_append_replace = [self.list, excel_sheet, row_replace, '执行替换数据成功，结束行数第']
                                    self.test_sum_data_replace.append(succeed_current_append_replace)
                                    self.list += 1
                                    row = 1

                                    if num == '替换完成':
                                        row_replace += 1
                                    continue
                            action = excel.excel_action()  # 获取操作值
                            text = excel.excel_text()  # 获取文本框内容
                            error_warning = error_all(row, xpath, action, account, text, self.excel_file, excel_sheet, row_replace=row_replace, data_judge=data_judge)  # 获取报错提示实例
                            error_reminder.excel_file = self.excel_file
                            error_reminder.excel_sheet = excel_sheet
                            error_reminder.row = row
                            error_warning.error_account() # 【account】数据验证报错提示
                            screen = excel.excel_screenshot()  # 是否截图
                            element = driver_xpath(row, xpath, account, error, text, self.excel_file, excel_sheet) # 执行操作
                            handles_get = handles(action, text, account, self.handles_append).handles_get()

                            if xpath == '生成用例':
                                row += 1

                            elif xpath == '其他操作':
                                try:
                                    screenshot(row, xpath, account, error, screen, self.wait_time, self.excel_file, excel_sheet)
                                    error_warning.error_action()# 【操作】数据验证报错提示
                                    error_warning.error_text() # 【内容输入】数据验证报错提示

                                    if action == '其他-坐标-获取文本':
                                        variate, text_value = action_judge(row, action, account, text, handles_get,text_dirt)  # 最后执行操作
                                        get_dirt = dict(zip(variate, text_value))
                                        text_dirt.update(get_dirt)

                                    elif action != '其他-坐标-获取文本':
                                        if action == '其他-清除句柄':
                                            self.handles_append = action_judge(row, action, account, text, handles_get, text_dirt)
                                        elif action != '其他-清除句柄':
                                            action_judge(row, action, account, text, handles_get, text_dirt)  # 最后执行操作

                                except Exception:
                                    lose_current_append = [self.list, excel_sheet, row_replace - 1, '执行替换数据失败，失败行数第']
                                    self.test_sum_data_replace.append(lose_current_append)
                                    error_warning.error_screenshot()
                                    raise

                                if num_1 != row:
                                    row += 1

                            elif xpath != None and xpath != '':
                                try:
                                    screenshot(row, xpath, account, error, screen, self.wait_time, self.excel_file, excel_sheet)
                                    error_warning.error_xpath() # 【操作】数据验证报错提示
                                    error_warning.error_text() # 【内容输入】数据验证报错提示
                                    driver_wait(row, xpath, account, error, self.wait_time, excel_file=self.excel_file, excel_sheet=excel_sheet).wait_element()

                                    if xpath != '':
                                        if action == 'xpath-点击':
                                            element.xpath_click()

                                        elif action == 'xpath-文本框输入':
                                            element.xpath_send_keys(text_dirt)

                                        elif action == 'xpath-切换框架':
                                            element.xpath_frame()

                                        elif action == 'xpath-上传附件':
                                            element.xpath_file()

                                        elif action == 'xpath-滑动滚动条':
                                            element.xpath_roll()

                                        elif action == 'xpath-清空文本框':
                                            element.xpath_clear()

                                        elif action == 'xpath-填写时间控件':
                                            element.xpath_timeAndSpace()

                                        elif action == 'xpath-获取文本':
                                            variate, text_value = element.xpath_text()
                                            get_dirt = dict(zip(variate, text_value))
                                            text_dirt.update(get_dirt)

                                except Exception:
                                    lose_current_append = [self.list, excel_sheet, row_replace, '执行替换数据失败，失败行数第']
                                    self.test_sum_data_replace.append(lose_current_append)
                                    error_warning.error_screenshot()
                                    # 暂时添加----------------------
                                    action_judge(row, '其他-切换窗口', account, 1, handles_get, text_dirt)
                                    self.handles_append = action_judge(row, '其他-清除句柄', account, 2, handles_get, text_dirt)
                                    # 暂时添加----------------------

                                    debug = '失败'
                                    raise

                                if num_1 != row:
                                    row +=1

                    except Exception:
                        debug_class = '二级'
                        web_logging_write(traceback.print_exc()) # 记录日志到窗口，输出详细报错信息

            except Exception:
                if debug_class == '一级':
                    web_logging_write(traceback.print_exc()) # 记录日志到窗口，输出详细报错信息

                elif debug_class == '二级':
                    pass

        return self.excel_file, self.test_sum_data_replace
