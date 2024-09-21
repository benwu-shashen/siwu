from time import sleep
from Auto_wed_current.Auto_driver.driver_class import driver
from Auto_wed_current.Auto_UI.GUI_Setting.__init__ import set_property_data

class web_chrome(set_property_data):
    def __init__(self):
        super().__init__()

    def driver_chrom(self):
        driver()  # 启动浏览器



