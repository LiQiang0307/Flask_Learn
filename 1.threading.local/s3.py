import time
from threading import get_ident, Thread

storage={}

def set(k,v):
    ident=get_ident()
    if ident in storage:
        storage[ident][k]=v
    else:
        storage[ident]={k:v}


def get(k):
    ident=get_ident()
    return storage[ident][k]


def task(arg):
    set('val',arg)
    print(storage)
    time.sleep(2)
    v=get('val')
    print(v)


for i in range(10):
    t=Thread(target=task,args=(i,))
    t.start()