from PyQt5.QtCore import pyqtSignal, QThread, QWaitCondition, QMutex

class web_thead_logging(QThread): # 执行开始线程
    logging_Edit = pyqtSignal()
    def __init__(self, *args, **kwargs):
        super(web_thead_logging, self).__init__(*args, **kwargs)
        self.cond = QWaitCondition()
        self.mutex = QMutex()

    def run(self):
        self.mutex.lock()
        print('你好')
        # self.logging_Edit.emit()
        self.mutex.unlock()

# class execute_thread(QThread): # 执行开始线程
#     text_Edit = pyqtSignal(str)
#     text_Edit_summary = pyqtSignal(str, str, str)
#     set_Enabled_bf = pyqtSignal()
#     set_Enabled_af = pyqtSignal()
#     set_Enabled_pa = pyqtSignal()
#     set_Enabled_re = pyqtSignal()
#     def __init__(self, *args, **kwargs):
#         super(execute_thread, self).__init__(*args, **kwargs)
#         self.cond = QWaitCondition()
#         self.mutex = QMutex()
#         self._isPause = False
#         execute_while_value.judge_pa_re = self.judge_pa_re
#         execute_summary.Edit_summary = self.Edit_summary
#
#     def pause(self):
#         self._isPause = True
#         self.set_Enabled_pa.emit()
#
#     def resume(self):
#         self._isPause = False
#         self.set_Enabled_re.emit()
#         self.cond.wakeOne()
#
#     def judge_pa_re(self):
#         if self._isPause:
#             self.cond.wait(self.mutex)
#
#     def Edit(self, text):
#         self.text_Edit.emit(text)
#
#     def Edit_summary(self, text, title, judge=None):
#         self.text_Edit_summary.emit(text, title, judge)
#
#     def bf(self):
#         self.set_Enabled_bf.emit()
#
#     def af(self):
#         self.set_Enabled_af.emit()
#
#     def run(self):
#         self.mutex.lock()
#         self.af()
#         execute_summary(self.Edit).execute_result()
#         self.bf()
#         self.mutex.unlock()