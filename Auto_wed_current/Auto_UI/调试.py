import os
import time

"""
连接当前浏览器，暂时注释，需要终端输入
chrome.exe --remote-debugging-port=9527 --user-data-dir="C:\selenium\AutomationProfile"
打开一个浏览器实例
#
# 可以添加多个浏览器同时多开账号
# """
#
# options = Options()
# options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
# driver = webdriver.Chrome(options=options)
# driver.get('https://baijiahao.baidu.com/s?id=1742093046408625280')
# 定义全局变量
# driver = webdriver.Chrome(options=options)
# driver.get('https://www.baidu.com/')

dir_01 = os.path.dirname
# filename_original = dir(dir(dir(__file__))) + os.sep + 'Auto_file' + os.sep + '原始导入excel模板'
# print(filename_original)
# print(dir(__file__))
# a = r'12345\22332\wewe'
# #从10到0进行遍历循环，括号里最后一个-1是步长，实现倒序；前两个参数是起始和终止值，也是前闭后开。
#
# filename_original = dir_01(__file__)
# filename_original_01 = ''
# for num in range(len(filename_original)-1, -1, -1):
#     if filename_original[num] == '\\':
#         dir = (filename_original[num+1 : len(filename_original)])
#         if dir == 'Auto_wed_current':
#             filename_original_01 = filename_original + os.sep + 'Auto_file' + os.sep + '原始导入excel模板'
#
#         elif dir != 'Auto_wed_current':
#             filename_original = dir_01(filename_original)
#
#     elif filename_original[num] != '\\':
#         print('失败')

# def filename(path):
#     dir = os.path.dirname
#     final_directory = ''
#     parent = dir(__file__)  # 当前目录
#     for num in range(len(parent) - 1, -1, -1):
#         if parent[num] == '\\':
#             current_name = (parent[num + 1: len(parent)])
#             if current_name == 'Auto_wed_current':
#                 final_directory = parent + path
#
#             elif current_name != 'Auto_wed_current':
#                 parent = dir(parent)
#
#         elif parent[num] != '\\':
#             pass
#
#     return final_directory
#
# filename_original = filename(r'\Auto_file\原始导入excel模板')
# filename_replace = filename(r'\Auto_file\替换导入excel模板')
# print(filename_replace)
# print(filename_original)
# self.filename_original = dir(dir(dir(__file__))) + os.sep + 'Auto_file' + os.sep + '原始导入excel模板'
# self.filename_replace = dir(dir(dir(__file__))) + os.sep + 'Auto_file' + os.sep + '替换导入excel模板'

curtime1 = time.strftime('%Y%m')
print(curtime1)

