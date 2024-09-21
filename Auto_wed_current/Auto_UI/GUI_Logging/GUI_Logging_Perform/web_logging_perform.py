from Auto_wed_current.Auto_UI.GUI_Logging.__init__ import log_property_data
from Auto_wed_current.Auto_UI.GUI_Error.web_error import web_error

class web_perform_func(log_property_data):
    def __init__(self):
        super().__init__()

        self.logging_perform_connect()
        self.test = self.test  # 一个bug，需要这样写才会触发信号

    def logging_perform_connect(self):
        # 清空文本
        self.pushButton_logging_clear.clicked.connect(self.logging_clear)

        # 关闭窗口
        self.pushButton_logging_close.clicked.connect(self.close)

    def logging_clear(self):
        self.textEdit_logging.clear()
        web_error().box_information('清除成功')

    def test(self): # 不能删
        pass