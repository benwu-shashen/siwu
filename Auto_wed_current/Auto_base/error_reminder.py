from datetime import datetime

class error_reminder(Exception):
    def __init__(self,
                 function_name,
                 row_replace=None,
                 file_01=None,
                 csv_data=None,
                 excel_sheet_dir=None,
                 img=None,
                 file=None,
                 sheet=None,
                 text=None
                 ):

        self.function_name = function_name
        self.row_replace = row_replace
        self.file_01 = file_01
        self.csv_data = csv_data
        self.excel_sheet_dir = excel_sheet_dir
        self.img = img
        self.file = file
        self.sheet = sheet
        self.text = text

    def error_file_sheet(self):
        self.error_location = '[{}]>[{}]>[第{}行]报错，'.format(self.excel_file, self.excel_sheet, self.row)
        return self.error_location

    def text_Edit_error(self, result):
        curr_time = datetime.now()
        curr_str = curr_time.strftime('%Y-%m-%d %H:%M:%S')
        print_result = '{}>>>{}'.format(curr_str, result)
        self.perform_error(print_result)

    def __str__(self):
        # Auto_base报错提示
        if self.function_name in ['error_action', 'error_xpath']:  # error.py文件报错信息提示
            text = '{}请检查【操作】数据正确性'.format(self.error_file_sheet())
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'error_account':
            text = '{}【account】数据只能填写为【account_01】'.format(self.error_file_sheet())
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'error_text':
            text = '{}请检查【内容输入】数据正确性'.format(self.error_file_sheet())
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'error_screenshot_01':
            text = '{}报错截图-{}已存在，请删除'.format(self.error_file_sheet(), self.img)
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'screenshot_01':
            text = '{}自动化截图-{}已存在，请删除'.format(self.error_file_sheet(), self.img)
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'wait_element':  # wait.py文件报错信息提示
            text = '{}页面等待超时'.format(self.error_file_sheet())
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'handles_get':
            text = '浏览器已被断开，请重新打开浏览器'
            self.text_Edit_error(text)
            return text

        # Auto_carry报错提示 ----------------
        elif self.function_name == 'action_handles_01':  # action.py文件报错信息提示
            text = '{}窗口不存在,请检查【内容输入】数据正确性'.format(self.error_file_sheet())
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'action_handles_02':
            text = '{}句柄不存在,请检查【内容输入】数据正确性'.format(self.error_file_sheet())
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'action_move_by_offset':
            text = '{}超出坐标索引范围，请降低坐标范围'.format(self.error_file_sheet())
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'action_format':
            text = '{}格式错误，请按【x,y-->内容】格式填写'.format(self.error_file_sheet())
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'action_format_01':
            text = '{}[{}], 格式错误，请按照[x,y]填写'.format(self.error_file_sheet(), self.text)
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'action_format_02':
            text = '{}[{}], 格式错误，坐标只能填写数字，不能填写其他字符'.format(self.error_file_sheet(), self.text)
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'action_format_03':
            text = '{}文本不存在'.format(self.error_file_sheet())
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'action_format_04':
            text = '{}{}，截取内容为空，请确定截取文本你是否正确'.format(self.error_file_sheet(), self.text)
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'action_format_05':
            text = '{}[{}]，变量数与文本数不对等，请重新获取'.format(self.error_file_sheet(), self.text)
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'action_format_06':
            text = '{}[{}]，截取值格式错误，请按照[截取头,截取尾]格式填写'.format(self.error_file_sheet(), self.text)
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'xpath_click':  # xpath.py文件报错信息提示
            text = '{}【点击】操作错误，请检查【操作】数据正确性'.format(self.error_file_sheet())
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'xpath_send_keys':
            text = '{}【文本框输入】操作错误，请检查数据正确性'.format(self.error_file_sheet())
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'xpath_frame':
            text = '{}【切换框架】操作错误，请检查【操作】数据正确性'.format(self.error_file_sheet())
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'xpath_file_03':
            text = '{}【上传附件】操作错误，请检查【操作】数据正确性'.format(self.error_file_sheet())
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'xpath_file_01':
            text = '{}上传文件名错误，错误文件名:{}，请点击编辑附件，维护上传附件'.format(self.error_file_sheet(), self.file_01)
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'xpath_file_02':
            text = '{}[{}]>[{}]文件上传超过数量，只能上传10个文件'.format(self.error_file_sheet(), self.error_file_sheet()[0], self.error_file_sheet()[1])
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'xpath_roll':
            text = '{}【滑动滚动条】操作错误，请检查【操作】数据正确性'.format(self.error_file_sheet())
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'xpath_clear':
            text = '{}【清空文本框】操作错误，请检查【操作】数据正确性'.format(self.error_file_sheet())
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'xpath_timeAndSpace':
            text = '{}【填写时间控件】操作错误，请检查【操作】数据正确性'.format(self.error_file_sheet())
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'xpath_text_01':
            text = '{}文本不存在'.format(self.error_file_sheet())
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'xpath_text_02':
            text = '{}[{}]，变量格式不正确，请按照[【变量1】]或[《变量1》]格式填写'.format(self.error_file_sheet(), self.text)
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'xpath_text_03':
            text = '{}{}，截取内容为空，请确定截取文本你是否正确'.format(self.error_file_sheet(), self.text)
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'xpath_text_04':
            text = '{}[{}]，变量值不能为空，请按照[【变量1】]或[《变量1》]格式填写'.format(self.error_file_sheet(), self.text)
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'xpath_text_05':
            text = '{}[{}]，截取值格式错误，请按照[截取头,截取尾]格式填写'.format(self.error_file_sheet(), self.text)
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'xpath_text_06':
            text = '{}[{}]，变量数与文本数不对等，请重新获取'.format(self.error_file_sheet(), self.text)
            self.text_Edit_error(text)
            return text

        # Auto_data报错提示 ---------------
        elif self.function_name == 'excel_account':  # excel.py文件报错信息提示
            text = '{}请填写[{}]>[{}]【account】列'.format(self.error_file_sheet(), self.error_file_sheet()[0], self.error_file_sheet()[1])
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'excel_file':
            text = '[{}]文件不存在，或sheet表内容为空'.format(self.file)
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'excel_sheet':
            text = '[{}]工作表不存在'.format(self.sheet)
            self.text_Edit_error(text)
            return text

        # Auto_execute报错提示
        # elif self.function_name == 'execute_function_replace_01': # execute_while.py文件报错信息提示
        #     text = '{}替换文件第[{}]行填写错误，不可小于上一行填写的替换编号'.format(self.error_file_sheet(), self.row_replace)
        #     self.text_Edit_error(text)
        #     return text

        elif self.function_name == 'execute_function_replace_02':
            text = '替换模板第[{}]行[account]有值，当[替换编号]为空，请注意填写[替换编号]，否则结束流程'.format(self.row_replace)
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'execute': # execute.py文件报错信息提示
            text = '配置文件中，文件名不能相同'
            self.text_Edit_error(text)
            return text

        # Auto_file报错提示
        # 暂时注释下，感觉都没有用
        # elif self.function_name == 'data_csv_01':  # data_csv.py文件报错信息提示
        #     text = '格式错误，请按【[文件名],[强制等待],[是否替换数据],[工作表名]】格式填写'
        #     self.text_Edit_error(text)
        #     return text
        #
        # elif self.function_name == 'data_csv_02':
        #     text = '[文件名]不能为空'
        #     self.text_Edit_error(text)
        #     return text
        #
        # elif self.function_name == 'data_csv_03':
        #     text = '[{}]的[强制等待]不能为空'.format(self.csv_data)
        #     self.text_Edit_error(text)
        #     return text
        #
        # elif self.function_name == 'data_csv_04':
        #     text = '[{}]的[强制等待]只能填写数字'.format(self.csv_data)
        #     self.text_Edit_error(text)
        #     return text
        #
        # elif self.function_name == 'data_csv_05':
        #     text = '[{}]的[是否替换数据]不能为空'.format(self.csv_data)
        #     self.text_Edit_error(text)
        #     return text
        #
        # elif self.function_name == 'data_csv_06':
        #     text = '[{}]的[是否替换数据]只能填写【是】或【否】'.format(self.csv_data)
        #     self.text_Edit_error(text)
        #     return text
        #
        # elif self.function_name == 'data_csv_07':
        #     text = '[{}]的[工作表名1]不能为空'.format(self.csv_data)
        #     self.text_Edit_error(text)
        #     return text

        elif self.function_name == 'data_csv_08':
            text = '[{}]的[执行模式]错误，只能填写调试模式, 基础模式, uniitest模式其中一个'.format(self.csv_data)
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'setting_csv_01':  # setting_csv.py文件报错信息提示
            text = '格式错误，请按【[是否报错截图]】格式填写'
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'setting_csv_02':
            text = '[是否报错截图]不能为空'
            self.text_Edit_error(text)
            return text

        elif self.function_name == 'setting_csv_03':
            text = '[{}]的[是否报错截图]只能填写【是】或【否】'.format(self.csv_data)
            self.text_Edit_error(text)
            return text
