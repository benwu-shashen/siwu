from Auto_wed_current.Auto_base.error_reminder import error_reminder
from Auto_wed_current.Auto_driver.driver_class import driver_class


class handles(object):
    def __init__(self, action, text, account, handles_append):
        self.action = action
        self.text = text
        self.account = account
        self.handles_append = handles_append
        self.driver = driver_class().driver_Chrome(self.account)

    def handles_get(self):
        try:
            handles_all = self.driver.window_handles

        except Exception:
            raise error_reminder('handles_get')

        if self.action == '关闭窗口':
            try:
                del self.handles_append[int(self.text) - 1]
            except Exception:
                pass

        else:
            for data_01 in handles_all:
                if data_01 in self.handles_append:
                    pass
                elif data_01 not in self.handles_append:
                    self.handles_append.append(data_01)

        return self.handles_append
