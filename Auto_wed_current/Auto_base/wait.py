from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Auto_wed_current.Auto_base.error_reminder import error_reminder
from Auto_wed_current.Auto_driver.driver_class import driver_class

"""
显性等待封装
"""
class driver_wait(object):
    def __init__(self, row, xpath, account, error, wait_time, excel_file=None, excel_sheet=None):
        self.row = row
        self.xpath = xpath
        self.account = account
        self.error = error
        self.wait_time = wait_time
        self.excel_file = excel_file
        self.excel_sheet = excel_sheet
        self.driver = driver_class().driver_Chrome(self.account)

    def wait_element(self):
        try:
            WebDriverWait(self.driver, self.wait_time).until(EC.presence_of_all_elements_located((By.XPATH, self.xpath)))
        except Exception:
            raise error_reminder('wait_element')

    def visibility_of(self): # 判断元素是否可见
        driver = driver_class().driver_Chrome(self.account)
        try:
            WebDriverWait(driver, 15).until(EC.visibility_of_all_elements_located((By.XPATH, self.xpath)))
        except Exception:
            print('报错行数:' + str(self.error + 1))
