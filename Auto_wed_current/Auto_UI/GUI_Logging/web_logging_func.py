import logging
import os
import sys
import time
import traceback

from Auto_wed_current.Auto_UI.GUI_Error.web_error import web_error
from Auto_wed_current.Auto_base.filename import filename
from Auto_wed_current.Auto_UI.GUI_Logging.__init__ import log_property_data

class wed_logging:
    def __init__(self):
        super().__init__()

        self.old_hook = sys.excepthook
        sys.excepthook = self.catch_exceptions

    def catch_exceptions(self, ty, value, test):
        """
            捕获异常，并弹窗显示
        :param ty: 异常的类型
        :param value: 异常的对象
        :param traceback: 异常的traceback
        """

        traceback_format = traceback.format_exception(ty, value, test)
        traceback_string = "".join(traceback_format)
        web_error().box_critical(traceback_string)
        web_logging_write(traceback_string)
        self.old_hook(ty, value, test)

class web_logging_write(log_property_data):
    def __init__(self, traceback_sprit):
        super().__init__()
        self.traceback_sprit = traceback_sprit

        print('\033[91m {} \033[0m'.format(self.traceback_sprit))
        self.log().error(traceback_sprit)

    def log(self):
        logger = logging.getLogger('web_UI')
        logger.setLevel(logging.DEBUG)

        log_name, mode = self.log_filename() # 一个月更换一次报告
        if mode == '原始':
            self.fh = logging.FileHandler(r'GUI_Logging\log_file\{}'.format(log_name), mode='a', encoding='utf-8')

        elif mode == '替换':
            self.fh = logging.FileHandler(r'GUI_Logging\log_file\{}'.format(log_name), mode='w', encoding='utf-8')

        self.fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.fh.setFormatter(formatter)
        logger.addHandler(self.fh)
        logger.handlers = logger.handlers[:1] # 去除所有重复打印日志，取第一个打印日志

        return logger

    def log_filename(self):
        name = filename().filename_func(r'\Auto_UI\GUI_Logging\log_file')
        for (root, dirs, file) in os.walk(name):  # 原始导入模板列表展示
            self.file_name = file

        curtime = time.strftime('%Y%m')

        if str(self.file_name[0])[0 : 6] != curtime:
            self.log_name = curtime + 'error.log'
            os.remove(name + r'\{}'.format(self.file_name[0]))
            self.mode = '替换'

        elif str(self.file_name[0])[0 : 6] == curtime:
            self.log_name = self.file_name[0]
            self.mode = '原始'

        return self.log_name, self.mode

    def log_error_data(self):
        return self.traceback_sprit

