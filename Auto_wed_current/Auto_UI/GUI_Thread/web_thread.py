from PyQt6.QtCore import pyqtSignal, QThread, QWaitCondition, QMutex, Qt

from Auto_wed_current.Auto_Post.post_window import post_window
from Auto_wed_current.Auto_execute.execute_summary import execute_summary
from Auto_wed_current.Auto_execute.execute_while import execute_while_value

class execute_thread(QThread): # 执行开始线程
    # 定义线程信号
    text_Edit = pyqtSignal(str)
    text_Edit_summary = pyqtSignal(str, str, str)
    text_Edit_logging = pyqtSignal(str) # 打印报错
    set_Enabled_bf = pyqtSignal()
    set_Enabled_af = pyqtSignal()
    set_Enabled_pa = pyqtSignal()
    set_Enabled_re = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.cond = QWaitCondition()
        self.mutex = QMutex()
        self._isPause = False
        execute_while_value.judge_pa_re = self.judge_pa_re
        execute_while_value.Edit_logging = self.Edit_logging
        execute_summary.Edit_summary = self.Edit_summary

    def pause(self):
        self._isPause = True
        self.set_Enabled_pa.emit()

    def resume(self):
        self._isPause = False
        self.set_Enabled_re.emit()
        self.cond.wakeOne()

    def judge_pa_re(self):
        if self._isPause:
            self.cond.wait(self.mutex)

    def Edit(self, text):
        self.text_Edit.emit(text)

    def Edit_summary(self, text, title, judge=None):
        self.text_Edit_summary.emit(text, title, judge)

    def Edit_logging(self, error_text):
        self.text_Edit_logging.emit(error_text)

    def bf(self):
        self.set_Enabled_bf.emit()

    def af(self):
        self.set_Enabled_af.emit()

    def run(self):
        self.mutex.lock()
        self.af()
        execute_summary(self.Edit).execute_result()
        self.bf()
        self.mutex.unlock()

class execute_summary_thread(QThread): # 结果总结线程
    text_summary = pyqtSignal(str, str, str)
    def __init__(self, *args, **kwargs):
        super(execute_summary_thread, self).__init__()
        self.mutex = QMutex()

    def Edit_summary(self, text, title, judge=None):
        self.text_summary.emit(self.text)

    def run(self):
        self.mutex.lock()
        self.text_summary.emit(self.Edit_summary)
        self.mutex.unlock()
