import os
import shutil
import time

from selenium.webdriver.common.by import By

from Auto_wed_current.Auto_base.error_reminder import error_reminder
from Auto_wed_current.Auto_base.filename import filename
from Auto_wed_current.Auto_base.wait import driver_wait
from Auto_wed_current.Auto_driver.driver_class import driver_class


def screenshot(row, xpath, account, error, screenshot, wait_time, excel_file, excel_sheet):
    wait = driver_wait(row, xpath, account, error, wait_time) # 获取显性等待实例，该实例判断元素是否可见
    driver = driver_class().driver_Chrome(account)  # 定义driver实例

    if screenshot == '是': # 判断是否截图
        if xpath == '其他操作':
            time.sleep(1)
            img = str(row) + '.png'
            driver.save_screenshot(img)
            src = os.path.join(os.getcwd() + os.sep + img)
            excel_file_dir = filename().filename(r'\Auto_file\自动化截图\{}'.format(excel_file))
            excel_sheet_dir = excel_file_dir + os.sep + excel_sheet

            excel_file_judge = os.path.exists(excel_file_dir)  # 判断文件是否存在
            if excel_file_judge == True:
                try:
                    os.mkdir(excel_sheet_dir)
                except Exception:
                    pass

            else:
                os.mkdir(excel_file_dir)

                excel_sheet_judge = os.path.exists(excel_sheet_dir)
                if excel_sheet_judge == True:
                    os.remove(img)
                else:
                    os.mkdir(excel_sheet_dir)

            try:
                shutil.move(src, excel_sheet_dir) # 移动截图
            except Exception:
                raise error_reminder('screenshot_01', img=img)

        elif xpath == '其他操作':
            wait.visibility_of()
            ele = driver.find_element(By.XPATH, xpath)
            driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", ele, "border: 3px solid yellow;")

            time.sleep(1)
            img = str(row) + '.png'
            driver = driver_class().driver_Chrome(account)
            driver.save_screenshot(img)

            driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", ele, "")
            src = os.path.join(os.getcwd() + os.sep + img)
            excel_file_dir = filename().filename(r'\Auto_file\自动化截图\{}'.format(excel_file))
            excel_sheet_dir = excel_file_dir + os.sep + excel_sheet

            excel_file_judge = os.path.exists(excel_file_dir)  # 判断文件是否存在
            if excel_file_judge == True:
                try:
                    os.mkdir(excel_sheet_dir)
                except Exception:
                    pass

            else:
                os.mkdir(excel_file_dir)
                excel_sheet_judge = os.path.exists(excel_sheet_dir) # 判断sheet文件夹是否存在

                if excel_sheet_judge == True:
                    os.remove(img)
                else:
                    os.mkdir(excel_sheet_dir)

            try:
                shutil.move(src, excel_sheet_dir)  # 移动截图
            except Exception:
                raise error_reminder('screenshot_01', img=img)




