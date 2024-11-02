from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 填写chromedriver的目录, 此处使用了相对路径
service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get("https://www.baidu.com")
print("你好")
