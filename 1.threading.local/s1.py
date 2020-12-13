import time
from threading import local,Thread,get_ident


"""
threading.local
作用：为每个线程开辟一块空间进行数据存储
问题：自己通过字典创建一个类似于threading.local的东西
"""

a=local()


def task(arg):
    a.value=arg
    time.sleep(2)
    print(a.value)
    print(get_ident())


for i in range(10):
    t=Thread(target=task,args=(i,))
    t.start()