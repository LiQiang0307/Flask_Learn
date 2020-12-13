import time
# from threading import get_ident, Thread
from threading import Thread

from greenlet import getcurrent as get_ident  # 协程


class Local(object):
    def __init__(self):
        # self.storage = {} #使用这行代码会报错
        object.__setattr__(self, 'storage', {})

    def __setattr__(self, k, v):
        ident = get_ident()
        if ident in self.storage:
            self.storage[ident][k] = v
        else:
            self.storage[ident] = {k: v}

    def __getattr__(self, k):
        ident = get_ident()
        return self.storage[ident][k]


obj = Local()


def task(arg):
    obj.val = arg
    time.sleep(2)
    print(obj.val)


for i in range(10):
    t = Thread(target=task, args=(i,))
    t.start()
