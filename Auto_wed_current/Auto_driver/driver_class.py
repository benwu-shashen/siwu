import os
import subprocess

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

"""
连接当前浏览器，暂时注释，需要终端输入
chrome.exe --remote-debugging-port=9527 --user-data-dir="C:\selenium\AutomationProfile"
打开一个浏览器实例
"""

class driver:
    def __init__(self):
        if self.mode == '启动正常模式':
            subprocess.Popen('chrome.exe --remote-debugging-port=9527 --user-data-dir="E:\selenium" ')

        elif self.mode == '启动无痕模式':
            subprocess.Popen('chrome.exe --remote-debugging-port=9527 --user-data-dir="E:\selenium" --incognito')

class driver_class:
    def __init__(self):
        pass

    def driver_Chrome(self, account):
        if account == 'account_01':
            return self.driver_01

    def driver_connect(self):
        options = Options()
        options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
        self.driver_01 = webdriver.Chrome(options=options)
        driver_class.driver_01 = self.driver_01

