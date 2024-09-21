import shutil

from PyQt6.QtWidgets import QFileDialog

from Auto_wed_current.Auto_UI.GUI_Error.web_error import web_error
from Auto_wed_current.Auto_base.filename import filename


class web_download_template:
    def __init__(self):
        self.we = web_error()

    def download_file(self):
        dir = QFileDialog()
        text = dir.getExistingDirectory(None, "选择文件夹路径", 'C:/')  # 选择文件夹位置
        file = filename().filename_func(r'\Auto_file\模板下载\模板下载.zip')

        if text != None:
            try:
                shutil.copy(file, text)

            except Exception:
                self.we.box_warning('选择路径无效')

            else:
                self.we.box_information('模板下载.zip压缩包已下载')