# 1.为什么要用装饰器》
"""
在不改变原函数的基础上，对函数执行前后进行自定义操作
"""
import functools

def wapper(func):
    @functools.wraps(func)  # 执行函数并获取 元信息
    def inner(*args,**kwargs):
        return func(*args,**kwargs)
    return inner

"""
1.执行wapper函数，并将装饰的函数当做参数。wapper（index）
2.将第一步的返回值，重新赋值给 新index =wapper(老 index)
"""
@wapper
def index(a1):
    return a1+1000

@wapper
def order(a1):
    return a1+1000

#执行
# v=index(2)
# print(v)
#获取函数名
print(index.__name__)
print(order.__name__)
