import re
import time
from time import sleep

# from jpype import *
from selenium.webdriver import ActionChains

from Auto_wed_current.Auto_base.error_reminder import error_reminder
from Auto_wed_current.Auto_driver.driver_class import driver_class

"""
操作行为函数，可在此添加各种操作行为
"""

def action_judge(row, action, account, text, handles_get, text_dirt):
    def text_variable(text):
        num_string = -1
        list_01 = []  # 变量值下标
        list_02 = []
        list_03 = []  # 变量列表

        for string in text:
            num_string += 1
            if string == '【':
                list_02 = []
                list_02.append(num_string)
                list_01.append(list_02)
            elif string == '】':
                list_02.append(num_string)
            if string == '《':
                list_02 = []
                list_02.append(num_string)
                list_01.append(list_02)
            elif string == '》':
                list_02.append(num_string)

        if list_01 == []:
            raise error_reminder('xpath_text_04', text=list_01)

        for num in list_01:
            if text[num[0]] + text[num[1]] == '【】' or text[num[0]] + text[num[1]] == '《》':
                pass
            else:
                raise error_reminder('xpath_text_02', text=text[0])  # 判断获取的字符是否符合填写格式，如果不符合填写格式，则会报错

        for num in list_01:
            string_value = ''
            for x in range(num[0], num[1] + 1):
                string_value += text[x]
            list_03.append(string_value)  # 获取变量值，循环每一个字符，符合条件的字符就相加，最终生成一个列表变量

        return list_01, list_03

    def coordinate_text_retrieval(x, y):
        js = """
                        window.hovered_element = null
                        function track_mouse(event){
                         var element = document.elementFromPoint(%s, %s)
                          if (!element) {
                              window.hovered_element = null
                          return // 当前位置没有元素
                         }
                          window.hovered_element = element
                        }
                        window.onmousemove = track_mouse
                        """ % (x, y)

        driver.execute_script(js)  # 可以参考该https://cloud.tencent.com/developer/article/1974407

        """
        可在浏览器的控制器中输入
        function track_mouse(event){
         var x = event.clientX, y = event.clientY
         console.log('当前鼠标所在位置的坐标：x=' +  x + 'y=' + y)
        }

        回车，然后再输入
        window.onmousemove = track_mouse

        回车，鼠标悬浮浏览器页面，就会快速打印鼠标坐标
        """
        try:
            ActionChains(driver).move_by_offset(x, y).perform()
            ActionChains(driver).reset_actions()
        except Exception:
            raise error_reminder('action_move_by_offset')

        element = driver.execute_script('return window.hovered_element')  # 如果此处报错gdk的问题，可以修改文件编码，全局编码和项目编码都改为utf-8
        if element:
            text_value_all = element.text
            return text_value_all
        else:
            return ''

    driver = driver_class().driver_Chrome(account)
    if action == '其他-输入网址':
        driver.get(text)
        sleep(1)

    elif action == '其他-窗口最大化':
        driver.maximize_window()
        sleep(1)

    elif action == '其他-窗口最小化':
        driver.minimize_window()
        sleep(1)

    elif action == '其他-切换窗口':
        try:
            driver.switch_to.window(handles_get[int(text) - 1])
        except Exception:
            raise error_reminder('action_handles_01')

        sleep(1)

    elif action == '其他-清除句柄':
        try:
            del handles_get[int(text) - 1]
        except Exception:
            raise error_reminder('action_handles_02')
        return handles_get

    elif action == '其他-关闭窗口或标签':
        try:
            driver.switch_to.window(handles_get[int(text) - 1])
        except Exception:
            raise error_reminder('action_handles')

        driver.close()
        sleep(1)

    elif action == '其他-新建标签':
        driver.switch_to.new_window('tab')
        sleep(1)

    elif action == '其他-新建窗口':
        driver.switch_to.new_window('window')
        sleep(1)

    elif action == '其他-刷新页面':
        driver.refresh()
        sleep(1)

    elif action == '其他-关闭浏览器':
        driver.quit()
        sleep(1)

    elif action == '其他-切换主框架':
        driver.switch_to.default_content()
        sleep(1)

    elif action == '其他-强制等待':
        time.sleep(int(text))

    elif action == '其他-坐标-点击': # 通过浏览器坐标点击操作
        coordinate =  re.split(',', text)

        for num in coordinate:
            try:
                if int(num):
                    pass
            except Exception:
                raise error_reminder('action_format_02', text=coordinate)

        try:
            ActionChains(driver).move_by_offset(coordinate[0], coordinate[1]).click().perform()
            ActionChains(driver).reset_actions()
        except Exception:
            raise error_reminder('action_move_by_offset')

    elif action == '其他-坐标-文本框输入':  # 通过浏览器坐标输入文本框内容
        if '-->' not in text:
            raise error_reminder('action_format')

        elif '-->' in text:
            data = re.split('-->', text)
            coordinate = re.split(',', data[0])

            for num in coordinate:
                try:
                    if int(num):
                        pass
                except Exception:
                    raise error_reminder('action_format_02', text=coordinate)

            def substitute_variable(value):
                data_6 = []
                for key in text_dirt:
                    if key in (value):
                        data_6.append(key)

                if data_6 != []:
                    for variable in data_6:
                        value = value.replace(variable, text_dirt[variable])

                return value

            def text_value(value):
                data_1 = re.findall('%H:%M:%S', value)  # 读取指定内容

                if data_1 == []:
                    value = substitute_variable(value)

                elif data_1[0] == '%H:%M:%S':
                    data_3 = value.strip('%H:%M:%S')  # 去掉时间戳内容
                    data_4 = time.strftime(data_1[0])  # 获取时间戳
                    data_5 = data_3 + data_4
                    value = substitute_variable(data_5)

                return value # 返回文本内容

            value = text_value(data[1])
            try:
                ActionChains(driver).move_by_offset(coordinate[0], coordinate[1]).click().perform()
                ActionChains(driver).reset_actions()
                ActionChains(driver).move_by_offset(coordinate[0], coordinate[1]).send_keys(value).perform()
                ActionChains(driver).reset_actions()
            except Exception:
                raise error_reminder('action_move_by_offset')

    elif action == '其他-坐标-获取文本':  # 通过浏览器坐标输入文本框内容
        if '-->' not in text:
            raise error_reminder('action_format')

        elif '-->' in text:
            oordinate_variables = re.split('-->', text)
            coordinate = re.split(',', oordinate_variables[0])

            if len(coordinate) != 2:
                raise error_reminder('action_format_01', text=coordinate)

            for num in coordinate:
                try:
                    if int(num):
                        pass
                except Exception:
                    raise error_reminder('action_format_02', text=coordinate)

            if '>>>' in (oordinate_variables[1]):
                data = re.split('>>>', oordinate_variables[1])

                capture_value = re.split(',', data[1])
                if len(capture_value) != 2:
                    raise error_reminder('action_format_06', text=data[1]) # 判断截取文本填写格式

                text_value_all = coordinate_text_retrieval(coordinate[0], coordinate[1])  # 获取文本

                if text_value_all == []:
                    raise error_reminder('action_format_03')

                value = re.compile('\{}(.*?)\{}'.format(capture_value[0], capture_value[1]))
                capture = value.findall(text_value_all)  # 循环整个文本，获取共有多少个截取片段，最终生成列表文本
                # capture：文本列表
                if capture == []:
                    raise error_reminder('action_format_04', text=capture)

                text_value_capture = ''  #
                text_value_capture_all = []

                text_variable_value = text_variable(data[0])


                if len(capture) != len(text_variable_value[1]):
                    raise error_reminder('action_format_05', text='变量数：{}，文本数：{}'.format(len(text_variable_value[1]), len(capture)))

                order = 0
                for num in text_variable_value[0]:
                    if data[0][num[0]] + data[0][num[1]] == '【】':
                        text_value_capture = capture_value[0] + capture[order] + capture_value[1]
                    elif data[0][num[0]] + data[0][num[1]] == '《》':
                        text_value_capture = capture[order]
                    order += 1

                    text_value_capture_all.append(text_value_capture)

                return text_variable_value[1], text_value_capture_all

            elif '>>>' not in (text):
                capture = []
                try:
                    text_value_capture_all = coordinate_text_retrieval(coordinate[0], [1])
                except Exception:
                    raise error_reminder('action_format_03')
                else:
                    text_variable_value = text_variable(text)
                    capture.append(text_value_capture_all)

                    if len(capture) != len(text_variable_value[1]):
                        raise error_reminder('action_format_05', text='变量数：{}，文本数：{}'.format(len(text_variable_value[1]), len(capture)))

                return text_variable_value[1], text_value_capture_all

    # elif action == '其他-图形交互_点击':
    #     data_1 = text.split(';')  # 读取指定内容
    #     data_file_1 = '{}{}{}{}图形交互_点击\\要点击的图片'.format(
    #         os.path.dirname(os.path.dirname(__file__)), os.sep, 'Auto_file', os.sep
    #     )
    #     data_file_2 = '{}{}{}{}图形交互_点击\\要识别的图片'.format(
    #         os.path.dirname(os.path.dirname(__file__)), os.sep, 'Auto_file', os.sep
    #     )
    #     data_file_3 = '{}{}{}{}sikulix\\sikulixide-2.0.5.jar'.format(
    #         os.path.dirname(__file__), os.sep, 'Auto_file', os.sep
    #     )
    #
    #     startJVM(getDefaultJVMPath(), "-ea",
    #              r"-Djava.class.path=C:\Users\16946\Desktop\web_UI\sikulixide-2.0.5.jar")  # path是刚才放的jar包位置，启动java虚拟机
    #     app = JClass('org.sikuli.script.App')
    #     app_path = r'C:\Program Files (x86)\NGVONE\Client\TopSAP.exe'
    #     app.open(app_path)
    #     Screen = JClass("org.sikuli.script.Screen")  # 获取java类
    #     screen = Screen()  # 生成类对象
    #     Key = JClass("org.sikuli.script.Key")
    #     key = Key()
    #     Pattern = JClass('org.sikuli.script.Pattern')
    #     KeyModifier = JClass('org.sikuli.script.KeyModifier')
    #     screen.doubleClick(data_file_1 + os.sep + data_1[0])  # 调用类对象的方法，双击快捷图片启动
    #     screen.click(data_file_2 + os.sep + data_1[1])




