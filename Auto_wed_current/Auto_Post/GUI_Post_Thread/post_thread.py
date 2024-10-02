from PyQt6.QtCore import pyqtSignal, QThread

from Auto_wed_current.Auto_Post.GUI_Post_Request.post_request import post_request
from Auto_wed_current.Auto_base.filename import filename


class execute_thread(QThread): # 执行开始线程
    # 定义线程信号
    set_Enabled_bf = pyqtSignal()
    set_Enabled_af = pyqtSignal()
    def __init__(self, post_combobox):
        super().__init__()
        self.path = filename().filename_func(r'\Auto_file\接口CSV模板')
        self.pr = post_request(self.path, self)
        self.post_combobox = post_combobox

    def bf(self):
        self.set_Enabled_bf.emit()

    def af(self):
        self.set_Enabled_af.emit()

    def run(self):
        self.pr.issue_resquest(self.post_combobox)


