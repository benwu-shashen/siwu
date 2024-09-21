import csv

from Auto_wed_current.Auto_base.error_reminder import error_reminder
from Auto_wed_current.Auto_base.filename import filename

"""
解析csv文件
"""

def data_csv():
    # with open(os.path.dirname(__file__) + os.sep + '配置文件' + os.sep + 'test_pattern.csv', 'r', encoding='utf-8') as e:
    #     csv_all_pattern = csv.reader(e)
    #     csv_data_pattern = []
    #     for csv_any_pattern in csv_all_pattern:
    #         csv_data_pattern.append(csv_any_pattern)
    #
    #     if csv_data_pattern[0][0] != '[执行模式]':
    #         raise error_reminder('data_csv_01')  # 报错提示
    #
    #     if csv_data_pattern[1][0] not in('调试模式', '基础模式', 'uniitest模式'):
    #         raise error_reminder('data_csv_08', csv_data=csv_data_pattern[1][0])  # 报错提示
    path = filename().filename_func(r'\Auto_file\配置文件\test_data.csv')
    with open(path, 'r', encoding='utf-8') as f:
        csv_all = csv.reader(f)
        csv_data = []
        for csv_any in csv_all:
            csv_data.append(csv_any)

    del csv_data[0]

    return csv_data

