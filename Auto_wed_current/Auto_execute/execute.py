from Auto_wed_current.Auto_execute.execute_while import execute_while_value
from Auto_wed_current.Auto_file.data_csv import data_csv

"""
执行自动化脚本
"""

class execute(object):
    def __init__(self, Edit):
        self.Edit = Edit

    def execute_function(self):
        csv_data = data_csv()
        excel_csv = []
        sheet_csv = []

        for excel_data in range(len(csv_data)): # 循环执行csv文件内容
            excel_verify = []
            excel_verify.append(csv_data[excel_data][0])
            excel_verify.append(csv_data[excel_data][2])
            excel_verify.append(csv_data[excel_data][3])
            sheet_csv.append(excel_verify)
            excel_csv.append(csv_data[excel_data][1])

        csv_dict = dict(zip(excel_csv, sheet_csv))
        test_sum_data_file = {}
        test_sum_data_file_re = {}
        test_sum_data_file_update = {}
        replace_data_sum = []

        for excel_file in csv_dict:
            list = 1
            test_sum_data = []
            test_sum_data_replace = []
            handles_append = []
            wait_time = csv_dict[excel_file][2]
            template_data = csv_dict[excel_file][0]

            if template_data == '原始模板':
                data_judge = '原始数据'
                execute_value = execute_while_value(csv_dict, excel_file, list, handles_append, wait_time, Edit=self.Edit, data_judge=data_judge, test_sum_data=test_sum_data)
                excel_file, test_sum_data = execute_value.execute_function_original()
                test_sum_data_file[excel_file] = test_sum_data
                test_sum_data_file_update.update(test_sum_data_file)
                replace_data_sum.append(template_data)

            elif template_data == '替换模板':
                execute_value = execute_while_value(csv_dict, excel_file, list, handles_append, wait_time, test_sum_data_replace=test_sum_data_replace)
                excel_file_replace, test_sum_data_replace = execute_value.execute_function_replace()
                test_sum_data_file_re[excel_file_replace] = test_sum_data_replace
                test_sum_data_file_update.update(test_sum_data_file_re)
                replace_data_sum.append(template_data)

        return replace_data_sum, test_sum_data_file_update

