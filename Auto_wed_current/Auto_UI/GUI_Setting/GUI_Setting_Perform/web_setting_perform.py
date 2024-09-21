from Auto_wed_current.Auto_UI.GUI_Setting.__init__ import set_property_data
from Auto_wed_current.Auto_UI.GUI_Setting.GUI_Setting_Chrome.web_chrome_mode import web_chrome_mode
from Auto_wed_current.Auto_driver.driver_class import driver


class web_perform_func(set_property_data):
    def __init__(self):
        super().__init__()

        self.cm = web_chrome_mode() # 浏览器模式设置
        self.test = self.test # 一个bug，需要这样写才会触发信号
        self.perform_connect()

    def perform_connect(self):
        self.pushButton_normal_mode.clicked.connect(self.cm.set_normal_mode) # 设置浏览器模式
        self.pushButton_incognito_mode.clicked.connect(self.cm.set_incognito_mode) # 重启浏览器

    def test(self): # 不能删
        pass