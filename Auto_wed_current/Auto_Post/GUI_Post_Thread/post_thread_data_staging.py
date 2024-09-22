import os

import pandas as pd
from PyQt6.QtCore import QThread

from Auto_wed_current.Auto_base.filename import filename


class post_thread_data_staging(QThread): # 执行开始线程
    def __init__(self):
        super().__init__()
        self.filename_original = filename().filename_func(r'\Auto_file\接口CSV模板')

    def run(self):
        for filename in os.listdir(self.filename_original):
            if filename.endswith('.xls'):
                # 构造完整的文件路径
                file_path = os.path.join(self.filename_original, filename)

                # 读取 .xls 文件
                df = pd.read_excel(file_path)

                # 构造新的 .csv 文件名
                csv_filename = filename.replace('.xls', '.csv')
                csv_file_path = os.path.join(self.filename_original, csv_filename)

                # 保存为 .csv 文件
                df.to_csv(csv_file_path, index=False, encoding='utf-8')
                os.remove(file_path)
