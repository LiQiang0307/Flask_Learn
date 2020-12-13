import time
from threading import local,Thread,get_ident

a=local()


def task(arg):
    print(get_ident())


for i in range(10):
    t=Thread(target=task,args=(i,))
    t.start()