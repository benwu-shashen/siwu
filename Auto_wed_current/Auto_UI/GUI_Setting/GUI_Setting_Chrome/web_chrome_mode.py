from Auto_wed_current.Auto_UI.GUI_Setting.__init__ import set_property_data
from Auto_wed_current.Auto_driver.driver_class import driver

class web_chrome_mode(set_property_data):
    def __init__(self):
        super().__init__()

    def set_normal_mode(self):
        driver.mode = '启动正常模式'  # 正常模式
        driver()

    def set_incognito_mode(self): # 无痕模式
        driver.mode = '启动无痕模式'
        driver()



