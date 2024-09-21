import csv

from Auto_wed_current.Auto_base.error_reminder import error_reminder
from Auto_wed_current.Auto_base.filename import filename


def setting_csv():
    path = filename().filename_func(r'\Auto_file\配置文件\test_setting.csv')
    with open(path, 'r', encoding='utf-8') as f:
        csv_all = csv.reader(f)
        csv_data = []
        for csv_any in csv_all:
            csv_data.append(csv_any)

    if csv_data[0] != ['[是否报错截图]']:
        raise error_reminder('setting_csv_01') # 报错提示

    try:
        csv_data[1]
    except Exception:
        raise error_reminder('setting_csv_02')

    if csv_data[1][0] not in ('是', '否'):
        raise error_reminder('setting_csv_03', csv_data=csv_data[1][0])

    return csv_data
