import os

class filename:
    def __init__(self):
        pass

    def filename_func(self, path): # 使用方法filename().filename(r'\文件路径)
        dir = os.path.dirname
        parent = dir(__file__)  # 当前目录

        while True:
            parent_Current = os.path.basename(parent)
            if parent_Current == 'Auto_wed_current':
                return parent + path
            else:
                parent = os.path.dirname(parent)