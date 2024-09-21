import time

from Auto_wed_current.Auto_execute.execute import execute
from Auto_wed_current.Auto_UI.GUI_Report.report_file.append_file import append_file

class execute_summary(object):
    def __init__(self, Edit):
        self.Edit = Edit
        # Edit_summary

    def execute_gui(self, text, title, judge=None):
        if title == 'file':
            self.Edit_summary(text, 'file') # 来自web_thread文件

        elif title == 'sheet':
            if judge == '失败':
                self.Edit_summary(text, 'sheet', judge='失败')

            elif judge == '成功':
                self.Edit_summary(text, 'sheet', judge='成功')

        elif title == 'summary':
            self.Edit_summary(text, 'summary')

    def execute_result(self):
        execute_data = execute(self.Edit).execute_function()
        execute_result = execute_data[1]
        time.sleep(1)
        count = 0

        total_result = {}

        for data_file in execute_result:
            lose = 0
            succeed = 0

            text = '执行[{}]文件：'.format(data_file)
            print(text, end='')
            self.execute_gui(text, 'file')
            if execute_data[0][count] == '原始模板':
                for data_sheet in execute_result[data_file]:
                    if data_sheet[3] == '执行原始数据失败，失败行数第':
                        text = '    {}、[{}]{}{}行'.format(
                            data_sheet[0],
                            data_sheet[1],
                            data_sheet[3],
                            data_sheet[2],
                        )
                        self.execute_gui(text, 'sheet', judge='失败')

                        data_sheet[3] = '执行\033[92m原始数据\033[91m失败，失败行数第'
                        print('\n   \033[91m {}、[{}]{}{}行 \033[0m'.format(
                            data_sheet[0],
                            data_sheet[1],
                            data_sheet[3],
                            data_sheet[2],
                        ), end='')
                        lose += 1

                    elif data_sheet[3] == '执行原始数据成功，结束行数第':
                        text = '    {}、[{}]{}{}行'.format(
                            data_sheet[0],
                            data_sheet[1],
                            data_sheet[3],
                            data_sheet[2] - 1,
                        )
                        self.execute_gui(text, 'sheet', judge='成功')

                        data_sheet[3] = '执行\033[92m原始数据\033[0m成功，结束行数第'
                        text = '\n    {}、[{}]{}{}行'.format(
                            data_sheet[0],
                            data_sheet[1],
                            data_sheet[3],
                            data_sheet[2] - 1,
                        )
                        print(text, end='')
                        succeed += 1

                count += 1

            elif execute_data[0][count] == '替换模板':
                for data_sheet in execute_result[data_file]:
                    if data_sheet[3] == '执行替换数据失败，失败行数第':
                        text = '    {}、[{}]{}{}行'.format(
                            data_sheet[0],
                            data_sheet[1],
                            data_sheet[3],
                            data_sheet[2],
                        )
                        self.execute_gui(text, 'sheet', judge='失败')

                        data_sheet[3] = '执行\033[93m替换数据\033[91m失败，失败行数第'
                        print('\n   \033[91m {}、[{}]{}{}行 \033[0m'.format(
                            data_sheet[0],
                            data_sheet[1],
                            data_sheet[3],
                            data_sheet[2],
                        ), end='')
                        lose += 1

                    elif data_sheet[3] == '执行替换数据成功，结束行数第':
                        text = '    {}、[{}]{}{}行'.format(
                            data_sheet[0],
                            data_sheet[1],
                            data_sheet[3],
                            data_sheet[2] - 1,
                        )
                        self.execute_gui(text, 'sheet', judge='成功')

                        data_sheet[3] = '执行\033[93m替换数据\033[0m成功，结束行数第'
                        print('\n    {}、[{}]{}{}行'.format(
                            data_sheet[0],
                            data_sheet[1],
                            data_sheet[3],
                            data_sheet[2] - 1,
                        ), end='')
                        succeed += 1

                count += 1

            text = '    共执行{}条， 成功数{}，失败数{}'.format(succeed+lose, succeed, lose)
            self.execute_gui(text, 'summary')

            print('\n    共执行{}条， 成功数{}，\033[91m 失败数{} \033[0m'.format(
                succeed+lose,
                succeed,
                lose
            ), end='\n')

            total_result[data_file] = '{},{},{}'.format(succeed+lose, succeed, lose)

        append_file().report_create_html(total_result)